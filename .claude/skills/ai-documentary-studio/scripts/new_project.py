#!/usr/bin/env python3
"""Create a documentary production workspace from the bundled templates."""
from __future__ import annotations
import argparse, csv, re, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TEMPLATES = HERE / "templates"
DIRS = ["00_brief", "01_research", "02_script", "03_storyboard", "04_media/images", "04_media/videos", "04_media/diagrams", "05_audio/voiceover", "05_audio/music_sfx", "06_subtitles", "07_edit/project_files", "08_exports/thumbnail", "09_reports", "10_youtube"]
FILES = {
    "00_brief/project_brief.yaml": "project_brief.yaml",
    "01_research/research_notes.md": "research_notes.md",
    "01_research/sources.csv": "sources.csv",
    "01_research/claim_register.csv": "claim_register.csv",
    "02_script/master_script.md": "master_script.md",
    "02_script/pronunciation_guide.md": None,
    "02_script/chapter_outline.md": None,
    "02_script/script_fact_map.csv": "script_fact_map.csv",
    "03_storyboard/continuity_bible.md": "continuity_bible.md",
    "03_storyboard/shot_list.md": "shot_list.md",
    "03_storyboard/visual_coverage_report.md": "visual_coverage_report.md",
    "03_storyboard/storyboard.csv": "storyboard.csv",
    "04_media/image_prompts.md": "image_prompts.md",
    "04_media/video_prompts.md": "video_prompts.md",
    "04_media/media_manifest.csv": "media_manifest.csv",
    "05_audio/voiceover_manifest.csv": "voiceover_manifest.csv",
    "05_audio/audio_cue_sheet.csv": "audio_cue_sheet.csv",
    "05_audio/audio_asset_licenses.csv": "asset_rights_register.csv",
    "06_subtitles/subtitle_corrections.csv": "subtitle_corrections.csv",
    "07_edit/edit_decision_list.md": "edit_decision_list.md",
    "07_edit/render_profile.yaml": "render_profile.yaml",
    "09_reports/production_status.md": "production_status.md",
    "09_reports/qc_report.md": "qc_report.md",
    "09_reports/asset_rights_register.csv": "asset_rights_register.csv",
    "09_reports/delivery_manifest.md": "delivery_manifest.md",
    "10_youtube/upload_checklist.md": None,
}

def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    if not value:
        raise ValueError("Project slug must contain at least one ASCII letter or digit.")
    return value[:64].rstrip("-")

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--slug")
    ap.add_argument("--root", default="documentary-projects")
    ap.add_argument("--duration", default="8-10 minutes")
    ap.add_argument("--language", default="Hindi (Devanagari)")
    args = ap.parse_args()
    slug = slugify(args.slug or args.title)
    target = Path(args.root).expanduser().resolve() / slug
    if target.exists() and any(target.iterdir()):
        raise SystemExit(f"Refusing to overwrite non-empty project folder: {target}")
    target.mkdir(parents=True, exist_ok=True)
    for rel in DIRS:
        (target / rel).mkdir(parents=True, exist_ok=True)
    for dest, source in FILES.items():
        out = target / dest
        out.parent.mkdir(parents=True, exist_ok=True)
        if source:
            shutil.copy2(TEMPLATES / source, out)
        elif not out.exists():
            out.write_text("# " + out.stem.replace("_", " ").title() + "\n", encoding="utf-8")
    brief = target / "00_brief/project_brief.yaml"
    text = brief.read_text(encoding="utf-8")
    text = text.replace('title: ""', f'title: "{args.title.replace(chr(34), chr(39))}"', 1)
    text = text.replace('slug: ""', f'slug: "{slug}"', 1)
    text = text.replace('duration_target: "8-10 minutes"', f'duration_target: "{args.duration}"', 1)
    text = text.replace('language: "Hindi"', f'language: "{args.language}"', 1)
    brief.write_text(text, encoding="utf-8")
    print(f"Created project workspace: {target}")
    print("No media was generated. The folder contains planning templates only.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
