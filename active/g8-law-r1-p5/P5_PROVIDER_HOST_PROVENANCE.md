# LAW-R1-P5 provider-host repository repair

## Repository-boundary correction

The P5 provider execution host was mistakenly materialized on `WhoSia/EPISTEME/main` in seven consecutive commits:

- `ac9faf79cab7ec90f669e2773143d2ce9c1be33e`
- `5573a57c3de5955648fdc34186f85d68f24e99eb`
- `a6eee019e7a821bd76750fb9bc51029a8c087db6`
- `96e7532a99296466d802ee7258694b4a33e6b980`
- `d39ed7369f6695a494ac8b1e84d9b988427c653b`
- `13c92b5ac607835e3246b638222ff37492cd3c40`
- `f9f61ad94af5e2543bf4ef1e829eca8d36043ad5`

The entire seven-commit delta consisted only of:

- `.github/workflows/evonomos_p5_host.yml`
- `active/evonomos_p5_trigger.txt`
- `src/evonomos_p5_host.py`

No EPISTEME-owned commit followed those seven commits.

On 2026-09-30, `WhoSia/EPISTEME/main` was therefore restored exactly to its preceding EPISTEME head:

`e2fa965f726baab1b0641961680645508dfe9084`

The host implementation is now owned by EvoNOMOS:

- `tools/law-r1-p5-provider-host.py`
- `.github/workflows/g8-law-r1-p5-provider-host.yml`

The native workflow is **manual-only** because P5 is already scientifically sealed. It exists for reproducibility, not to reopen P5.

Historical EPISTEME-hosted runs `36676553417`, `36677159816`, and `36677191280` remain provenance for the already-sealed P5 result, but the cross-repository placement is classified as a repository-boundary mistake and is not a precedent for future EvoNOMOS execution.

## Prospective rule

EvoNOMOS scientific execution belongs in `WhoSia/EvoNOMOS`.

A different laboratory repository may be used only when the external laboratory itself is the scientific object or when an explicitly declared, non-mutating external service boundary is scientifically necessary. Convenience is not sufficient.
