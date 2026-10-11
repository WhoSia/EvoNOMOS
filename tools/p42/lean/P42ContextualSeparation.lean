import P42HistoricalAuthorityNonidentifiability

/- P42-P2 — A FINITE observational-quotient court.
  Formal objects model a small declared semantics. PRE/POST signatures are
  hypotheses frozen before original Go CI; the ALT world is hypothetical.
  Full Echo v4 operational correctness, universal client completeness and a
  source-to-Lean refinement theorem are NOT asserted. -/
namespace P42P2

inductive World where
  | pre
  | post
  | alternate
  deriving Repr, DecidableEq

inductive Query where
  | health
  | bare
  | inlineVerb
  | otherSuffix
  deriving Repr, DecidableEq

/- Status and hidden parameter class. Pre/post projections deliberately
   share HTTP status for the inline-verb client but differ in binding. -/
def observe : World → Query → Nat × Nat
  | _, .health => (200, 0)
  | .pre, .bare => (200, 0)
  | .post, .bare => (404, 0)
  | .alternate, .bare => (404, 0)
  | .pre, .inlineVerb => (200, 0)
  | .post, .inlineVerb => (200, 1)
  | .alternate, .inlineVerb => (200, 0)
  | .pre, .otherSuffix => (200, 0)
  | .post, .otherSuffix => (404, 0)
  | .alternate, .otherSuffix => (404, 0)

def coarseHTTP (observation : Nat × Nat) : Nat := observation.1

def distinguish (suite : List Query) (x y : World) : Prop :=
  ∃ c, c ∈ suite ∧ observe x c ≠ observe y c

def separates (suite : List Query) : Prop :=
  ∀ x y : World, x ≠ y → distinguish suite x y

theorem masked_verb_same_status_but_different_parameter :
    coarseHTTP (observe .pre .inlineVerb) =
      coarseHTTP (observe .post .inlineVerb) ∧
    observe .pre .inlineVerb ≠ observe .post .inlineVerb := by decide

theorem health_context_does_not_distinguish_source_versions :
    observe World.pre Query.health =
      observe World.post Query.health := by decide

theorem bare_is_genuine_two_world_distinguisher :
    distinguish [.bare] .pre .post := by
  refine ⟨.bare, by simp, ?_⟩
  decide

theorem inline_is_hidden_two_world_distinguisher :
    distinguish [.inlineVerb] .pre .post := by
  refine ⟨.inlineVerb, by simp, ?_⟩
  decide

/- An *additional hypothetical implementation* has the same status
   signature as POST at bare but the same parameter signature as PRE
   at inlineVerb. Two different contexts are required to separate all
   three possibilities. This is a classical minimal distinguishing suite,
   not the minimal actual test set for all real Echo programs. -/
theorem bare_inline_is_separating_for_three_hypotheses :
    separates [.bare, .inlineVerb] := by
  intro x y h
  cases x <;> cases y
  all_goals simp_all [distinguish, observe]

theorem same_context_cannot_separate_distinct_worlds
    (x y : World) (q : Query)
    (different : x ≠ y) (equalOnQuery : observe x q = observe y q) :
    ¬ separates [q] := by
  intro h
  obtain ⟨query, inSuite, differentTrace⟩ := h x y different
  have onlyQuery : query = q := by simpa using inSuite
  subst query
  exact differentTrace equalOnQuery

theorem no_single_query_separates_all_three_hypotheses (q : Query) :
    ¬ separates [q] := by
  cases q with
  | health =>
      exact same_context_cannot_separate_distinct_worlds
        .pre .post .health (by decide) (by decide)
  | bare =>
      exact same_context_cannot_separate_distinct_worlds
        .post .alternate .bare (by decide) (by decide)
  | inlineVerb =>
      exact same_context_cannot_separate_distinct_worlds
        .pre .alternate .inlineVerb (by decide) (by decide)
  | otherSuffix =>
      exact same_context_cannot_separate_distinct_worlds
        .post .alternate .otherSuffix (by decide) (by decide)

/- General source-independent, classical contextual-equivalence refinement:
   a richer observation view implies equality of any of its projections.
   Its converse is not valid for the actual chosen inline-verb hypothesis. -/
def clientEquivalent (suite : List Query)
    (o : World → Query → Nat × Nat) (x y : World) : Prop :=
  ∀ q, q ∈ suite → o x q = o y q

theorem richer_observer_refines_status_observer
    (suite : List Query) (x y : World)
    (h : clientEquivalent suite observe x y) :
    ∀ q, q ∈ suite →
      coarseHTTP (observe x q) = coarseHTTP (observe y q) := by
  intro q hq
  exact congrArg coarseHTTP (h q hq)

theorem status_equivalence_not_parameter_equivalence :
    (∀ q, q ∈ [.inlineVerb] →
      coarseHTTP (observe .pre q) =
        coarseHTTP (observe .post q)) ∧
    ¬ clientEquivalent [.inlineVerb] observe .pre .post := by
  constructor
  · intro q hq
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hq
    subst q
    decide
  · intro h
    have hh := h Query.inlineVerb (by simp)
    have mismatch : observe .pre .inlineVerb ≠
      observe .post .inlineVerb := by decide
    exact mismatch hh

end P42P2
