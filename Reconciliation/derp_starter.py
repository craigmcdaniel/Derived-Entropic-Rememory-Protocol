#!/usr/bin/env python3
"""DERP public starter: read a ChatGPT ZIP and produce a private Obsidian index.

Only conversation metadata is rendered. No transcripts or attachments are published.
Standard library only. A minimal starting point, not the full DERP v0.3 converter.
"""
import argparse
import csv
import hashlib
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path


def iso(value):
    if value is None:
        return ""
    try:
        return datetime.fromtimestamp(float(value), timezone.utc).isoformat()
    except (ValueError, TypeError, OverflowError):
        return ""


def date(value):
    stamp = iso(value)
    return stamp[:10] if stamp else "undated"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Untouched ChatGPT export ZIP")
    parser.add_argument("output", type=Path, help="NEW private output directory")
    parser.add_argument("--cutoff", default="2025-10-01T00:00:00-04:00")
    args = parser.parse_args()

    if not args.archive.is_file():
        parser.error("Archive not found")
    if args.output.exists():
        parser.error("Output already exists; choose a new directory (no overwrite)")
    cutoff = datetime.fromisoformat(args.cutoff).timestamp()
    if args.archive.resolve() == args.output.resolve():
        parser.error("Output cannot be the source archive")

    rows = []
    seen = set()
    totals = {"examined": 0, "included": 0, "excluded": 0, "nodes": 0}
    digest = hashlib.sha256()
    with args.archive.open("rb") as input_file:
        for chunk in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(chunk)

    with zipfile.ZipFile(args.archive) as archive:
        filenames = sorted(
            n for n in archive.namelist()
            if re.fullmatch(r"conversations-\d+\.json", n)
        )
        if not filenames:
            parser.error("No conversations-000.json style files in archive")

        for filename in filenames:
            with archive.open(filename) as stream:
                conversations = json.load(stream)
            for conversation in conversations:
                totals["examined"] += 1
                created = float(conversation.get("create_time") or 0)
                updated = float(conversation.get("update_time") or 0)
                if max(created, updated) < cutoff:
                    totals["excluded"] += 1
                    continue
                cid = str(conversation.get("id") or "")
                if not re.fullmatch(r"[a-zA-Z0-9_-]+", cid):
                    continue
                if cid in seen:
                    continue
                seen.add(cid)
                mapping = conversation.get("mapping") or {}
                totals["included"] += 1
                totals["nodes"] += len(mapping)
                rows.append({
                    "conversation_id": cid,
                    "title": str(conversation.get("title") or "(untitled)"),
                    "created_utc": iso(conversation.get("create_time")),
                    "updated_utc": iso(conversation.get("update_time")),
                    "node_count": len(mapping),
                    "current_node": str(conversation.get("current_node") or ""),
                    "source_file": filename,
                })

    rows.sort(key=lambda r: r["updated_utc"], reverse=True)
    args.output.mkdir(parents=True)
    csv_path = args.output / "conversation-index.csv"
    with csv_path.open("x", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else [
            "conversation_id", "title", "created_utc", "updated_utc",
            "node_count", "current_node", "source_file"
        ])
        writer.writeheader()
        writer.writerows(rows)

    markdown = [
        "# Private ChatGPT conversation index",
        "",
        "**These records are historical source metadata, not verified facts.**",
        "",
        f"Source archive: `{args.archive.name}`",
        "",
        f"Source SHA-256: `{digest.hexdigest()}`",
        "",
        f"Cutoff: `{args.cutoff}`",
        "",
        f"Included conversations: **{len(rows)}**",
        "",
        "## Conversations",
        "",
    ]
    for row in rows:
        title = row["title"].replace("\n", " ").replace("\r", " ")
        markdown.append(
            f"- **{row['updated_utc'][:10]}** — {title} "
            f"(`{row['conversation_id']}`, {row['node_count']} nodes)"
        )
    (args.output / "INDEX.md").write_text(
        "\n".join(markdown) + "\n", encoding="utf-8"
    )
    manifest = {
        "generator": "derp-public-starter-0.1",
        "source_filename": args.archive.name,
        "source_sha256": digest.hexdigest(),
        "cutoff": args.cutoff,
        "counts": totals,
        "limitations": [
            "Indexes metadata only; does not render dialogue or alternate branches",
            "Does not extract or reconcile factual claims",
            "No attachments are materialized"
        ],
    }
    (args.output / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(totals, indent=2))
    print(f"Private index: {args.output / 'INDEX.md'}")


if __name__ == "__main__":
    main()
