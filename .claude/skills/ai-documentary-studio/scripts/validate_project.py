#!/usr/bin/env python3
"""Validate documentary project manifests, paths, and SRT structure (stdlib only)."""
from __future__ import annotations
import argparse, csv, re, sys
from pathlib import Path

REQUIRED_CSV = {
    "01_research/sources.csv": {"source_id", "title", "url", "access_date"},
    "01_research/claim_register.csv": {"claim_id", "claim_text", "status", "source_ids"},
    "03_storyboard/storyboard.csv": {"shot_id", "in_time", "out_time", "duration_seconds", "visual_type"},
    "04_media/media_manifest.csv": {"asset_id", "shot_id", "asset_type", "file_path", "generation_status"},
    "05_audio/voiceover_manifest.csv": {"voice_id", "scene_id", "file_path", "duration_seconds"},
}
STATUSES = {"verified", "supported-debated", "hypothesis", "unknown", "false-misleading"}
TIME = re.compile(r"^(\d{2}):(\d{2}):(\d{2})[,.](\d{3})$")

def parse_time(s: str):
    m = TIME.match(s.strip())
    if not m: return None
    h, mnt, sec, ms = map(int, m.groups())
    if mnt > 59 or sec > 59: return None
    return ((h * 60 + mnt) * 60 + sec) * 1000 + ms

def check_csv(project: Path, rel: str, required: set[str], errors: list[str], warnings: list[str]):
    p = project / rel
    if not p.exists():
        warnings.append(f"Missing optional manifest: {rel}")
        return []
    try:
        with p.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            headers = set(reader.fieldnames or [])
            missing = required - headers
            if missing: errors.append(f"{rel}: missing columns {sorted(missing)}")
            return list(reader)
    except Exception as e:
        errors.append(f"{rel}: cannot parse CSV: {e}")
        return []

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project", type=Path, help="Path to documentary project folder")
    args = ap.parse_args()
    project = args.project.expanduser().resolve()
    errors, warnings = [], []
    if not project.is_dir():
        print(f"ERROR: Not a directory: {project}")
        return 2
    rows = {rel: check_csv(project, rel, cols, errors, warnings) for rel, cols in REQUIRED_CSV.items()}
    claims = rows.get("01_research/claim_register.csv", [])
    for i, row in enumerate(claims, 2):
        status = (row.get("status") or "").strip()
        if status and status not in STATUSES:
            errors.append(f"claim_register.csv row {i}: unknown status {status!r}")
    shot_rows = rows.get("03_storyboard/storyboard.csv", [])
    shot_ids = set()
    for i, row in enumerate(shot_rows, 2):
        sid = (row.get("shot_id") or "").strip()
        if sid and sid in shot_ids: errors.append(f"storyboard.csv row {i}: duplicate shot_id {sid}")
        shot_ids.add(sid)
        try:
            start, end = float(row.get("in_time") or 0), float(row.get("out_time") or 0)
            if end <= start: errors.append(f"storyboard.csv row {i}: out_time must be greater than in_time")
        except ValueError: errors.append(f"storyboard.csv row {i}: invalid in_time/out_time")
    for rel, entries in rows.items():
        for i, row in enumerate(entries, 2):
            raw = (row.get("file_path") or "").strip()
            if raw:
                path = Path(raw)
                if path.is_absolute():
                    warnings.append(f"{rel} row {i}: absolute path is not portable: {raw}")
                elif not (project / path).exists():
                    state = (row.get("generation_status") or row.get("rights_status") or "").lower()
                    if state not in {"not-started", "planned", "pending", "not-created", "blocked", "rejected"}:
                        warnings.append(f"{rel} row {i}: referenced file does not exist yet: {raw}")
    srt = project / "06_subtitles/hindi_subtitles.srt"
    if srt.exists():
        content = srt.read_text(encoding="utf-8-sig", errors="replace").strip()
        blocks = re.split(r"\n\s*\n", content) if content else []
        previous_end = -1
        for idx, block in enumerate(blocks, 1):
            lines = block.splitlines()
            if len(lines) < 3 or not lines[0].strip().isdigit() or "-->" not in lines[1]:
                errors.append(f"SRT block {idx}: malformed block")
                continue
            a, b = [x.strip() for x in lines[1].split("-->", 1)]
            start, end = parse_time(a), parse_time(b)
            if start is None or end is None or end <= start:
                errors.append(f"SRT block {idx}: invalid timestamps")
            elif start < previous_end:
                warnings.append(f"SRT block {idx}: overlapping or non-monotonic cue")
            if end is not None: previous_end = end
    else:
        warnings.append("Subtitles not created yet (06_subtitles/hindi_subtitles.srt).")
    print(f"Project: {project}")
    print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
    for x in errors: print("ERROR:", x)
    for x in warnings: print("WARN :", x)
    if errors: return 1
    print("Validation completed. Warnings require review; this is not an editorial or legal clearance.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
