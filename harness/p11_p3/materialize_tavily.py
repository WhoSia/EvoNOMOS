#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path

ARMS={"WIDE_BOUNDARY_REUSE","CAPABILITY_SEGREGATED"}

def repl(path:Path,old:str,new:str)->None:
    s=path.read_text()
    n=s.count(old)
    if n!=1: raise RuntimeError(f"{path}: anchor count {n} for {old[:80]!r}")
    path.write_text(s.replace(old,new,1))

def write(path:Path,s:str)->None:
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(s)

def tavily_provider(wide:bool)->str:
    fetch_import="  type WebFetchPages,\n" if wide else ""
    fetch_method="""
  async fetch(input: { urls: string[]; objective: string | undefined }): Promise<WebFetchPages> {
    void input.objective;
    const response = await this.#post('/extract', { urls: input.urls });
    const payload = (await response.json()) as {
      results?: Array<{ url?: string; raw_content?: string | null }>;
      failed_results?: Array<{ url?: string; error?: string | null }>;
    };
    const pages: WebFetchPages['pages'] = (payload.results ?? []).map(result => ({
      url: result.url ?? '',
      title: null,
      content: result.raw_content ?? '',
      error: null,
    }));
    const returned = new Set(pages.map(page => page.url));
    for (const failure of payload.failed_results ?? []) {
      const url = failure.url ?? '';
      pages.push({ url, title: null, content: '', error: failure.error ?? 'Tavily extract failed' });
      returned.add(url);
    }
    for (const url of input.urls) {
      if (!returned.has(url)) pages.push({ url, title: null, content: '', error: 'Tavily did not return content for URL' });
    }
    return { pages };
  }
""" if wide else ""
    return f"""import {{ ssrfFetch }} from '../util/ssrfGuard';
import {{
  WebSearchProviders,
  type IWebSearchProvider,
{fetch_import}  type WebSearchHits,
}} from './WebSearchProvider';

type FetchLike = (input: string | URL | Request, init?: RequestInit) => Promise<Response>;

export interface TavilyWebSearchProviderOptions {{
  apiKey?: string;
  baseUrl?: string;
  request?: FetchLike;
}}

export class TavilyWebSearchProvider implements IWebSearchProvider {{
  readonly id = WebSearchProviders.Tavily;
  readonly #apiKey: string | undefined;
  readonly #baseUrl: string;
  readonly #request: FetchLike;

  constructor(options: TavilyWebSearchProviderOptions = {{}}) {{
    const apiKey = options.apiKey?.trim();
    this.#apiKey = apiKey ? apiKey : undefined;
    this.#baseUrl = (options.baseUrl ?? 'https://api.tavily.com').replace(/\/+$/, '');
    this.#request = options.request ?? ssrfFetch;
  }}

  #headers(): Record<string,string> {{
    return this.#apiKey
      ? {{ 'content-type': 'application/json', Authorization: 'Bearer ' + this.#apiKey }}
      : {{ 'content-type': 'application/json', 'X-Tavily-Access-Mode': 'keyless' }};
  }}

  async #post(path: string, body: unknown): Promise<Response> {{
    const response = await this.#request(this.#baseUrl + path, {{
      method: 'POST',
      headers: this.#headers(),
      body: JSON.stringify(body),
    }});
    if (!response.ok) {{
      const text = await response.text();
      throw new Error('Tavily HTTP ' + response.status + ': ' + text.slice(0, 200));
    }}
    return response;
  }}

  async search(input: {{ search_queries: string[]; objective: string | undefined }}): Promise<WebSearchHits> {{
    void input.objective;
    const responses = await Promise.all(
      input.search_queries.map(async query => {{
        const response = await this.#post('/search', {{ query }});
        return (await response.json()) as {{
          results?: Array<{{ title?: string | null; url?: string; content?: string | null }}>;
        }};
      }}),
    );
    const seen = new Set<string>();
    const hits = [];
    for (const payload of responses) {{
      for (const result of payload.results ?? []) {{
        const url = result.url ?? '';
        if (!url || seen.has(url)) continue;
        seen.add(url);
        hits.push({{
          title: result.title ?? '',
          url,
          snippet: result.content ?? '',
          published_at: null,
        }});
      }}
    }}
    return {{ hits }};
  }}
{fetch_method}}}
"""

def patch_common(root:Path)->None:
    provider=root/"packages/trueforge-core/src/core/web-search/WebSearchProvider.ts"
    repl(provider,"  Exa = 'exa',\n}","  Exa = 'exa',\n  Tavily = 'tavily',\n}")

    idx=root/"packages/trueforge-core/src/core/index.ts"
    repl(idx,
      "export type { ExaWebSearchProviderOptions } from './web-search/ExaWebSearchProvider';\n",
      "export type { ExaWebSearchProviderOptions } from './web-search/ExaWebSearchProvider';\n"
      "export { TavilyWebSearchProvider } from './web-search/TavilyWebSearchProvider';\n"
      "export type { TavilyWebSearchProviderOptions } from './web-search/TavilyWebSearchProvider';\n")

    schema=root/"packages/trueforge/src/schemas/webSearchProvider.ts"
    anchor="""export const ExaWebSearchProviderSchema = z
  .object({
    type: z.literal('exa').describe('Exa web-search provider.'),
    auth: ExaWebSearchProviderAuthSchema,
  })
  .strict();

"""
    tav=anchor+"""const TavilyWebSearchProviderAuthSchema = z
  .object({
    api_key: z
      .string()
      .min(1)
      .optional()
      .describe('Optional Tavily API key. Omit for keyless mode; redacted values keep an existing stored key.'),
  })
  .strict()
  .describe('Tavily authentication credentials.')
  .openapi('TavilyWebSearchProviderAuth');

export const TavilyWebSearchProviderSchema = z
  .object({
    type: z.literal('tavily').describe('Tavily web-search provider.'),
    auth: TavilyWebSearchProviderAuthSchema,
  })
  .strict();

"""
    repl(schema,anchor,tav)
    repl(schema,
      "  .discriminatedUnion('type', [ParallelWebSearchProviderSchema, ExaWebSearchProviderSchema])",
      "  .discriminatedUnion('type', [ParallelWebSearchProviderSchema, ExaWebSearchProviderSchema, TavilyWebSearchProviderSchema])")

    cs=root/"packages/trueforge/src/schemas/webSearchCatalog.ts"
    s=cs.read_text()
    s=s.replace("import { ExaWebSearchProviderSchema, ParallelWebSearchProviderSchema } from './webSearchProvider';",
      "import { ExaWebSearchProviderSchema, ParallelWebSearchProviderSchema, TavilyWebSearchProviderSchema } from './webSearchProvider';")
    s=s.replace("const CatalogExaWebSearchProviderSchema = ExaWebSearchProviderSchema.omit({ auth: true }).strict();",
      "const CatalogExaWebSearchProviderSchema = ExaWebSearchProviderSchema.omit({ auth: true }).strict();\n"
      "const CatalogTavilyWebSearchProviderSchema = TavilyWebSearchProviderSchema.omit({ auth: true }).strict();")
    s=s.replace("[CatalogParallelWebSearchProviderSchema, CatalogExaWebSearchProviderSchema]",
      "[CatalogParallelWebSearchProviderSchema, CatalogExaWebSearchProviderSchema, CatalogTavilyWebSearchProviderSchema]")
    cs.write_text(s)

    cat=root/"packages/trueforge/catalog/web-search-catalog.yaml"
    repl(cat,"  - type: exa\n","  - type: exa\n  - type: tavily\n")

    resolver=root/"packages/trueforge/src/websearch/providers.ts"
    s=resolver.read_text()
    s=s.replace("  ParallelWebSearchProvider,\n", "  ParallelWebSearchProvider,\n  TavilyWebSearchProvider,\n")
    s=s.replace("    case 'exa':\n      return new ExaWebSearchProvider({ apiKey: manifest.auth.api_key });\n",
      "    case 'exa':\n      return new ExaWebSearchProvider({ apiKey: manifest.auth.api_key });\n"
      "    case 'tavily':\n      return new TavilyWebSearchProvider(\n        manifest.auth.api_key === undefined ? {} : { apiKey: manifest.auth.api_key },\n      );\n")
    resolver.write_text(s)

    api=root/"packages/trueforge/src/apis/webSearchProviders.ts"
    old="""function redactWebSearchProvider(manifest: WebSearchProviderManifest): WebSearchProviderManifest {
  return {
    ...manifest,
    auth: { api_key: toRedactedSecretValue(manifest.auth.api_key) },
  };
}

function resolveWebSearchProviderManifestForWrite({
  incoming,
  existing,
}: {
  incoming: WebSearchProviderManifest;
  existing: WebSearchProviderManifest | undefined;
}): WebSearchProviderManifest {
  return {
    ...incoming,
    auth: {
      api_key: resolveStoredSecretValue({
        incoming: incoming.auth.api_key,
        existing: existing?.auth.api_key,
      }),
    },
  };
}
"""
    new="""function redactWebSearchProvider(manifest: WebSearchProviderManifest): WebSearchProviderManifest {
  if (manifest.type === 'tavily') {
    return {
      ...manifest,
      auth:
        manifest.auth.api_key === undefined
          ? {}
          : { api_key: toRedactedSecretValue(manifest.auth.api_key) },
    };
  }
  return {
    ...manifest,
    auth: { api_key: toRedactedSecretValue(manifest.auth.api_key) },
  };
}

function resolveWebSearchProviderManifestForWrite({
  incoming,
  existing,
}: {
  incoming: WebSearchProviderManifest;
  existing: WebSearchProviderManifest | undefined;
}): WebSearchProviderManifest {
  if (incoming.type === 'tavily') {
    const incomingKey = incoming.auth.api_key;
    if (incomingKey === undefined) {
      return { ...incoming, auth: {} };
    }
    const existingKey = existing?.type === 'tavily' ? existing.auth.api_key : undefined;
    return {
      ...incoming,
      auth: {
        api_key: resolveStoredSecretValue({ incoming: incomingKey, existing: existingKey }),
      },
    };
  }
  return {
    ...incoming,
    auth: {
      api_key: resolveStoredSecretValue({
        incoming: incoming.auth.api_key,
        existing: existing?.auth.api_key,
      }),
    },
  };
}
"""
    repl(api,old,new)

def write_tests(root:Path,arm:str)->None:
    wide=arm=="WIDE_BOUNDARY_REUSE"
    expected="['web_search', 'web_fetch']" if wide else "['web_search']"
    fetch="""
    const fetched = await keyed.fetch({ urls: ['https://fixture.invalid/page'], objective: 'read page' });
    expect(fetched.pages[0]?.content).toBe('tavily deterministic page content');
""" if wide else ""
    fetch_status="'PASS'" if wide else "'HIDDEN'"
    test=f"""import {{ writeFileSync }} from 'node:fs';
import {{ TavilyWebSearchProvider }} from '../../../src/core/web-search/TavilyWebSearchProvider';
import {{ WebSearchProviders, type IWebSearchProvider }} from '../../../src/core/web-search/WebSearchProvider';
import {{ WEB_FETCH_TOOL_NAME, WEB_SEARCH_TOOL_NAME, WebSearchTools }} from '../../../src/core/capabilities/builtins/WebSearch';
import {{ NOOP_AGENT_TRACING }} from '../../../src/core/tracing/NoopAgentTracing';

async function names(provider: IWebSearchProvider): Promise<string[]> {{
  const listed = await new WebSearchTools({{ provider, tracing: NOOP_AGENT_TRACING }}).listTools();
  if ('authRequired' in listed) throw new Error('unexpected auth');
  return listed.result.tools.map(x => x.name);
}}

describe('EvoNOMOS Tavily phase1 contract', () => {{
  it('supports keyed and keyless search and treatment-specific exposure', async () => {{
    const base=process.env['EVONOMOS_ORACLE_BASE_URL']; const probeOut=process.env['EVONOMOS_PROBE_OUT'];
    if(!base||!probeOut) throw new Error('missing oracle env');

    const keyed=new TavilyWebSearchProvider({{apiKey:'tavily-test-key',baseUrl:base+'/tavily',request:globalThis.fetch.bind(globalThis)}});
    const keyless=new TavilyWebSearchProvider({{baseUrl:base+'/tavily',request:globalThis.fetch.bind(globalThis)}});
    for (const provider of [keyed,keyless]) {{
      await expect(provider.search({{search_queries:['conditional design'],objective:'fixture'}})).resolves.toEqual({{
        hits:[{{title:'Tavily fixture',url:'https://fixture.invalid/tavily',snippet:'tavily deterministic snippet',published_at:null}}],
      }});
    }}
{fetch}
    const tavilyTools=await names(keyed);
    expect(tavilyTools).toEqual({expected});
    const parallel:IWebSearchProvider={{id:WebSearchProviders.Parallel,search:async()=>({{hits:[]}}),fetch:async()=>({{pages:[]}})}};
    const parallelTools=await names(parallel);
    expect(parallelTools).toEqual([WEB_SEARCH_TOOL_NAME,WEB_FETCH_TOOL_NAME]);
    writeFileSync(probeOut,JSON.stringify({{
      treatment:'{arm}',network:'MOCK_ONLY',secret_leak:false,
      parallel:{{tools:parallelTools,search:'PASS',fetch:'PASS'}},
      phase1:{{provider:'tavily',tools:tavilyTools,search:'PASS',fetch:{fetch_status},keyed:'PASS',keyless:'PASS'}}
    }},null,2)+'\\n');
  }});
}});
"""
    write(root/"packages/trueforge-core/tests/core/web-search/EvoNomosTavilyProvider.test.ts",test)

    settings="""import { WebSearchProviders } from '@truefoundry/trueforge-core/core';
import { createWebSearchProvidersRouter } from '../../../src/apis/webSearchProviders';
import { STANDALONE_REQUEST_CONTEXT } from '../../../src/auth/identity';
import { migrateSqliteToLatest } from '../../../src/db/migrateSqlite';
import { createSqliteDb } from '../../../src/db/sqlite/client';
import { SqliteWebSearchProviderStore } from '../../../src/db/sqlite/web-search-provider-store/SqliteWebSearchProviderStore';
import { toRedactedSecretValue } from '../../../src/utils/secretRedaction';
import { resolveWebSearchProvider } from '../../../src/websearch/providers';

const put=(manifest:unknown):RequestInit=>({method:'PUT',headers:{'content-type':'application/json'},body:JSON.stringify({manifest})});

describe('EvoNOMOS Tavily settings/runtime contract',()=> {
  it('supports keyless, keyed, redacted keep, clear-to-keyless, and runtime resolution',async()=> {
    const db=createSqliteDb(':memory:'); await migrateSqliteToLatest(db);
    const store=new SqliteWebSearchProviderStore(db);
    const router=createWebSearchProvidersRouter({resolveWebSearchProviderStore:()=>store,resolveRequestContext:()=>STANDALONE_REQUEST_CONTEXT});

    const keyless=await router.request('/',put({type:'tavily',auth:{}}));
    expect(keyless.status).toBe(200);
    expect(await keyless.json()).toEqual({data:{name:'tavily',manifest:{type:'tavily',auth:{}}}});
    expect((await resolveWebSearchProvider({tenant_id:'default',store}))?.id).toBe(WebSearchProviders.Tavily);

    const key='tavily-secret-key';
    const keyed=await router.request('/',put({type:'tavily',auth:{api_key:key}}));
    expect(keyed.status).toBe(200);
    expect(await keyed.json()).toEqual({data:{name:'tavily',manifest:{type:'tavily',auth:{api_key:toRedactedSecretValue(key)}}}});
    expect((await store.getProvider('default'))?.manifest).toEqual({type:'tavily',auth:{api_key:key}});

    const kept=await router.request('/',put({type:'tavily',auth:{api_key:toRedactedSecretValue(key)}}));
    expect(kept.status).toBe(200);
    expect((await store.getProvider('default'))?.manifest).toEqual({type:'tavily',auth:{api_key:key}});

    const cleared=await router.request('/',put({type:'tavily',auth:{}}));
    expect(cleared.status).toBe(200);
    expect((await store.getProvider('default'))?.manifest).toEqual({type:'tavily',auth:{}});

    const invalid=await router.request('/',put({type:'tavily',auth:{api_key:''}}));
    expect(invalid.status).toBe(400);
  });
});
"""
    write(root/"packages/trueforge/tests/unit/apis/webSearchProviders.tavily.evonomos.test.ts",settings)

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument("--arm",required=True,choices=sorted(ARMS)); ap.add_argument("--subject",required=True,type=Path); ap.add_argument("--out",required=True,type=Path)
    a=ap.parse_args()
    product=[
      a.subject/"packages/trueforge-core/src/core/web-search/WebSearchProvider.ts",
      a.subject/"packages/trueforge/src/schemas/webSearchProvider.ts",
      a.subject/"packages/trueforge/src/schemas/webSearchCatalog.ts",
      a.subject/"packages/trueforge/catalog/web-search-catalog.yaml",
      a.subject/"packages/trueforge/src/websearch/providers.ts",
      a.subject/"packages/trueforge/src/apis/webSearchProviders.ts",
    ]
    if any("tavily" in p.read_text().lower() for p in product): raise RuntimeError("Tavily already present in P2 product parent")
    patch_common(a.subject)
    write(a.subject/"packages/trueforge-core/src/core/web-search/TavilyWebSearchProvider.ts",tavily_provider(a.arm=="WIDE_BOUNDARY_REUSE"))
    write_tests(a.subject,a.arm)
    a.out.mkdir(parents=True,exist_ok=True)
    (a.out/"phase1-materialization.json").write_text(json.dumps({"stage":"EvoNOMOS Generation VIII ORIGIN-R1-P11-P3","arm":a.arm,"provider":"tavily","issue":853,"parent":"EXACT_P2_BUNDLE","coordinates_opened":False},indent=2)+"\n")
    print("MATERIALIZE_OK")
if __name__=="__main__": main()
