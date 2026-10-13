#!/usr/bin/env python3
"""Validate data/facts.json and write data/facts.js (what the page loads).

facts.json is the single source of truth. Run this after every change to it:
    python3 build/build.py
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABS = {"results", "plant", "materials", "timeline", "terms"}
STATUS = {"confirmed", "pending", "conflict", "retired"}


def main():
    data = json.load(open(os.path.join(ROOT, "data/facts.json"), encoding="utf-8"))
    log_path = os.path.join(ROOT, "data/changelog.json")
    log = json.load(open(log_path, encoding="utf-8")) if os.path.exists(log_path) else []
    errs, seen = [], set()
    for f in data["facts"]:
        i = f.get("id", "?")
        if i in seen:
            errs.append(f"{i}: duplicate id")
        seen.add(i)
        if f.get("tab") not in TABS:
            errs.append(f"{i}: bad tab {f.get('tab')!r}")
        if f.get("status") not in STATUS:
            errs.append(f"{i}: bad status {f.get('status')!r}")
        for k in ("title", "statement"):
            v = f.get(k) or {}
            if not (isinstance(v, dict) and v.get("zh") and v.get("en")):
                errs.append(f"{i}: {k} needs zh and en")
        for im in f.get("images") or []:
            if not os.path.exists(os.path.join(ROOT, im["src"])):
                errs.append(f"{i}: missing image {im['src']}")
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    out = {"meta": data["meta"], "facts": data["facts"], "changelog": log}
    with open(os.path.join(ROOT, "data/facts.js"), "w", encoding="utf-8") as fh:
        fh.write("window.FC = " + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
    n = {}
    for f in data["facts"]:
        n[f["status"]] = n.get(f["status"], 0) + 1
    print(f"ok: {len(data['facts'])} facts, version {data['meta']['version']}, {n}")


if __name__ == "__main__":
    main()
