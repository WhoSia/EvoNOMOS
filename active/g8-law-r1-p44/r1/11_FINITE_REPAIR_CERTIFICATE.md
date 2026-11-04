# Finite repair certificate — three independent feature-removal witnesses

The predeclared P44 adapter grammar has H (HEAD registration), D (URL-path unescaping) and M (405 response semantics). A precise finite certificate consists of three original-source HTTP probes:
- HEAD /items/alpha detects missing H.
- GET /items/a%2Fb detects missing D.
- POST /items/alpha detects missing M.

If any of H,D,M is absent, at least its associated witness must differ from the standard source under this precise implementation grammar. The full H+D+M candidate is separately checked on all twelve probes and passed original-source native CI #41756947113.

Consequently a 3-probe *sufficient distinguishing basis* certifies the unique matching mask within this eight-element family. This is a finite certificate: it does not prove that every alternative adapter scheme needs three independent edits or every valid HTTP request is equivalent.

An independently executable Go test enumerates all eight masks on the three witnesses and evaluates minimum unit cost among masks that match all twelve probes. This new test itself requires a separate successful workflow run; document actual status before promoting the certificate from source argument to execution evidence.
