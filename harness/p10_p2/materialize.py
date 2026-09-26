#!/usr/bin/env python3
"""Deterministically materialize the two P10-P2 treatment arms.

The script is deliberately source-locked to
2GT-Media-Group-LLC/mikrotik-manager@68f3c7fc50a91f7dee79f7af914d9dd205498fc7.

It does not measure comparative outcomes. It creates treatment bytes, common
contract tests, and a machine-readable manifest for later independent custody
and pair-comparability verification.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

BASE = "68f3c7fc50a91f7dee79f7af914d9dd205498fc7"
ARMS = {"DIRECT_DEDICATED", "INVERT_CHANNEL_ADAPTER"}

COMMON_FILES = [
    "backend/src/db/migrate.ts",
    "frontend/src/services/api.ts",
    "frontend/src/pages/SettingsPage.tsx",
    "backend/src/services/__tests__/Gotify.contract.test.ts",
    "backend/src/routes/__tests__/alerts-gotify.contract.test.ts",
]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{path}: expected exactly one anchor, found {n}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

def insert_before_once(path: Path, anchor: str, payload: str) -> None:
    replace_once(path, anchor, payload + anchor)

def verify_base(subject: Path) -> None:
    head = subprocess.check_output(
        ["git", "-C", str(subject), "rev-parse", "HEAD"], text=True
    ).strip()
    if head != BASE:
        raise RuntimeError(f"wrong subject HEAD: {head} != {BASE}")
    if subprocess.run(
        ["git", "-C", str(subject), "diff", "--quiet"], check=False
    ).returncode != 0:
        raise RuntimeError("subject worktree is dirty before materialization")

def patch_common(subject: Path) -> None:
    api = subject / "frontend/src/services/api.ts"
    settings = subject / "frontend/src/pages/SettingsPage.tsx"
    migrate = subject / "backend/src/db/migrate.ts"
    service = subject / "backend/src/services/AlertService.ts"
    routes = subject / "backend/src/routes/alerts.ts"

    replace_once(
        api,
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy';",
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy' | 'gotify';",
    )

    replace_once(
        settings,
        "(['slack', 'discord', 'telegram', 'ntfy', 'email'] as const)",
        "(['slack', 'discord', 'telegram', 'ntfy', 'gotify', 'email'] as const)",
    )
    gotify_ui = """              ) : chForm.type === 'gotify' ? (
                <>
                  <div>
                    <label className="block text-xs font-medium text-gray-600 dark:text-slate-400 mb-1">Server URL</label>
                    <input className="input w-full font-mono text-xs" value={cfgStr('server_url')} onChange={(e) => setCfg('server_url', e.target.value)} placeholder="https://gotify.example.com" />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-gray-600 dark:text-slate-400 mb-1">Application Token</label>
                    <input type="password" className="input w-full font-mono text-xs" value={cfgStr('app_token')} onChange={(e) => setCfg('app_token', e.target.value)} placeholder="A..." />
                  </div>
                </>
"""
    replace_once(
        settings,
        "              ) : chForm.type === 'ntfy' ? (\n",
        gotify_ui + "              ) : chForm.type === 'ntfy' ? (\n",
    )

    old_check = "CHECK (type IN ('email','slack','discord','telegram','ntfy'))"
    new_check = "CHECK (type IN ('email','slack','discord','telegram','ntfy','gotify'))"
    migrate_text = migrate.read_text(encoding="utf-8")
    if migrate_text.count(old_check) != 2:
        raise RuntimeError("migrate.ts: expected exactly two alert-channel CHECK anchors")
    migrate.write_text(migrate_text.replace(old_check, new_check), encoding="utf-8")

    replace_once(
        service,
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy';",
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy' | 'gotify';",
    )

    gotify_sender = """  private gotifyPriority(eventType: string): number {
    if (['device_offline', 'log_error', 'high_cpu', 'high_memory'].includes(eventType)) return 4;
    if (['device_online', 'device_discovered'].includes(eventType)) return 2;
    return 3;
  }

  private async sendGotify(
    cfg: Record<string, unknown>,
    eventType: string,
    message: string,
    ctx: AlertContext
  ): Promise<void> {
    const serverUrl = ((cfg.server_url as string | undefined)?.trim() || '').replace(/\\/+$/, '');
    const appToken = (cfg.app_token as string | undefined)?.trim() || '';
    if (!serverUrl) throw new Error('Gotify channel missing server_url');
    if (!appToken) throw new Error('Gotify channel missing app_token');

    let parsed: URL;
    try {
      parsed = new URL(serverUrl);
    } catch {
      throw new Error('Gotify channel has an invalid server_url: ' + serverUrl);
    }
    if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
      throw new Error('Gotify server_url must be http or https');
    }

    const label = EVENT_LABELS[eventType] ?? eventType;
    const emoji = EVENT_EMOJI[eventType] ?? '🔔';
    const lines = [message];
    if (ctx.deviceName) lines.push('Device: ' + ctx.deviceName);
    if (ctx.details) lines.push(ctx.details);

    const body = JSON.stringify({
      title: emoji + ' ' + label,
      message: lines.join('\\n'),
      priority: this.gotifyPriority(eventType),
    });
    await this.postJson(serverUrl + '/message', body, { 'X-Gotify-Key': appToken });
  }

"""
    insert_before_once(service, "  private async sendNtfy(\n", gotify_sender)

    replace_once(routes, "function maskConfig(", "export function maskConfig(")
    replace_once(routes, "function mergeConfig(", "export function mergeConfig(")

    service_test = subject / "backend/src/services/__tests__/Gotify.contract.test.ts"
    service_test.write_text(GOTIFY_SERVICE_TEST, encoding="utf-8")
    route_test = subject / "backend/src/routes/__tests__/alerts-gotify.contract.test.ts"
    route_test.parent.mkdir(parents=True, exist_ok=True)
    route_test.write_text(GOTIFY_ROUTE_TEST, encoding="utf-8")

def patch_direct(subject: Path) -> None:
    service = subject / "backend/src/services/AlertService.ts"
    routes = subject / "backend/src/routes/alerts.ts"

    replace_once(
        service,
        "      case 'ntfy':     await this.sendNtfy(ch.config, eventType, message, ctx); break;\n",
        "      case 'ntfy':     await this.sendNtfy(ch.config, eventType, message, ctx); break;\n"
        "      case 'gotify':   await this.sendGotify(ch.config, eventType, message, ctx); break;\n",
    )
    replace_once(
        routes,
        "const validTypes = ['email', 'slack', 'discord', 'telegram', 'ntfy'];",
        "const validTypes = ['email', 'slack', 'discord', 'telegram', 'ntfy', 'gotify'];",
    )
    replace_once(
        routes,
        "  ntfy:     ['token', 'password'],\n",
        "  ntfy:     ['token', 'password'],\n  gotify:   ['app_token'],\n",
    )

def patch_invert(subject: Path) -> None:
    service = subject / "backend/src/services/AlertService.ts"
    routes = subject / "backend/src/routes/alerts.ts"
    registry = subject / "backend/src/services/ChannelProviderRegistry.ts"
    registry.write_text(CHANNEL_PROVIDER_REGISTRY, encoding="utf-8")

    replace_once(
        service,
        "import { query } from '../config/database';\n",
        "import { query } from '../config/database';\n"
        "import { AlertChannelType, getChannelProvider } from './ChannelProviderRegistry';\n",
    )
    replace_once(
        service,
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy' | 'gotify';",
        "type: AlertChannelType;",
    )

    old_switch = """    switch (ch.type) {
      case 'email':    await this.sendEmail(ch.config, eventType, message, ctx); break;
      case 'slack':    await this.sendSlack(ch.config, eventType, message, ctx); break;
      case 'discord':  await this.sendDiscord(ch.config, eventType, message, ctx); break;
      case 'telegram': await this.sendTelegram(ch.config, eventType, message, ctx); break;
      case 'ntfy':     await this.sendNtfy(ch.config, eventType, message, ctx); break;
    }
"""
    new_dispatch = """    const provider = getChannelProvider(ch.type);
    provider.validate(ch.config);
    type Sender = (
      cfg: Record<string, unknown>,
      eventType: string,
      message: string,
      ctx: AlertContext
    ) => Promise<void>;
    const sender = (this as unknown as Record<string, Sender>)[provider.sendMethod];
    if (typeof sender !== 'function') {
      throw new Error('Alert provider sender is unavailable: ' + provider.sendMethod);
    }
    await sender.call(this, ch.config, eventType, message, ctx);
"""
    replace_once(service, old_switch, new_dispatch)

    replace_once(
        routes,
        "import { alertService } from '../services/AlertService';\n",
        "import { alertService } from '../services/AlertService';\n"
        "import { SUPPORTED_CHANNEL_TYPES, sensitiveKeysFor } from '../services/ChannelProviderRegistry';\n",
    )
    replace_once(
        routes,
        "const validTypes = ['email', 'slack', 'discord', 'telegram', 'ntfy'];",
        "const validTypes = SUPPORTED_CHANNEL_TYPES;",
    )
    sensitive_block = """const SENSITIVE_KEYS: Record<string, string[]> = {
  email:    ['smtp_pass'],
  slack:    [],
  discord:  [],
  telegram: ['bot_token'],
  // ntfy accepts either an access token or basic auth; both are secrets.
  ntfy:     ['token', 'password'],
};

"""
    replace_once(routes, sensitive_block, "")
    old_loop = "for (const key of SENSITIVE_KEYS[type] ?? []) {"
    new_loop = "for (const key of sensitiveKeysFor(type)) {"
    routes_text = routes.read_text(encoding="utf-8")
    if routes_text.count(old_loop) != 2:
        raise RuntimeError("alerts.ts: expected exactly two sensitive-key loops")
    routes.write_text(routes_text.replace(old_loop, new_loop), encoding="utf-8")

def contract_digest(constitution: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(constitution.rglob("*")):
        if path.is_file():
            h.update(path.relative_to(constitution).as_posix().encode())
            h.update(b"\\0")
            h.update(path.read_bytes())
            h.update(b"\\0")
    return h.hexdigest()

def write_manifest(subject: Path, arm: str, constitution: Path, out: Path) -> None:
    changed = subprocess.check_output(
        ["git", "-C", str(subject), "status", "--porcelain=v1"], text=True
    ).splitlines()
    paths = sorted(line[3:] for line in changed if len(line) >= 4)
    common_hashes = {
        path: sha256(subject / path) for path in COMMON_FILES
    }
    manifest = {
        "stage": "G8-ORIGIN-R1-P10-P2",
        "arm": arm,
        "base": BASE,
        "contract_digest": contract_digest(constitution),
        "changed_paths": paths,
        "common_file_sha256": common_hashes,
        "treatment_files": [
            "backend/src/services/AlertService.ts",
            "backend/src/routes/alerts.ts",
        ] + (["backend/src/services/ChannelProviderRegistry.ts"] if arm == "INVERT_CHANNEL_ADAPTER" else []),
        "comparative_metrics_opened": False,
    }
    out.mkdir(parents=True, exist_ok=True)
    (out / "materialization-manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True, choices=sorted(ARMS))
    ap.add_argument("--subject", type=Path, required=True)
    ap.add_argument("--constitution", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    verify_base(args.subject)
    patch_common(args.subject)
    if args.arm == "DIRECT_DEDICATED":
        patch_direct(args.subject)
    else:
        patch_invert(args.subject)
    write_manifest(args.subject, args.arm, args.constitution, args.out)
    print("MATERIALIZE_OK")

CHANNEL_PROVIDER_REGISTRY = r"""export type AlertChannelType =
  | 'email'
  | 'slack'
  | 'discord'
  | 'telegram'
  | 'ntfy'
  | 'gotify';

export type ChannelSendMethod =
  | 'sendEmail'
  | 'sendSlack'
  | 'sendDiscord'
  | 'sendTelegram'
  | 'sendNtfy'
  | 'sendGotify';

export interface ChannelProviderDescriptor {
  type: AlertChannelType;
  sensitiveKeys: readonly string[];
  sendMethod: ChannelSendMethod;
  validate(config: Record<string, unknown>): void;
}

function requireString(config: Record<string, unknown>, key: string, label: string): string {
  const value = (config[key] as string | undefined)?.trim() || '';
  if (!value) throw new Error(label + ' missing ' + key);
  return value;
}

function validateHttpUrl(value: string, label: string): void {
  let parsed: URL;
  try {
    parsed = new URL(value);
  } catch {
    throw new Error(label + ' has an invalid URL: ' + value);
  }
  if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
    throw new Error(label + ' URL must be http or https');
  }
}

export const CHANNEL_PROVIDERS: Record<AlertChannelType, ChannelProviderDescriptor> = {
  email: {
    type: 'email',
    sensitiveKeys: ['smtp_pass'],
    sendMethod: 'sendEmail',
    validate(config) {
      requireString(config, 'smtp_host', 'Email channel');
      const recipients = config.recipients as string[] | undefined;
      if (!recipients || recipients.length === 0) throw new Error('Email channel missing recipients');
    },
  },
  slack: {
    type: 'slack',
    sensitiveKeys: [],
    sendMethod: 'sendSlack',
    validate(config) { requireString(config, 'webhook_url', 'Slack channel'); },
  },
  discord: {
    type: 'discord',
    sensitiveKeys: [],
    sendMethod: 'sendDiscord',
    validate(config) { requireString(config, 'webhook_url', 'Discord channel'); },
  },
  telegram: {
    type: 'telegram',
    sensitiveKeys: ['bot_token'],
    sendMethod: 'sendTelegram',
    validate(config) {
      requireString(config, 'bot_token', 'Telegram channel');
      requireString(config, 'chat_id', 'Telegram channel');
    },
  },
  ntfy: {
    type: 'ntfy',
    sensitiveKeys: ['token', 'password'],
    sendMethod: 'sendNtfy',
    validate(config) {
      requireString(config, 'topic', 'ntfy channel');
      const url = ((config.server_url as string | undefined)?.trim() || 'https://ntfy.sh');
      validateHttpUrl(url, 'ntfy channel');
    },
  },
  gotify: {
    type: 'gotify',
    sensitiveKeys: ['app_token'],
    sendMethod: 'sendGotify',
    validate(config) {
      const url = requireString(config, 'server_url', 'Gotify channel');
      requireString(config, 'app_token', 'Gotify channel');
      validateHttpUrl(url, 'Gotify channel');
    },
  },
};

export const SUPPORTED_CHANNEL_TYPES =
  Object.freeze(Object.keys(CHANNEL_PROVIDERS) as AlertChannelType[]);

export function getChannelProvider(type: AlertChannelType): ChannelProviderDescriptor {
  const provider = CHANNEL_PROVIDERS[type];
  if (!provider) throw new Error('Unsupported alert channel type: ' + String(type));
  return provider;
}

export function sensitiveKeysFor(type: string): readonly string[] {
  return (CHANNEL_PROVIDERS as Record<string, ChannelProviderDescriptor | undefined>)[type]?.sensitiveKeys ?? [];
}
"""

GOTIFY_SERVICE_TEST = r"""jest.mock('../../config/database');
jest.mock('nodemailer');

import * as http from 'http';
import { AlertService } from '../AlertService';
import { query } from '../../config/database';

const mockedQuery = jest.mocked(query);

type TestService = {
  sendToChannel(
    ch: { id: number; name: string; type: 'gotify'; enabled: boolean; config: Record<string, unknown> },
    eventType: string,
    message: string,
    ctx: { deviceId?: number; deviceName?: string; details?: string }
  ): Promise<void>;
  postJson(url: string, body: string, headers?: Record<string, string>): Promise<void>;
};

const asTest = (s: AlertService) => s as unknown as TestService;
const channel = (config: Record<string, unknown> = {}) => ({
  id: 77,
  name: 'gotify-test',
  type: 'gotify' as const,
  enabled: true,
  config: { server_url: 'http://127.0.0.1:9999/', app_token: 'app_test', ...config },
});

function capture() {
  const service = new AlertService();
  const calls: { url: string; body: Record<string, unknown>; headers?: Record<string, string> }[] = [];
  asTest(service).postJson = async (url, body, headers) => {
    calls.push({ url, body: JSON.parse(body), headers });
  };
  return { service, calls };
}

describe('Gotify frozen contract', () => {
  beforeEach(() => jest.clearAllMocks());

  it('emits exact endpoint, application-token header, title/message and offline priority', async () => {
    const { service, calls } = capture();
    await asTest(service).sendToChannel(
      channel(),
      'device_offline',
      'sw1 is unreachable',
      { deviceName: 'sw1', details: 'timeout' }
    );
    expect(calls).toHaveLength(1);
    expect(calls[0].url).toBe('http://127.0.0.1:9999/message');
    expect(calls[0].headers).toEqual({ 'X-Gotify-Key': 'app_test' });
    expect(String(calls[0].body.title)).toContain('Device Offline');
    expect(String(calls[0].body.message)).toContain('sw1 is unreachable');
    expect(String(calls[0].body.message)).toContain('Device: sw1');
    expect(String(calls[0].body.message)).toContain('timeout');
    expect(calls[0].body.priority).toBe(4);
  });

  it('uses recovery priority 2 and default priority 3', async () => {
    const { service, calls } = capture();
    await asTest(service).sendToChannel(channel(), 'device_online', 'back', {});
    await asTest(service).sendToChannel(channel(), 'config_drift', 'changed', {});
    expect(calls[0].body.priority).toBe(2);
    expect(calls[1].body.priority).toBe(3);
  });

  it('rejects missing application token and invalid URL', async () => {
    const { service } = capture();
    await expect(asTest(service).sendToChannel(channel({ app_token: '' }), 'device_offline', 'x', {}))
      .rejects.toThrow(/app_token/);
    await expect(asTest(service).sendToChannel(channel({ server_url: 'ftp://invalid' }), 'device_offline', 'x', {}))
      .rejects.toThrow(/http/);
  });

  it('accepts HTTP 2xx and rejects non-2xx through the real shared transport', async () => {
    const service = new AlertService();
    const server = http.createServer((_req, res) => {
      res.statusCode = 204;
      res.end();
    });
    await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve));
    const address = server.address();
    if (!address || typeof address === 'string') throw new Error('no test address');
    await expect(asTest(service).sendToChannel(
      channel({ server_url: 'http://127.0.0.1:' + address.port }),
      'device_online',
      'ok',
      {}
    )).resolves.toBeUndefined();
    await new Promise<void>((resolve, reject) => server.close((e) => e ? reject(e) : resolve()));

    const rejecting = http.createServer((_req, res) => {
      res.statusCode = 401;
      res.end('unauthorized');
    });
    await new Promise<void>((resolve) => rejecting.listen(0, '127.0.0.1', resolve));
    const address2 = rejecting.address();
    if (!address2 || typeof address2 === 'string') throw new Error('no test address');
    await expect(asTest(service).sendToChannel(
      channel({ server_url: 'http://127.0.0.1:' + address2.port }),
      'device_offline',
      'x',
      {}
    )).rejects.toThrow(/HTTP 401/);
    await new Promise<void>((resolve, reject) => rejecting.close((e) => e ? reject(e) : resolve()));
  });

  it('testChannel reaches the same Gotify send path exactly once', async () => {
    mockedQuery.mockResolvedValueOnce([channel()]);
    const { service, calls } = capture();
    await service.testChannel(77);
    expect(calls).toHaveLength(1);
    expect(calls[0].body.priority).toBe(2);
    expect(String(calls[0].body.message)).toContain('This is a test alert');
  });
});
"""

GOTIFY_ROUTE_TEST = r"""jest.mock('../../config/database');
jest.mock('../../middleware/auth', () => ({
  requireAuth: (_req: unknown, _res: unknown, next: () => void) => next(),
  requireWrite: (_req: unknown, _res: unknown, next: () => void) => next(),
}));

import express from 'express';
import request from 'supertest';
import router, { maskConfig, mergeConfig } from '../alerts';
import { query } from '../../config/database';

const mockedQuery = jest.mocked(query);

describe('Gotify channel-management contract', () => {
  beforeEach(() => jest.clearAllMocks());

  it('accepts gotify as a channel type and masks app_token on create response', async () => {
    mockedQuery.mockResolvedValueOnce([{
      id: 7,
      name: 'g',
      type: 'gotify',
      enabled: true,
      config: { server_url: 'https://gotify.example', app_token: 'secret-token' },
    }]);
    const app = express();
    app.use(express.json());
    app.use('/alerts', router);
    const res = await request(app).post('/alerts/channels').send({
      name: 'g',
      type: 'gotify',
      config: { server_url: 'https://gotify.example', app_token: 'secret-token' },
    });
    expect(res.status).toBe(201);
    expect(res.body.type).toBe('gotify');
    expect(res.body.config.app_token).toBe('••••••••');
  });

  it('preserves an existing application token when the mask is submitted', () => {
    const existing = { server_url: 'https://gotify.example', app_token: 'secret-token' };
    const incoming = { server_url: 'https://gotify2.example', app_token: '••••••••' };
    expect(mergeConfig('gotify', existing, incoming)).toEqual({
      server_url: 'https://gotify2.example',
      app_token: 'secret-token',
    });
  });

  it('masks Gotify token without masking non-secret server URL', () => {
    expect(maskConfig('gotify', {
      server_url: 'https://gotify.example',
      app_token: 'secret-token',
    })).toEqual({
      server_url: 'https://gotify.example',
      app_token: '••••••••',
    });
  });
});
"""

if __name__ == "__main__":
    main()
