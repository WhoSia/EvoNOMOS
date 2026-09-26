#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ARMS = {"WIDE_BOUNDARY_REUSE", "CAPABILITY_SEGREGATED"}

def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{path}: expected exactly one anchor, found {n}: {old[:100]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def patch_common(root: Path) -> None:
    provider = root / "packages/trueforge-core/src/core/web-search/WebSearchProvider.ts"
    replace_once(
        provider,
        "export enum WebSearchProviders {\n  Parallel = 'parallel',\n}",
        "export enum WebSearchProviders {\n  Parallel = 'parallel',\n  Exa = 'exa',\n}",
    )

    index = root / "packages/trueforge-core/src/core/index.ts"
    replace_once(
        index,
        "export { ParallelWebSearchProvider } from './web-search/ParallelWebSearchProvider';\n",
        "export { ExaWebSearchProvider } from './web-search/ExaWebSearchProvider';\n"
        "export type { ExaWebSearchProviderOptions } from './web-search/ExaWebSearchProvider';\n"
        "export { ParallelWebSearchProvider } from './web-search/ParallelWebSearchProvider';\n",
    )

    schema = root / "packages/trueforge/src/schemas/webSearchProvider.ts"
    anchor = """export const ParallelWebSearchProviderSchema = z
  .object({
    type: z.literal('parallel').describe('Parallel web-search provider.'),
    auth: ParallelWebSearchProviderAuthSchema,
  })
  .strict();

"""
    exa = anchor + """const ExaWebSearchProviderAuthSchema = z
  .object({
    api_key: z
      .string()
      .min(1)
      .describe(
        'Exa API key. Responses are redacted; on PUT, a real value sets/rotates and a redacted value keeps the stored key.',
      ),
  })
  .strict()
  .describe('Exa authentication credentials.')
  .openapi('ExaWebSearchProviderAuth');

export const ExaWebSearchProviderSchema = z
  .object({
    type: z.literal('exa').describe('Exa web-search provider.'),
    auth: ExaWebSearchProviderAuthSchema,
  })
  .strict();

"""
    replace_once(schema, anchor, exa)
    replace_once(
        schema,
        "  .discriminatedUnion('type', [ParallelWebSearchProviderSchema])",
        "  .discriminatedUnion('type', [ParallelWebSearchProviderSchema, ExaWebSearchProviderSchema])",
    )

    catalog_schema = root / "packages/trueforge/src/schemas/webSearchCatalog.ts"
    write(
        catalog_schema,
        """import { z } from '@hono/zod-openapi';
import { ExaWebSearchProviderSchema, ParallelWebSearchProviderSchema } from './webSearchProvider';

const CatalogParallelWebSearchProviderSchema = ParallelWebSearchProviderSchema.omit({ auth: true }).strict();
const CatalogExaWebSearchProviderSchema = ExaWebSearchProviderSchema.omit({ auth: true }).strict();

export const CatalogWebSearchProviderSchema = z
  .discriminatedUnion('type', [CatalogParallelWebSearchProviderSchema, CatalogExaWebSearchProviderSchema])
  .openapi('CatalogWebSearchProvider');

export const WebSearchCatalogFileSchema = z
  .object({
    providers: z.array(CatalogWebSearchProviderSchema),
  })
  .strict();

export const GetWebSearchProviderCatalogResponseSchema = z
  .object({
    data: z.array(CatalogWebSearchProviderSchema),
  })
  .openapi('GetWebSearchProviderCatalogResponse');

export type CatalogWebSearchProvider = z.infer<typeof CatalogWebSearchProviderSchema>;
export type WebSearchCatalogFile = z.infer<typeof WebSearchCatalogFileSchema>;
""",
    )

    catalog = root / "packages/trueforge/catalog/web-search-catalog.yaml"
    write(catalog, "providers:\n  - type: parallel\n  - type: exa\n")

    resolver = root / "packages/trueforge/src/websearch/providers.ts"
    write(
        resolver,
        """import {
  ExaWebSearchProvider,
  ParallelWebSearchProvider,
  type IWebSearchProvider,
} from '@truefoundry/trueforge-core/core';
import type { IWebSearchProviderStore } from '../db/webSearchProviderStore';

export async function hasConfiguredWebSearchProvider({
  tenant_id,
  store,
}: {
  tenant_id: string;
  store: IWebSearchProviderStore;
}): Promise<boolean> {
  const record = await store.getProvider(tenant_id);
  return record !== undefined;
}

export async function resolveWebSearchProvider({
  tenant_id,
  store,
}: {
  tenant_id: string;
  store: IWebSearchProviderStore;
}): Promise<IWebSearchProvider | undefined> {
  const record = await store.getProvider(tenant_id);
  if (!record) {
    return undefined;
  }
  const { manifest } = record;
  switch (manifest.type) {
    case 'parallel':
      return new ParallelWebSearchProvider({ apiKey: manifest.auth.api_key, mode: 'turbo' });
    case 'exa':
      return new ExaWebSearchProvider({ apiKey: manifest.auth.api_key });
  }
}
""",
    )

def exa_provider(wide: bool) -> str:
    fetch_method = """
  async fetch(input: { urls: string[]; objective: string | undefined }): Promise<WebFetchPages> {
    const response = await this.#post('/contents', {
      urls: input.urls,
      text: true,
      ...(input.objective ? { context: input.objective } : {}),
    });
    const payload = (await response.json()) as {
      results?: Array<{ url?: string; title?: string | null; text?: string | null }>;
      statuses?: Array<{ id?: string; status?: string; error?: { tag?: string; httpStatusCode?: number } }>;
    };
    const pages: WebFetchPages['pages'] = (payload.results ?? []).map(result => ({
      url: result.url ?? '',
      title: result.title ?? null,
      content: result.text ?? '',
      error: null,
    }));
    const returned = new Set(pages.map(page => page.url));
    for (const url of input.urls) {
      if (!returned.has(url)) {
        pages.push({ url, title: null, content: '', error: 'Exa did not return content for URL' });
      }
    }
    return { pages };
  }
""" if wide else ""
    fetch_import = "  type WebFetchPages,\n" if wide else ""
    return f"""import {{ ssrfFetch }} from '../util/ssrfGuard';
import {{
  WebSearchProviders,
  type IWebSearchProvider,
{fetch_import}  type WebSearchHits,
}} from './WebSearchProvider';

type FetchLike = (input: string | URL | Request, init?: RequestInit) => Promise<Response>;

export interface ExaWebSearchProviderOptions {{
  apiKey: string;
  baseUrl?: string;
  request?: FetchLike;
}}

export class ExaWebSearchProvider implements IWebSearchProvider {{
  readonly id = WebSearchProviders.Exa;
  readonly #apiKey: string;
  readonly #baseUrl: string;
  readonly #request: FetchLike;

  constructor(options: ExaWebSearchProviderOptions) {{
    const apiKey = options.apiKey.trim();
    if (!apiKey) {{
      throw new Error('Exa API key is required');
    }}
    this.#apiKey = apiKey;
    this.#baseUrl = (options.baseUrl ?? 'https://api.exa.ai').replace(/\/+$/, '');
    this.#request = options.request ?? ssrfFetch;
  }}

  async #post(path: string, body: unknown): Promise<Response> {{
    const response = await this.#request(this.#baseUrl + path, {{
      method: 'POST',
      headers: {{
        'content-type': 'application/json',
        'x-api-key': this.#apiKey,
      }},
      body: JSON.stringify(body),
    }});
    if (!response.ok) {{
      const text = await response.text();
      throw new Error('Exa HTTP ' + response.status + ': ' + text.slice(0, 200));
    }}
    return response;
  }}

  async search(input: {{ search_queries: string[]; objective: string | undefined }}): Promise<WebSearchHits> {{
    const responses = await Promise.all(
      input.search_queries.map(async query => {{
        const response = await this.#post('/search', {{
          query,
          ...(input.objective ? {{ context: input.objective }} : {{}}),
        }});
        return (await response.json()) as {{
          results?: Array<{{
            title?: string | null;
            url?: string;
            publishedDate?: string | null;
            text?: string | null;
          }}>;
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
          snippet: result.text ?? '',
          published_at: result.publishedDate ?? null,
        }});
      }}
    }}
    return {{ hits }};
  }}
{fetch_method}}}
"""

def patch_wide(root: Path) -> None:
    write(root / "packages/trueforge-core/src/core/web-search/ExaWebSearchProvider.ts", exa_provider(True))

def patch_segregated(root: Path) -> None:
    provider = root / "packages/trueforge-core/src/core/web-search/WebSearchProvider.ts"
    old = """/**
 * Host-supplied web search backend. Implementations map vendor APIs onto
 * {@link WebSearchHits} / {@link WebFetchPages} so the capability tools stay provider-agnostic.
 */
export interface IWebSearchProvider {
  readonly id: WebSearchProviders;
  search(input: { search_queries: string[]; objective: string | undefined }): Promise<WebSearchHits>;
  fetch(input: { urls: string[]; objective: string | undefined }): Promise<WebFetchPages>;
}
"""
    new = """export interface IWebSearchCapability {
  search(input: { search_queries: string[]; objective: string | undefined }): Promise<WebSearchHits>;
}

export interface IWebFetchCapability {
  fetch(input: { urls: string[]; objective: string | undefined }): Promise<WebFetchPages>;
}

/**
 * Host-supplied web backend capabilities. Search is required by this provider
 * family; fetch/extract is an independently satisfiable capability.
 */
export type IWebSearchProvider = {
  readonly id: WebSearchProviders;
} & IWebSearchCapability &
  Partial<IWebFetchCapability>;

export function hasWebFetchCapability(
  provider: IWebSearchProvider,
): provider is IWebSearchProvider & IWebFetchCapability {
  return typeof provider.fetch === 'function';
}
"""
    replace_once(provider, old, new)

    parallel = root / "packages/trueforge-core/src/core/web-search/ParallelWebSearchProvider.ts"
    replace_once(
        parallel,
        "  type IWebSearchProvider,\n",
        "  type IWebFetchCapability,\n  type IWebSearchCapability,\n",
    )
    replace_once(
        parallel,
        "export class ParallelWebSearchProvider implements IWebSearchProvider {",
        "export class ParallelWebSearchProvider implements IWebSearchCapability, IWebFetchCapability {",
    )

    index = root / "packages/trueforge-core/src/core/index.ts"
    replace_once(
        index,
        "export { WebSearchProviders } from './web-search/WebSearchProvider';\nexport type {\n  IWebSearchProvider,\n",
        "export { WebSearchProviders, hasWebFetchCapability } from './web-search/WebSearchProvider';\nexport type {\n"
        "  IWebFetchCapability,\n  IWebSearchCapability,\n  IWebSearchProvider,\n",
    )

    web = root / "packages/trueforge-core/src/core/capabilities/builtins/WebSearch.ts"
    replace_once(
        web,
        "import type { IWebSearchProvider } from '../../web-search/WebSearchProvider';",
        "import { hasWebFetchCapability, type IWebSearchProvider } from '../../web-search/WebSearchProvider';",
    )
    full_builder_anchor = """export function buildWebSearchInstruction(builder: InstructionBuilder): void {
  builder.addSection(
    WEB_SEARCH_REMINDER_TAG,
    dedent`
      The Agent has two system tools for live web access: ${WEB_SEARCH_TOOL_NAME} (search) and ${WEB_FETCH_TOOL_NAME} (extract page content).

      When to use them:
      - The user asks to search, browse, verify, look up, or get latest information.
      - Facts may have changed recently (news, prices, laws, schedules, product specs, software APIs/docs, people in roles, rates, scores).
      - The answer needs direct quotes, links, or precise source attribution.
      - A specific page, paper, dataset, or site is referenced and its contents were not provided.

      How to use them:
      - Start with ${WEB_SEARCH_TOOL_NAME} for discovery; follow with ${WEB_FETCH_TOOL_NAME} on the best URLs when snippets are not enough.
      - Prefer primary and authoritative sources.
    `.trim(),
  );
}

"""
    search_only_builder = full_builder_anchor + """export function buildWebSearchOnlyInstruction(builder: InstructionBuilder): void {
  builder.addSection(
    WEB_SEARCH_REMINDER_TAG,
    dedent`
      The Agent has one system tool for live web discovery: ${WEB_SEARCH_TOOL_NAME}.

      Use it when the user asks to search, browse, verify, look up, or get latest information.
      Prefer primary and authoritative sources. This configured provider does not expose page extraction.
    `.trim(),
  );
}

"""
    replace_once(web, full_builder_anchor, search_only_builder)
    replace_once(
        web,
        "  protected getTools(): ToolDefinition[] {\n    return this.tools;\n  }",
        "  protected getTools(): ToolDefinition[] {\n"
        "    return hasWebFetchCapability(this.#provider)\n"
        "      ? this.tools\n"
        "      : this.tools.filter(tool => tool.name !== WEB_FETCH_TOOL_NAME);\n"
        "  }",
    )
    replace_once(
        web,
        """  private async runFetch(input: z.infer<typeof webFetchInputSchema>): Promise<CallToolResponse> {
    const result = await this.#provider.fetch({
      urls: input.urls,
      objective: input.objective,
    });
    return toolResultResponse({ text: JSON.stringify(result) });
  }
}

export function webSearch(options: { provider: IWebSearchProvider; tracing: AgentTracing }): AgentCapability {
  return {
    systemToolSets: [new WebSearchTools(options)],
    instructionBuilders: [buildWebSearchInstruction],
  };
}
""",
        """  private async runFetch(input: z.infer<typeof webFetchInputSchema>): Promise<CallToolResponse> {
    if (!hasWebFetchCapability(this.#provider)) {
      throw new Error('Configured web-search provider does not support web_fetch');
    }
    const result = await this.#provider.fetch({
      urls: input.urls,
      objective: input.objective,
    });
    return toolResultResponse({ text: JSON.stringify(result) });
  }
}

export function webSearch(options: { provider: IWebSearchProvider; tracing: AgentTracing }): AgentCapability {
  return {
    systemToolSets: [new WebSearchTools(options)],
    instructionBuilders: [
      hasWebFetchCapability(options.provider) ? buildWebSearchInstruction : buildWebSearchOnlyInstruction,
    ],
  };
}
""",
    )

    write(root / "packages/trueforge-core/src/core/web-search/ExaWebSearchProvider.ts", exa_provider(False))

def write_tests(root: Path, arm: str) -> None:
    wide = arm == "WIDE_BOUNDARY_REUSE"
    expected_tools = "['web_search', 'web_fetch']" if wide else "['web_search']"
    fetch_assert = """
    const fetched = await provider.fetch({
      urls: ['https://fixture.invalid/page'],
      objective: 'read page',
    });
    expect(fetched.pages[0]?.content).toContain('exa deterministic page content');
""" if wide else ""
    fetch_status = "'PASS'" if wide else "'HIDDEN'"
    test = f"""import {{ writeFileSync }} from 'node:fs';
import {{ ExaWebSearchProvider }} from '../../../src/core/web-search/ExaWebSearchProvider';
import {{ WebSearchProviders, type IWebSearchProvider }} from '../../../src/core/web-search/WebSearchProvider';
import {{
  WEB_FETCH_TOOL_NAME,
  WEB_SEARCH_TOOL_NAME,
  WebSearchTools,
}} from '../../../src/core/capabilities/builtins/WebSearch';
import {{ NOOP_AGENT_TRACING }} from '../../../src/core/tracing/NoopAgentTracing';

async function toolNames(provider: IWebSearchProvider): Promise<string[]> {{
  const toolSet = new WebSearchTools({{ provider, tracing: NOOP_AGENT_TRACING }});
  const listed = await toolSet.listTools();
  if ('authRequired' in listed) throw new Error('unexpected auth requirement');
  return listed.result.tools.map(tool => tool.name);
}}

describe('EvoNOMOS Exa phase0 contract', () => {{
  it('satisfies frozen wire behavior and treatment-specific capability exposure', async () => {{
    const base = process.env['EVONOMOS_ORACLE_BASE_URL'];
    const probeOut = process.env['EVONOMOS_PROBE_OUT'];
    if (!base || !probeOut) throw new Error('EvoNOMOS oracle/probe env missing');

    const provider = new ExaWebSearchProvider({{
      apiKey: 'exa-test-key',
      baseUrl: base + '/exa',
      request: globalThis.fetch.bind(globalThis),
    }});

    const result = await provider.search({{
      search_queries: ['conditional software design'],
      objective: 'fixture',
    }});
    expect(result.hits).toEqual([
      {{
        title: 'Exa fixture',
        url: 'https://fixture.invalid/exa',
        snippet: 'exa deterministic snippet',
        published_at: '2026-09-20T00:00:00Z',
      }},
    ]);

{fetch_assert}
    const exaTools = await toolNames(provider);
    expect(exaTools).toEqual({expected_tools});

    const parallelStub: IWebSearchProvider = {{
      id: WebSearchProviders.Parallel,
      search: async () => ({{ hits: [] }}),
      fetch: async () => ({{ pages: [] }}),
    }};
    const parallelTools = await toolNames(parallelStub);
    expect(parallelTools).toEqual([WEB_SEARCH_TOOL_NAME, WEB_FETCH_TOOL_NAME]);

    writeFileSync(
      probeOut,
      JSON.stringify(
        {{
          treatment: '{arm}',
          network: 'MOCK_ONLY',
          secret_leak: false,
          parallel: {{ tools: parallelTools, search: 'PASS', fetch: 'PASS' }},
          phase0: {{ provider: 'exa', tools: exaTools, search: 'PASS', fetch: {fetch_status} }},
          phase1: {{ provider: 'tavily', tools: [], search: 'SEALED', fetch: 'SEALED' }},
        }},
        null,
        2,
      ) + '\\n',
    );
  }});
}});
"""
    write(root / "packages/trueforge-core/tests/core/web-search/EvoNomosExaProvider.test.ts", test)

    settings_test = """import { WebSearchProviders } from '@truefoundry/trueforge-core/core';
import { createWebSearchProvidersRouter } from '../../../src/apis/webSearchProviders';
import { STANDALONE_REQUEST_CONTEXT } from '../../../src/auth/identity';
import { migrateSqliteToLatest } from '../../../src/db/migrateSqlite';
import { createSqliteDb } from '../../../src/db/sqlite/client';
import { SqliteWebSearchProviderStore } from '../../../src/db/sqlite/web-search-provider-store/SqliteWebSearchProviderStore';
import type { IWebSearchProviderStore } from '../../../src/db/webSearchProviderStore';
import { toRedactedSecretValue } from '../../../src/utils/secretRedaction';
import { resolveWebSearchProvider } from '../../../src/websearch/providers';

function putInit(manifest: unknown): RequestInit {
  return {
    method: 'PUT',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ manifest }),
  };
}

describe('EvoNOMOS Exa settings/runtime contract', () => {
  it('upserts, redacts, rotates/keeps secret and resolves Exa runtime', async () => {
    const db = createSqliteDb(':memory:');
    await migrateSqliteToLatest(db);
    const store = new SqliteWebSearchProviderStore(db);
    const router = createWebSearchProvidersRouter({
      resolveWebSearchProviderStore: () => store,
      resolveRequestContext: () => STANDALONE_REQUEST_CONTEXT,
    });

    const key = 'exa-secret-key';
    const created = await router.request('/', putInit({ type: 'exa', auth: { api_key: key } }));
    expect(created.status).toBe(200);
    expect(await created.json()).toEqual({
      data: {
        name: 'exa',
        manifest: { type: 'exa', auth: { api_key: toRedactedSecretValue(key) } },
      },
    });
    expect((await store.getProvider('default'))?.manifest).toEqual({ type: 'exa', auth: { api_key: key } });

    const kept = await router.request(
      '/',
      putInit({ type: 'exa', auth: { api_key: toRedactedSecretValue(key) } }),
    );
    expect(kept.status).toBe(200);
    expect((await store.getProvider('default'))?.manifest).toEqual({ type: 'exa', auth: { api_key: key } });

    const runtime = await resolveWebSearchProvider({
      tenant_id: 'default',
      store: store as unknown as IWebSearchProviderStore,
    });
    expect(runtime?.id).toBe(WebSearchProviders.Exa);

    const missing = await router.request('/', putInit({ type: 'exa', auth: { api_key: '' } }));
    expect(missing.status).toBe(400);
  });
});
"""
    write(root / "packages/trueforge/tests/unit/apis/webSearchProviders.evonomos.test.ts", settings_test)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True, choices=sorted(ARMS))
    ap.add_argument("--subject", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    patch_common(args.subject)
    if args.arm == "WIDE_BOUNDARY_REUSE":
        patch_wide(args.subject)
    else:
        patch_segregated(args.subject)
    write_tests(args.subject, args.arm)

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "materialization-manifest.json").write_text(
        json.dumps(
            {
                "stage": "EvoNOMOS Generation VIII ORIGIN-R1-P11-P2",
                "phase": 0,
                "provider": "exa",
                "arm": args.arm,
                "source": "dd421b79216c9b42eefd7b0191e546919f8be3f1",
                "tavily_opened": False,
                "comparative_coordinates_opened": False,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print("MATERIALIZE_OK")

if __name__ == "__main__":
    main()
