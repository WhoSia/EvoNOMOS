#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

SUBJECT_REPO = "https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture.git"
BASE = "cdfcddb12f6248d881fd6789c905bae30058ecdd"
PROD = ["scripts/dekc_common.py", "scripts/dekc_grade.py", "scripts/dekc_business.py", "scripts/dekc_pack.py"]


def run(cmd, cwd=None, check=True):
    p = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if check and p.returncode != 0:
        raise RuntimeError(f"command failed {cmd}:\n{p.stdout}")
    return p


def replace_once(path: Path, old: str, new: str):
    s = path.read_text()
    if s.count(old) != 1:
        raise RuntimeError(f"expected one replacement in {path}: {s.count(old)}")
    path.write_text(s.replace(old, new, 1))


def commit(root: Path, msg: str):
    run(["git", "add", "-A"], root)
    run(["git", "-c", "user.name=EvoNOMOS", "-c", "user.email=evonomos@example.invalid", "commit", "-m", msg], root)
    return run(["git", "rev-parse", "HEAD"], root).stdout.strip()


def stats(root: Path, a: str, b: str):
    p = run(["git", "diff", "--numstat", a, b, "--", *PROD], root)
    files = 0
    churn = 0
    rows = []
    for line in p.stdout.splitlines():
        if not line.strip():
            continue
        add, dele, path = line.split("\t", 2)
        if add == "-" or dele == "-":
            raise RuntimeError("binary production diff")
        files += 1
        churn += int(add) + int(dele)
        rows.append([path, int(add), int(dele)])
    return files, churn, rows


def phase0_direct(root: Path):
    p = root / "scripts/dekc_grade.py"
    replace_once(
        p,
        '        blob = (fm.get("description") or "") + "\\n" + (body or "")\n',
        '        desc = fm.get("description")\n        if not isinstance(desc, str):\n            desc = ""\n        blob = desc + "\\n" + (body or "")\n',
    )


def phase0_invert(root: Path):
    common = root / "scripts/dekc_common.py"
    marker = '\ndef utc_now() -> str:\n'
    helper = '\ndef description_text(value: Any) -> str:\n    """Return a frontmatter description only when it is already text."""\n    return value if isinstance(value, str) else ""\n\n\ndef utc_now() -> str:\n'
    replace_once(common, marker, helper)
    grade = root / "scripts/dekc_grade.py"
    replace_once(grade, '    append_log,\n', '    append_log,\n    description_text,\n')
    replace_once(
        grade,
        '        blob = (fm.get("description") or "") + "\\n" + (body or "")\n',
        '        blob = description_text(fm.get("description")) + "\\n" + (body or "")\n',
    )


def phase1_direct(root: Path):
    business = root / "scripts/dekc_business.py"
    replace_once(
        business,
        '    desc = (fm.get("description") or "").strip()\n',
        '    desc_value = fm.get("description")\n    desc = desc_value.strip() if isinstance(desc_value, str) else ""\n',
    )
    pack = root / "scripts/dekc_pack.py"
    replace_once(
        pack,
        '                "description": fm.get("description") or "",\n',
        '                "description": fm.get("description") if isinstance(fm.get("description"), str) else "",\n',
    )


def phase1_invert(root: Path):
    business = root / "scripts/dekc_business.py"
    replace_once(
        business,
        'from dekc_common import list_concepts, parse_frontmatter, resolve_knowledge_root, slugify  # noqa: E402\n',
        'from dekc_common import description_text, list_concepts, parse_frontmatter, resolve_knowledge_root, slugify  # noqa: E402\n',
    )
    replace_once(
        business,
        '    desc = (fm.get("description") or "").strip()\n',
        '    desc = description_text(fm.get("description")).strip()\n',
    )
    pack = root / "scripts/dekc_pack.py"
    replace_once(pack, '    append_log,\n', '    append_log,\n    description_text,\n')
    replace_once(
        pack,
        '                "description": fm.get("description") or "",\n',
        '                "description": description_text(fm.get("description")),\n',
    )


def oracle(root: Path):
    scripts = root / "scripts"
    code = f'''\nimport sys\nfrom pathlib import Path\nsys.path.insert(0, {str(scripts)!r})\nimport dekc_grade as g\nimport dekc_business as b\nimport dekc_pack as p\n\n# phase-0 grade oracle: patch collaborators so only description boundary is exercised.\ng.list_concepts=lambda bundle:[(bundle/'tables/x.md', {{'type':'Table','description':{{'nested':True}},'layer':'gold'}}, 'body text long enough for evidence')]\ng.build_graph=lambda bundle:{{}}\ng.doctor=lambda bundle:{{'validation_ok':True,'orphan_technical':[]}}\nr=g.grade_bundle(Path('/tmp/bundle'))\nassert isinstance(r, dict)\n\n# Strings preserve byte semantics in the transformed boundary.\ng.list_concepts=lambda bundle:[(bundle/'tables/x.md', {{'type':'Table','description':'alpha','layer':'gold'}}, 'beta')]\nr2=g.grade_bundle(Path('/tmp/bundle'))\nassert isinstance(r2, dict)\n\n# phase-1 business reader: non-text falls back to body, text remains unchanged.\nassert b.infer_definition('X', {{'description':{{'nested':True}},'layer':'gold'}}, 'Fallback prose') == 'Fallback prose'\nassert b.infer_definition('X', {{'description':'Exact text','layer':'gold'}}, 'Fallback prose') == 'Exact text'\n\n# phase-1 pack reader: non-text becomes absent; ordinary strings are preserved.\norig_list=p.list_concepts\norig_graph=p.build_graph\np.list_concepts=lambda bundle:[(bundle/'tables/x.md', {{'type':'Table','title':'X','description':{{'nested':True}}}}, 'body')]\np.build_graph=lambda bundle:{{}}\nr3=p.pack(Path('/tmp/bundle'),'tables/x.md',hops=0,max_nodes=1)\nassert r3['nodes'][0]['description']==''\np.list_concepts=lambda bundle:[(bundle/'tables/x.md', {{'type':'Table','title':'X','description':'Exact text'}}, 'body')]\nr4=p.pack(Path('/tmp/bundle'),'tables/x.md',hops=0,max_nodes=1)\nassert r4['nodes'][0]['description']=='Exact text'\nprint('ORACLE_PASS')\n'''
    p = run(["python3", "-c", code], root, check=False)
    return p.returncode == 0, p.stdout


def execute_arm(base_clone: Path, work: Path, arm: str):
    shutil.copytree(base_clone, work)
    base_sha = run(["git", "rev-parse", "HEAD"], work).stdout.strip()
    if base_sha != BASE:
        raise RuntimeError(f"base mismatch {base_sha}")
    if arm == "DIRECT":
        phase0_direct(work)
    else:
        phase0_invert(work)
    run(["python3", "-m", "py_compile", *PROD], work)
    p0 = commit(work, f"{arm} phase0")
    f0, c0, rows0 = stats(work, BASE, p0)
    if arm == "DIRECT":
        phase1_direct(work)
    else:
        phase1_invert(work)
    run(["python3", "-m", "py_compile", *PROD], work)
    p1 = commit(work, f"{arm} phase1")
    f1, c1, rows1 = stats(work, p0, p1)
    ok, out = oracle(work)
    return {"V":[f0,c0,f1,c1,1 if ok else 0],"phase0":rows0,"phase1":rows1,"oracle":out[-4000:]}


def pareto(dv, iv):
    # lower F/C is better, P1 higher is better
    if dv[4] != iv[4]:
        return "PARETO_DIRECT" if dv[4] > iv[4] else "PARETO_INVERT"
    direct_no_worse = all(dv[i] <= iv[i] for i in range(4)) and any(dv[i] < iv[i] for i in range(4))
    invert_no_worse = all(iv[i] <= dv[i] for i in range(4)) and any(iv[i] < dv[i] for i in range(4))
    if direct_no_worse: return "PARETO_DIRECT"
    if invert_no_worse: return "PARETO_INVERT"
    if dv[:4] == iv[:4]: return "TIE"
    return "TRADEOFF"


def main():
    out_path = Path(__file__).with_name("RESULT_SEAL.json")
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        base = td / "base"
        run(["git", "clone", "--quiet", SUBJECT_REPO, str(base)])
        run(["git", "checkout", "--quiet", BASE], base)
        direct = execute_arm(base, td/"direct", "DIRECT")
        invert = execute_arm(base, td/"invert", "INVERT")
    dv, iv = direct["V"], invert["V"]
    result = {
        "stage":"DIP-71-F2-X",
        "subject":"SpillwaveSolutions/data-engineering-knowledge-capture#27",
        "base":BASE,
        "direct":direct,
        "invert":invert,
        "delta_invert_minus_direct":[iv[i]-dv[i] for i in range(5)],
        "geometry":pareto(dv,iv),
        "historical_patch_used":False,
    }
    out_path.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__ == "__main__":
    main()
