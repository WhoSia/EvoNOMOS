#!/usr/bin/env python3
"""Apply the frozen P10-P3 Pushover follow-up to one exact P10-P2 arm.

This script is arm-aware but outcome-blind. It performs no comparative
measurement and prints no change-volume information.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

ARMS={"DIRECT_DEDICATED","INVERT_CHANNEL_ADAPTER"}

def replace_once(path:Path, old:str, new:str)->None:
    text=path.read_text(encoding="utf-8")
    n=text.count(old)
    if n!=1:
        raise RuntimeError(f"{path}: expected one anchor, found {n}: {old[:100]!r}")
    path.write_text(text.replace(old,new,1),encoding="utf-8")

def insert_before_once(path:Path, anchor:str, payload:str)->None:
    replace_once(path,anchor,payload+anchor)

def patch_common(subject:Path)->None:
    api=subject/"frontend/src/services/api.ts"
    settings=subject/"frontend/src/pages/SettingsPage.tsx"
    migrate=subject/"backend/src/db/migrate.ts"
    service=subject/"backend/src/services/AlertService.ts"

    replace_once(
        api,
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy' | 'gotify';",
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy' | 'gotify' | 'pushover';",
    )
    replace_once(
        settings,
        "(['slack', 'discord', 'telegram', 'ntfy', 'gotify', 'email'] as const)",
        "(['slack', 'discord', 'telegram', 'ntfy', 'gotify', 'pushover', 'email'] as const)",
    )
    pushover_ui="""              ) : chForm.type === 'pushover' ? (
                <>
                  <div>
                    <label className="block text-xs font-medium text-gray-600 dark:text-slate-400 mb-1">API Token</label>
                    <input type="password" className="input w-full font-mono text-xs" value={cfgStr('api_token')} onChange={(e) => setCfg('api_token', e.target.value)} placeholder="application token" />
                  </div>
                  <div>
                    <label className="block text-xs font-medium text-gray-600 dark:text-slate-400 mb-1">User Key</label>
                    <input type="password" className="input w-full font-mono text-xs" value={cfgStr('user_key')} onChange={(e) => setCfg('user_key', e.target.value)} placeholder="user/group key" />
                  </div>
                </>
"""
    replace_once(
        settings,
        "              ) : chForm.type === 'gotify' ? (\n",
        pushover_ui+"              ) : chForm.type === 'gotify' ? (\n",
    )

    old="CHECK (type IN ('email','slack','discord','telegram','ntfy','gotify'))"
    new="CHECK (type IN ('email','slack','discord','telegram','ntfy','gotify','pushover'))"
    text=migrate.read_text(encoding="utf-8")
    if text.count(old)!=2:
        raise RuntimeError("migrate.ts: expected two P2 CHECK anchors")
    migrate.write_text(text.replace(old,new),encoding="utf-8")

    sender=r"""  private pushoverPriority(eventType: string): number {
    if (['device_offline', 'log_error', 'high_cpu', 'high_memory'].includes(eventType)) return 1;
    if (['device_online', 'device_discovered'].includes(eventType)) return -1;
    return 0;
  }

  private assertPushoverResponse(statusCode: number, body: string): void {
    if (statusCode < 200 || statusCode >= 300) {
      throw new Error('Pushover HTTP ' + statusCode + ': ' + body.slice(0, 200));
    }
    let parsed: { status?: number };
    try {
      parsed = JSON.parse(body) as { status?: number };
    } catch {
      throw new Error('Pushover returned invalid JSON');
    }
    if (parsed.status !== 1) {
      throw new Error('Pushover rejected message: ' + body.slice(0, 200));
    }
  }

  private postPushoverJson(url: string, body: string): Promise<void> {
    return new Promise((resolve, reject) => {
      const parsed = new URL(url);
      const req = https.request({
        hostname: parsed.hostname,
        port: parsed.port || 443,
        path: parsed.pathname + parsed.search,
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(body),
        },
      }, (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
          try {
            this.assertPushoverResponse(res.statusCode || 0, data);
            resolve();
          } catch (err) {
            reject(err);
          }
        });
      });
      req.on('error', reject);
      req.write(body);
      req.end();
    });
  }

  private async sendPushover(
    cfg: Record<string, unknown>,
    eventType: string,
    message: string,
    ctx: AlertContext
  ): Promise<void> {
    const apiToken = (cfg.api_token as string | undefined)?.trim() || '';
    const userKey = (cfg.user_key as string | undefined)?.trim() || '';
    if (!apiToken) throw new Error('Pushover channel missing api_token');
    if (!userKey) throw new Error('Pushover channel missing user_key');

    const label = EVENT_LABELS[eventType] ?? eventType;
    const emoji = EVENT_EMOJI[eventType] ?? '🔔';
    const lines = [message];
    if (ctx.deviceName) lines.push('Device: ' + ctx.deviceName);
    if (ctx.details) lines.push(ctx.details);

    const body = JSON.stringify({
      token: apiToken,
      user: userKey,
      title: emoji + ' ' + label,
      message: lines.join('\n'),
      priority: this.pushoverPriority(eventType),
    });
    await this.postPushoverJson('https://api.pushover.net/1/messages.json', body);
  }

"""
    insert_before_once(service,"  private gotifyPriority(eventType: string): number {\n",sender)

    service_test=subject/"backend/src/services/__tests__/Pushover.contract.test.ts"
    service_test.write_text(PUSHOVER_SERVICE_TEST,encoding="utf-8")
    route_test=subject/"backend/src/routes/__tests__/alerts-pushover.contract.test.ts"
    route_test.parent.mkdir(parents=True,exist_ok=True)
    route_test.write_text(PUSHOVER_ROUTE_TEST,encoding="utf-8")

def patch_direct(subject:Path)->None:
    service=subject/"backend/src/services/AlertService.ts"
    routes=subject/"backend/src/routes/alerts.ts"
    replace_once(
        service,
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy' | 'gotify';",
        "type: 'email' | 'slack' | 'discord' | 'telegram' | 'ntfy' | 'gotify' | 'pushover';",
    )
    replace_once(
        service,
        "      case 'gotify':   await this.sendGotify(ch.config, eventType, message, ctx); break;\n",
        "      case 'gotify':   await this.sendGotify(ch.config, eventType, message, ctx); break;\n"
        "      case 'pushover': await this.sendPushover(ch.config, eventType, message, ctx); break;\n",
    )
    replace_once(
        routes,
        "const validTypes = ['email', 'slack', 'discord', 'telegram', 'ntfy', 'gotify'];",
        "const validTypes = ['email', 'slack', 'discord', 'telegram', 'ntfy', 'gotify', 'pushover'];",
    )
    replace_once(
        routes,
        "  gotify:   ['app_token'],\n",
        "  gotify:   ['app_token'],\n  pushover: ['api_token', 'user_key'],\n",
    )

def patch_invert(subject:Path)->None:
    registry=subject/"backend/src/services/ChannelProviderRegistry.ts"
    replace_once(registry,"  | 'gotify';","  | 'gotify'\n  | 'pushover';")
    replace_once(registry,"  | 'sendGotify';","  | 'sendGotify'\n  | 'sendPushover';")
    gotify=r"""  gotify: {
    type: 'gotify',
    sensitiveKeys: ['app_token'],
    sendMethod: 'sendGotify',
    validate(config) {
      const url = requireString(config, 'server_url', 'Gotify channel');
      requireString(config, 'app_token', 'Gotify channel');
      validateHttpUrl(url, 'Gotify channel');
    },
  },
"""
    pushover=gotify+r"""  pushover: {
    type: 'pushover',
    sensitiveKeys: ['api_token', 'user_key'],
    sendMethod: 'sendPushover',
    validate(config) {
      requireString(config, 'api_token', 'Pushover channel');
      requireString(config, 'user_key', 'Pushover channel');
    },
  },
"""
    replace_once(registry,gotify,pushover)

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--arm",required=True,choices=sorted(ARMS))
    ap.add_argument("--subject",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args()
    patch_common(args.subject)
    if args.arm=="DIRECT_DEDICATED":
        patch_direct(args.subject)
    else:
        patch_invert(args.subject)
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/"followup-manifest.json").write_text(json.dumps({
        "stage":"EvoNOMOS Generation VIII ORIGIN-R1-P10-P3",
        "arm":args.arm,
        "followup":"PUSHOVER_PROTOCOL_REAL_SYNTHETIC_FOLLOWUP_v1",
        "comparative_values_opened":False,
        "authority":"EXPLORATORY_ONLY",
    },indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("PUSHOVER_FOLLOWUP_MATERIALIZED=PASS")

PUSHOVER_SERVICE_TEST=r"""jest.mock('../../config/database');
jest.mock('nodemailer');

import { AlertService } from '../AlertService';

type TestService = {
  sendToChannel(
    ch: { id: number; name: string; type: 'pushover'; enabled: boolean; config: Record<string, unknown> },
    eventType: string,
    message: string,
    ctx: { deviceName?: string; details?: string }
  ): Promise<void>;
  postPushoverJson(url: string, body: string): Promise<void>;
  assertPushoverResponse(statusCode: number, body: string): void;
};
const asTest=(s:AlertService)=>s as unknown as TestService;
const channel=(config:Record<string,unknown>={})=>({
  id:88,name:'pushover-test',type:'pushover' as const,enabled:true,
  config:{api_token:'app_test',user_key:'user_test',...config},
});
function capture(){
  const service=new AlertService();
  const calls:{url:string;body:Record<string,unknown>}[]=[];
  asTest(service).postPushoverJson=async (url,body)=>{calls.push({url,body:JSON.parse(body)});};
  return {service,calls};
}

describe('Pushover frozen exploratory follow-up',()=>{
  it('emits fixed endpoint, credentials, message and offline priority',async()=>{
    const {service,calls}=capture();
    await asTest(service).sendToChannel(channel(),'device_offline','sw1 down',{deviceName:'sw1',details:'timeout'});
    expect(calls).toHaveLength(1);
    expect(calls[0].url).toBe('https://api.pushover.net/1/messages.json');
    expect(calls[0].body.token).toBe('app_test');
    expect(calls[0].body.user).toBe('user_test');
    expect(calls[0].body.priority).toBe(1);
    expect(String(calls[0].body.message)).toContain('Device: sw1');
  });
  it('maps recovery to -1 and default to 0',async()=>{
    const {service,calls}=capture();
    await asTest(service).sendToChannel(channel(),'device_online','back',{});
    await asTest(service).sendToChannel(channel(),'config_drift','changed',{});
    expect(calls[0].body.priority).toBe(-1);
    expect(calls[1].body.priority).toBe(0);
  });
  it('rejects missing credentials',async()=>{
    const {service}=capture();
    await expect(asTest(service).sendToChannel(channel({api_token:''}),'device_offline','x',{})).rejects.toThrow(/api_token/);
    await expect(asTest(service).sendToChannel(channel({user_key:''}),'device_offline','x',{})).rejects.toThrow(/user_key/);
  });
  it('accepts status=1 and rejects protocol or HTTP failure',()=>{
    const service=new AlertService();
    expect(()=>asTest(service).assertPushoverResponse(200,'{"status":1}')).not.toThrow();
    expect(()=>asTest(service).assertPushoverResponse(200,'{"status":0}')).toThrow(/rejected/);
    expect(()=>asTest(service).assertPushoverResponse(401,'{"status":0}')).toThrow(/HTTP 401/);
  });
});
"""

PUSHOVER_ROUTE_TEST=r"""jest.mock('../../config/database');
jest.mock('../../middleware/auth',()=>({
  requireAuth:(_req:unknown,_res:unknown,next:()=>void)=>next(),
  requireWrite:(_req:unknown,_res:unknown,next:()=>void)=>next(),
}));
import { maskConfig, mergeConfig } from '../alerts';

describe('Pushover secret-policy contract',()=>{
  it('masks both credentials',()=>{
    expect(maskConfig('pushover',{api_token:'a',user_key:'u'}))
      .toEqual({api_token:'••••••••',user_key:'••••••••'});
  });
  it('preserves both masked credentials on update',()=>{
    expect(mergeConfig(
      'pushover',
      {api_token:'secret-a',user_key:'secret-u'},
      {api_token:'••••••••',user_key:'••••••••'}
    )).toEqual({api_token:'secret-a',user_key:'secret-u'});
  });
});
"""

if __name__=="__main__":
    main()
