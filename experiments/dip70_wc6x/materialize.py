from pathlib import Path
import json, subprocess, sys

BASE="9f056cd3e340361947d3bb5e7b63ae2edf47b445"
ISSUE=369
ROOT=Path(sys.argv[1])
ARM=sys.argv[2]
PHASE=sys.argv[3]
assert ARM in {"DIRECT","INVERT"}
assert PHASE in {"phase0","phase1"}

api=ROOT/"indexer/src/api.ts"
text=api.read_text()

if PHASE=="phase0":
    if ARM=="DIRECT":
        text=text.replace('import express, { NextFunction, Request, Response } from "express";','import express, { NextFunction, Request, Response } from "express";\nimport { randomUUID } from "node:crypto";')
        anchor='export function createApp(options: { cachedMigrationHealth?: MigrationHealth | null } = {}) {\n  const app = express();'
        block='''const CORRELATION_HEADER = "x-correlation-id";\nconst CORRELATION_ID_RE = /^[A-Za-z0-9._-]{1,64}$/;\n\nfunction correlationMiddleware(req: Request, res: Response, next: NextFunction) {\n  const raw = req.get(CORRELATION_HEADER)?.trim() ?? "";\n  const correlationId = CORRELATION_ID_RE.test(raw) ? raw : randomUUID();\n  res.setHeader(CORRELATION_HEADER, correlationId);\n  res.locals.correlationId = correlationId;\n  res.on("finish", () => {\n    console.info(JSON.stringify({\n      event: "request.complete",\n      correlationId,\n      method: req.method,\n      path: req.path,\n      status: res.statusCode,\n    }));\n  });\n  next();\n}\n\nexport function createApp(options: { cachedMigrationHealth?: MigrationHealth | null } = {}) {\n  const app = express();\n  app.use(correlationMiddleware);'''
        if anchor not in text: raise SystemExit("DIRECT anchor missing")
        text=text.replace(anchor,block,1)
        api.write_text(text)
    else:
        text=text.replace('import type { MigrationHealth } from "./db/migrate";','import type { MigrationHealth } from "./db/migrate";\nimport { createCorrelationMiddleware } from "./correlation";')
        anchor='export function createApp(options: { cachedMigrationHealth?: MigrationHealth | null } = {}) {\n  const app = express();'
        repl='export function createApp(options: { cachedMigrationHealth?: MigrationHealth | null } = {}) {\n  const app = express();\n  app.use(createCorrelationMiddleware());'
        if anchor not in text: raise SystemExit("INVERT anchor missing")
        text=text.replace(anchor,repl,1)
        api.write_text(text)
        (ROOT/"indexer/src/correlation.ts").write_text('''import { randomUUID } from "node:crypto";\nimport type { NextFunction, Request, Response } from "express";\n\nconst CORRELATION_HEADER = "x-correlation-id";\nconst CORRELATION_ID_RE = /^[A-Za-z0-9._-]{1,64}$/;\n\nexport function createCorrelationMiddleware() {\n  return function correlationMiddleware(req: Request, res: Response, next: NextFunction) {\n    const raw = req.get(CORRELATION_HEADER)?.trim() ?? "";\n    const correlationId = CORRELATION_ID_RE.test(raw) ? raw : randomUUID();\n    res.setHeader(CORRELATION_HEADER, correlationId);\n    res.locals.correlationId = correlationId;\n    res.on("finish", () => {\n      console.info(JSON.stringify({\n        event: "request.complete",\n        correlationId,\n        method: req.method,\n        path: req.path,\n        status: res.statusCode,\n      }));\n    });\n    next();\n  };\n}\n''')

    test=(ROOT/"indexer/src/correlation.contract.test.ts")
    test.write_text('''import { test } from "node:test";\nimport assert from "node:assert/strict";\nimport request from "supertest";\nimport { createApp } from "./api";\n\nconst ID=/^[A-Za-z0-9._-]{1,64}$/;\n\ntest("generated correlation id is exposed on responses", async () => {\n  const res=await request(createApp()).get("/__wc6_missing__");\n  assert.equal(res.status,404);\n  assert.match(res.headers["x-correlation-id"],ID);\n});\n\ntest("valid client correlation id is preserved", async () => {\n  const res=await request(createApp()).get("/__wc6_missing__").set("x-correlation-id","support.case-42");\n  assert.equal(res.headers["x-correlation-id"],"support.case-42");\n});\n\ntest("invalid client correlation id is replaced by bounded safe id", async () => {\n  const res=await request(createApp()).get("/__wc6_missing__").set("x-correlation-id","bad id with spaces and secrets");\n  assert.notEqual(res.headers["x-correlation-id"],"bad id with spaces and secrets");\n  assert.match(res.headers["x-correlation-id"],ID);\n});\n\ntest("error response also exposes correlation id", async () => {\n  const old=process.env.ALLOWED_ORIGINS;\n  process.env.ALLOWED_ORIGINS="https://app.circleup.xyz";\n  try {\n    const res=await request(createApp()).get("/__wc6_missing__").set("Origin","https://evil.example.com");\n    assert.equal(res.status,403);\n    assert.match(res.headers["x-correlation-id"],ID);\n  } finally {\n    if(old===undefined) delete process.env.ALLOWED_ORIGINS; else process.env.ALLOWED_ORIGINS=old;\n  }\n});\n\ntest("structured completion log carries id without query wallet payload", async () => {\n  const lines:string[]=[];\n  const old=console.info;\n  console.info=(...args:unknown[])=>lines.push(args.map(String).join(" "));\n  try {\n    await request(createApp()).get("/__wc6_missing__?wallet=GSECRET_WALLET_PAYLOAD").set("x-correlation-id","support.case-99");\n    await new Promise(resolve=>setImmediate(resolve));\n  } finally { console.info=old; }\n  const line=lines.find(v=>v.includes('"event":"request.complete"')) ?? "";\n  assert.match(line,/support\.case-99/);\n  assert.doesNotMatch(line,/GSECRET_WALLET_PAYLOAD/);\n});\n''')
else:
    # Prospective maintenance perturbation frozen before any arm outcome is read:
    # accept x-request-id as a fallback client alias while preserving x-correlation-id as canonical response header.
    target='const raw = req.get(CORRELATION_HEADER)?.trim() ?? "";'
    repl='const raw = (req.get(CORRELATION_HEADER) ?? req.get("x-request-id"))?.trim() ?? "";'
    if ARM=="DIRECT":
        if target not in text: raise SystemExit("DIRECT phase1 target missing")
        api.write_text(text.replace(target,repl,1))
    else:
        corr=ROOT/"indexer/src/correlation.ts"
        c=corr.read_text()
        if target not in c: raise SystemExit("INVERT phase1 target missing")
        corr.write_text(c.replace(target,repl,1))
    test=ROOT/"indexer/src/correlation.contract.test.ts"
    t=test.read_text()+'''\n\ntest("x-request-id is accepted as fallback alias while response stays canonical", async () => {\n  const res=await request(createApp()).get("/__wc6_missing__").set("x-request-id","support.alias-7");\n  assert.equal(res.headers["x-correlation-id"],"support.alias-7");\n});\n'''
    test.write_text(t)

print(json.dumps({"base":BASE,"issue":ISSUE,"arm":ARM,"phase":PHASE,"status":"MATERIALIZED"}))
