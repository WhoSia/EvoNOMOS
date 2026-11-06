# Research OS — latest two previously missing source files, 2026-11-05

**Both previously missing TITLES were found in 00_INTAKE.** Distinguish "bytes present" from "readable verified canonical text"; never repeat both as completely absent.

1. White et al. 2014 original research article, [Drive original](https://drive.google.com/file/d/1n4vr5-CR7P-_HHBzpkmHmoNzFqzmghDp/view). Verified actual journal metadata, readable source text and full original filename identity. Renamed to `White, Galindo, Saxena, Dougherty, Benavides & Schmidt (2014) — Evolving Feature Model Configurations in Software Product Lines — JSS 87 119-136.pdf` and moved from 00_INTAKE into 10_PAPERS. Final target parent and filename verified by separate metadata read. Status: OWNED/READABLE/CANONICAL. Do not put in missing table.

2. Borodin & El-Yaniv 1998 book candidate, [Drive upload](https://drive.google.com/file/d/11AdbiQ9bvF0bi-74k8sLRVP09Sqpw7Ax/view), 21,483,785 bytes; title inferred from uploaded file name, no trustworthy page extracted. Raw PDF streamed from authenticated Drive into local runtime for inspection. `pdfinfo` sees 217 PDF pages but `pdftotext` emits empty data and `Bad FCHECK` / illegal character errors; PyMuPDF reports failed zlib stream decompression for sampled pages, and page 1 rendered blank. Thus NOT successfully read and not adequate canonical book. Renamed in place to `BORODIN & EL-YANIV (1998) — Online Computation and Competitive Analysis — PDF STREAM CORRUPTION — INTAKE HOLD.pdf`, remains 00_INTAKE until a readable source is available. Final title, source parent and unchanged 21,483,785 size read back. Status: BYTES PRESENT / SUSPECTED CORRUPTION / CONTENT UNVERIFIED / REPLACEMENT NEEDED.

Research progress: original White §3.1 6-tuple, §3.3 edge constraints, §2.5 model drift, §6.4 validity limitations read; Borodin contents NOT studied from damaged PDF. Avoid confusing bibliographic familiarity with original-text inspection.

Current open literature need: a verified readable edition of Borodin & El-Yaniv 1998 (target 11_BOOKS) and an exact theorem/proof/algorithm audit of White 2014 plus its 2009 predecessor. Do not invent additional missing titles without fresh search.

## 2026-11-05 further non-destructive recoverability check

The original 21.5-MB PDF was kept unchanged on Drive and checked in a temporary local copy. Ghostscript 10.05.1 pdfwrite conversion technically returned exit status 0, but produced only a 56-KB output and many Page drawing error warnings; its first four extracted pages had no text. Therefore the converter exit code is NOT evidence of successfully repairing the book. The generated local candidate was NOT uploaded to Drive or treated as canonical. No page-by-page book content study or reliable edition check is possible from the existing damaged PDF. **Maintain intact original under 00_INTAKE HOLD until a readable, provenance-verified edition exists.**
