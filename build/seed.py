#!/usr/bin/env python3
"""One-time: merge data/_seed/*.json (agent extractions) into data/facts.json.

After the first seed, facts.json is edited directly and this script is not run again.
"""
import glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABS = {"results", "plant", "materials", "timeline", "terms"}
STATUS = {"confirmed", "pending", "conflict", "retired"}
ORDER = ["manual", "wiki-wetlab", "wiki-hardware", "wiki-model", "wiki-hp", "plant-agar", "plant-soil-hydro"]


def bi(v):
    if isinstance(v, dict):
        zh, en = (v.get("zh") or "").strip(), (v.get("en") or "").strip()
        return {"zh": zh or en, "en": en or zh}
    v = (v or "").strip() if isinstance(v, str) else ""
    return {"zh": v, "en": v}


def main(version):
    facts, seen, dropped = [], set(), 0
    files = sorted(glob.glob(os.path.join(ROOT, "data/_seed/*.json")),
                   key=lambda p: ORDER.index(os.path.basename(p)[:-5]) if os.path.basename(p)[:-5] in ORDER else 99)
    for path in files:
        for f in json.load(open(path, encoding="utf-8")):
            if f.get("id") in seen or f.get("tab") not in TABS:
                dropped += 1
                continue
            seen.add(f["id"])
            imgs = [{"src": im["src"], "caption": bi(im.get("caption"))} for im in f.get("images") or []
                    if os.path.exists(os.path.join(ROOT, im.get("src", "")))]
            facts.append({
                "id": f["id"], "tab": f["tab"], "group": bi(f.get("group")),
                "title": bi(f.get("title")), "statement": bi(f.get("statement")),
                "value": str(f.get("value") or ""), "unit": str(f.get("unit") or ""), "date": str(f.get("date") or ""),
                "status": f.get("status") if f.get("status") in STATUS else "pending",
                "status_note": bi(f.get("status_note")), "ask": str(f.get("ask") or ""),
                "source": f.get("source") or [], "wiki": f.get("wiki") or [], "images": imgs,
                "critical": bool(f.get("critical")),
                "confirmed_by": f.get("confirmed_by", ""), "confirmed_on": f.get("confirmed_on", ""),
            })
    meta = {"version": version, "freeze": "2026-10-21T23:00:00+08:00",
            "wikiBase": "https://timmy97-tw.github.io/releaf-wiki/"}
    with open(os.path.join(ROOT, "data/facts.json"), "w", encoding="utf-8") as fh:
        json.dump({"meta": meta, "facts": facts}, fh, ensure_ascii=False, indent=1)
    print(f"seeded {len(facts)} facts from {len(files)} files, dropped {dropped}")


if __name__ == "__main__":
    main(sys.argv[1])
