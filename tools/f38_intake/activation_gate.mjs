/* F38 mechanical metadata audit only; never authenticates external evidence. */
export function assess(frame, episode = null) {
  const blockers = [];
  const require = (condition, label) => { if (!condition) blockers.push(label); };
  const digest = x => typeof x === "string" && /^[a-f0-9]{64}$/.test(x);
  const git = x => typeof x === "string" && /^[a-f0-9]{40}$/.test(x);
  const nonempty = x => typeof x === "string" && x.trim().length > 0;
  const url = x => typeof x === "string" && /^https:\/\/[^/\s]+\S*$/.test(x);
  const time = x => typeof x === "string" && /^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$/.test(x) &&
    Number.isFinite(Date.parse(x)) && new Date(Date.parse(x)).toISOString().replace(".000Z","Z") === x ? Date.parse(x) : NaN;
  const f = frame ?? {};
  const ids = Array.isArray(f.repository_ids) ? f.repository_ids : [];
  require(ids.length > 0 && ids.every(x => typeof x === "string" && /^[1-9]\d*$/.test(x)) &&
    new Set(ids).size === ids.length, "confirmed_frame_repository_ids");
  require(f.metadata_verified === true && url(f.frame_review_receipt), "frame_review");
  require(digest(f.frame_digest) && digest(f.protocol_digest) && digest(f.rival_policy_digest), "frame_protocol_rival_digests");
  const start = time(f.window_start), end = time(f.window_end), frozen = time(f.frozen_at);
  require(frozen < start && start < end, "frame_frozen_before_window");
  const stamp = f.timestamp_receipt ?? {};
  require(url(stamp.url) && nonempty(stamp.issuer) && stamp.issuer !== f.investigator &&
    stamp.digest === f.frame_digest && digest(stamp.digest) && frozen <= time(stamp.observed_at) &&
    time(stamp.observed_at) < start, "external_timestamp_metadata");
  require([f.investigator, f.selector, f.adjudicator].every(nonempty) &&
    new Set([f.investigator, f.selector, f.adjudicator]).size === 3 &&
    url(f.independence_review_receipt), "independent_roles_receipt");
  if (episode !== null) {
    const e = episode ?? {};
    require(ids.includes(e.repository_id), "repository_in_frame");
    require(url(e.issue_url) && nonempty(e.external_author) && e.external_author !== f.investigator &&
      e.research_authored === false && e.previously_exposed === false &&
      url(e.disclosure_receipt), "external_demand_metadata");
    const disclosed = time(e.disclosed_at), pairFrozen = time(e.pair_frozen_at), taskFrozen = time(e.task_frozen_at);
    require(start <= disclosed && disclosed < end && frozen <= pairFrozen &&
      pairFrozen < start && disclosed <= taskFrozen, "prospective_chronology");
    const arms = Array.isArray(e.arms) ? e.arms : [];
    require(arms.length === 2 && arms[0]?.id === "A" && arms[1]?.id === "B" &&
      arms.every(a => git(a.source_commit) && digest(a.manifest_digest)) &&
      arms[0]?.manifest_digest !== arms[1]?.manifest_digest, "distinct_pinned_source_arms");
    for (const key of ["rights_digest", "budget_digest", "input_digest", "oracle_digest"]) {
      require(arms.length === 2 && arms.every(a => digest(a[key])) &&
        arms[0]?.[key] === arms[1]?.[key], "matched_" + key);
    }
    require(url(e.behavior_match_receipt) && url(e.rights_review_receipt), "pair_and_rights_review");
    const preds = Array.isArray(e.predictors) ? e.predictors : [];
    require(preds.length === 2 && preds[0]?.id === "evonomos" && preds[1]?.id === "classical" &&
      preds.every(p => digest(p.prediction_digest) && digest(p.policy_digest) &&
        p.input_digest === arms[0]?.input_digest && time(p.frozen_at) === taskFrozen) &&
      preds[1]?.policy_digest === f.rival_policy_digest, "equal_information_frozen_predictions");
    require(e.repair_started_at === null || taskFrozen < time(e.repair_started_at), "prediction_before_repair");
    require(e.outcome_observed_at === null || (e.repair_started_at !== null &&
      taskFrozen < time(e.outcome_observed_at) && time(e.repair_started_at) <= time(e.outcome_observed_at)),
      "prediction_before_outcome");
    const kinds = e.candidate_classes ?? {};
    require(["configuration","extension","local","structural"].every(k =>
      ["CONSIDERED","INAPPLICABLE_WITH_REASON","UNKNOWN"].includes(kinds[k]?.status) &&
      nonempty(kinds[k]?.reason)), "complete_candidate_menu_account");
    require(e.adjudication_receipt === null || url(e.adjudication_receipt), "adjudication_receipt_format");
  }
  return {
    status: blockers.length ? "BLOCKED_METADATA" : "METADATA_CONSISTENT_MANUAL_REVIEW_REQUIRED",
    blockers, independent_timestamp_authenticated: false, actual_rights_verified: false,
    independent_adjudication_verified: false, activation_authorized: false, claim_promotion_authorized: false
  };
}
export function test() {
  const h = c => c.repeat(64);
  const f = {repository_ids:["123"],metadata_verified:true,frame_review_receipt:"https://example.org/frame",
    frame_digest:h("a"),protocol_digest:h("b"),rival_policy_digest:h("c"),
    window_start:"2026-11-28T00:00:00Z",window_end:"2026-12-12T00:00:00Z",frozen_at:"2026-11-27T14:00:00Z",
    timestamp_receipt:{url:"https://example.org/stamp",issuer:"external-service",digest:h("a"),observed_at:"2026-11-27T14:01:00Z"},
    investigator:"synthetic-investigator",selector:"synthetic-selector",adjudicator:"synthetic-adjudicator",
    independence_review_receipt:"https://example.org/roles"};
  const arm = id => ({id,source_commit:(id==="A"?"a":"b").repeat(40),manifest_digest:h(id==="A"?"d":"e"),
    rights_digest:h("f"),budget_digest:h("1"),input_digest:h("2"),oracle_digest:h("3")});
  const e = {repository_id:"123",issue_url:"https://example.org/issue/1",external_author:"synthetic-author",
    research_authored:false,previously_exposed:false,disclosure_receipt:"https://example.org/disclosure",
    disclosed_at:"2026-11-29T01:00:00Z",pair_frozen_at:"2026-11-27T14:02:00Z",task_frozen_at:"2026-11-29T02:00:00Z",
    arms:[arm("A"),arm("B")],behavior_match_receipt:"https://example.org/match",rights_review_receipt:"https://example.org/rights",
    predictors:[{id:"evonomos",prediction_digest:h("4"),policy_digest:h("5"),input_digest:h("2"),frozen_at:"2026-11-29T02:00:00Z"},
      {id:"classical",prediction_digest:h("6"),policy_digest:h("c"),input_digest:h("2"),frozen_at:"2026-11-29T02:00:00Z"}],
    repair_started_at:null,outcome_observed_at:null,adjudication_receipt:null,
    candidate_classes:Object.fromEntries(["configuration","extension","local","structural"].map(k=>[k,{status:"UNKNOWN",reason:"synthetic fixture"}]))};
  const clone = x => JSON.parse(JSON.stringify(x));
  const tests = [
    ["empty_frame", (f,e)=>{f.repository_ids=[]}],
    ["unverified_frame", (f,e)=>{f.metadata_verified=false}],
    ["wrong_stamp_digest", (f,e)=>{f.timestamp_receipt.digest=h("0")}],
    ["late_freeze", (f,e)=>{f.frozen_at=f.window_start}],
    ["invalid_calendar_date", (f,e)=>{f.window_end="2026-11-31T00:00:00Z"}],
    ["same_adjudicator", (f,e)=>{f.adjudicator=f.investigator}],
    ["outside_frame", (f,e)=>{e.repository_id="999"}],
    ["pre_window", (f,e)=>{e.disclosed_at="2026-11-27T13:00:00Z"}],
    ["known_exposure", (f,e)=>{e.previously_exposed=true}],
    ["late_pair_freeze", (f,e)=>{e.pair_frozen_at=e.disclosed_at}],
    ["unequal_rights", (f,e)=>{e.arms[1].rights_digest=h("0")}],
    ["unequal_oracle", (f,e)=>{e.arms[1].oracle_digest=h("0")}],
    ["different_rival_policy", (f,e)=>{e.predictors[1].policy_digest=h("0")}],
    ["different_rival_input", (f,e)=>{e.predictors[1].input_digest=h("0")}],
    ["outcome_before_prediction", (f,e)=>{e.repair_started_at="2026-11-29T01:30:00Z";e.outcome_observed_at="2026-11-29T01:45:00Z"}],
    ["missing_configuration", (f,e)=>{delete e.candidate_classes.configuration}],
  ];
  const results=tests.map(([name,mutate])=>{const ff=clone(f),ee=clone(e);mutate(ff,ee);const a=assess(ff,ee);
    if(a.status!=="BLOCKED_METADATA"||a.activation_authorized)throw Error("missed mutation: "+name);
    return {name,blockers:a.blockers};});
  const good=assess(f,e);
  if(good.status!=="METADATA_CONSISTENT_MANUAL_REVIEW_REQUIRED"||good.activation_authorized||good.claim_promotion_authorized)throw Error("synthetic admission");
  const empty=assess({});
  if(empty.status!=="BLOCKED_METADATA")throw Error("empty admission");
  return {negative_controls:results,positive_synthetic_metadata_only:good,empty_frame:empty};
}
