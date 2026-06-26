#!/usr/bin/env python3
"""
AIsa Docs Mirror
================

Pulls AIsa's **entire** developer-doc surface to a local mirror, so you can
read, grep, diff, and feed it to other tools even when you can't reach the
site directly.

WHY IT EXISTS
-------------
`llms.txt` is only the index. This tool resolves that index into the real
content: every page is fetched via its `.md` twin (the lossless,
render-free machine version of the human page), plus all the per-service
OpenAPI specs. Output is a faithful directory tree mirroring the URL paths,
plus a manifest recording the SHA-256 and fetch time of every file so you
can detect exactly what changed between two pulls.

SOURCES (all public, no API key)
  - https://aisa.one/docs/llms.txt          -> master index of doc pages + specs
  - https://aisa.one/docs/<path>.md         -> clean markdown for each page
  - https://aisa.one/docs/openapi/<x>.json  -> per-service OpenAPI specs

USAGE
  python docs_mirror.py                 # full pull into ./docs-mirror
  python docs_mirror.py --out DIR       # choose output dir
  python docs_mirror.py --incremental   # only refetch pages whose bytes changed
  python docs_mirror.py --diff          # print what changed vs the last manifest
  python docs_mirror.py --jobs 8        # parallel fetch (default 8)

NOTE ON HUMAN PAGES
  The human HTML pages (e.g. /docs/guides/getting-started-with-aisa) are a
  Next.js app: the readable text is buried in serialized RSC payloads and
  needs a JS render to extract cleanly. The `.md` twin of every page carries
  the same content in clean form, so this tool mirrors the `.md` set. Pass
  --keep-html to additionally save the raw HTML shell for archival.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as _dt
import hashlib
import json
import os
import re
import sys
import urllib.request
import urllib.error

BASE = "https://aisa.one"
LLMS_TXT = BASE + "/docs/llms.txt"
UA = "aisa-docs-mirror/1.0 (+https://github.com/yuanshan8053/aisa-docs-voyager)"
TIMEOUT = 30

MD_RE = re.compile(r"https://aisa\.one/docs/[^\s)]+\.md")
SPEC_RE = re.compile(r"https://aisa\.one/docs/openapi/[^\s)]+\.json")


def fetch(url: str) -> tuple[int, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.getcode(), r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception:
        return 0, b""


def discover() -> dict[str, list[str]]:
    """Return {'pages': [...md urls...], 'specs': [...json urls...]} from llms.txt."""
    code, body = fetch(LLMS_TXT)
    if code != 200:
        raise SystemExit(f"Cannot read llms.txt (HTTP {code}). Aborting.")
    text = body.decode("utf-8", "replace")
    pages = sorted(set(MD_RE.findall(text)))
    specs = sorted(set(SPEC_RE.findall(text)))
    return {"pages": pages, "specs": specs}


def url_to_relpath(url: str) -> str:
    """https://aisa.one/docs/guides/x.md -> guides/x.md"""
    return url.split("/docs/", 1)[1]


def load_manifest(path: str) -> dict:
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {"files": {}}


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def pull_one(url: str, out_dir: str, prev: dict, incremental: bool) -> dict:
    rel = url_to_relpath(url)
    dest = os.path.join(out_dir, rel)
    code, body = fetch(url)
    if code != 200 or not body:
        return {"url": url, "rel": rel, "status": code, "result": "ERROR"}
    digest = sha256(body)
    prev_entry = prev.get("files", {}).get(rel)
    if incremental and prev_entry and prev_entry.get("sha256") == digest \
            and os.path.isfile(dest):
        return {"url": url, "rel": rel, "status": code, "sha256": digest,
                "bytes": len(body), "result": "UNCHANGED"}
    changed = bool(prev_entry) and prev_entry.get("sha256") != digest
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(body)
    return {"url": url, "rel": rel, "status": code, "sha256": digest,
            "bytes": len(body), "result": "CHANGED" if changed else "NEW"}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Mirror the full AIsa doc surface locally.")
    ap.add_argument("--out", default="docs-mirror", help="output directory")
    ap.add_argument("--incremental", action="store_true",
                    help="skip files whose bytes are unchanged since last manifest")
    ap.add_argument("--diff", action="store_true",
                    help="after pulling, print what changed vs the previous manifest")
    ap.add_argument("--jobs", type=int, default=8, help="parallel fetch workers")
    ap.add_argument("--keep-html", action="store_true",
                    help="also archive the raw HTML shell of each human page")
    args = ap.parse_args(argv)

    out_dir = os.path.abspath(args.out)
    os.makedirs(out_dir, exist_ok=True)
    manifest_path = os.path.join(out_dir, "manifest.json")
    prev = load_manifest(manifest_path)

    print(f"[1/3] Discovering doc surface from {LLMS_TXT} ...")
    surface = discover()
    urls = surface["pages"] + surface["specs"]
    print(f"      {len(surface['pages'])} pages + {len(surface['specs'])} "
          f"OpenAPI specs = {len(urls)} files")

    print(f"[2/3] Fetching with {args.jobs} workers"
          f"{' (incremental)' if args.incremental else ''} ...")
    results: list[dict] = []
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = [ex.submit(pull_one, u, out_dir, prev, args.incremental) for u in urls]
        for i, fut in enumerate(cf.as_completed(futs), 1):
            results.append(fut.result())
            if i % 50 == 0 or i == len(urls):
                print(f"      {i}/{len(urls)}")

    if args.keep_html:
        print("      archiving raw HTML shells ...")
        for u in surface["pages"]:
            html_url = u[:-3]  # strip .md
            code, body = fetch(html_url)
            if code == 200 and body:
                dest = os.path.join(out_dir, "_html", url_to_relpath(u)[:-3] + ".html")
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as f:
                    f.write(body)

    # build manifest
    files = {}
    tally = {"NEW": 0, "CHANGED": 0, "UNCHANGED": 0, "ERROR": 0}
    errors = []
    for r in results:
        tally[r["result"]] = tally.get(r["result"], 0) + 1
        if r["result"] == "ERROR":
            errors.append(r)
            continue
        files[r["rel"]] = {"sha256": r["sha256"], "bytes": r["bytes"],
                           "url": r["url"], "status": r["status"]}
    manifest = {
        "tool": "aisa-docs-mirror",
        "version": "1.0",
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "source_index": LLMS_TXT,
        "counts": {"pages": len(surface["pages"]),
                   "specs": len(surface["specs"]),
                   **tally},
        "files": files,
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"[3/3] Done. NEW={tally['NEW']} CHANGED={tally['CHANGED']} "
          f"UNCHANGED={tally['UNCHANGED']} ERROR={tally['ERROR']}")
    print(f"      Mirror: {out_dir}")
    print(f"      Manifest: {manifest_path}")
    if errors:
        print(f"      {len(errors)} fetch error(s):")
        for e in errors[:10]:
            print(f"        - {e['status']}  {e['url']}")

    if args.diff:
        prev_files = prev.get("files", {})
        added = sorted(set(files) - set(prev_files))
        removed = sorted(set(prev_files) - set(files))
        changed = sorted(rel for rel in files
                         if rel in prev_files
                         and files[rel]["sha256"] != prev_files[rel]["sha256"])
        print("\n=== DIFF vs previous manifest ===")
        print(f"added:   {len(added)}")
        for r in added[:20]:
            print(f"  + {r}")
        print(f"removed: {len(removed)}")
        for r in removed[:20]:
            print(f"  - {r}")
        print(f"changed: {len(changed)}")
        for r in changed[:20]:
            print(f"  ~ {r}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
