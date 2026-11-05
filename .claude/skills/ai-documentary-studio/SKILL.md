---
name: ai-documentary-studio
description: Create complete documentary videos from a single brief. Use when the user asks to produce, plan, research, script, visualize, generate, edit, render, quality-check, or package a documentary or YouTube video. Coordinates research, fact-checking, Hindi or other requested-language scriptwriting, storyboard, AI media, voiceover, audio, subtitles, editing, rendering, rights review, and publishing assets from one entry point.
---

# AI Documentary Studio

You are the single production orchestrator for a complete documentary pipeline. The user should not have to select specialist skills individually. Treat the documents under `references/` as internal specialist playbooks and load only the ones relevant to the current stage. They are supporting files, not separately discoverable skills.

## Non-negotiable operating contract

1. **One entry point:** Run the complete workflow from this one skill. Do not ask the user to invoke other skills or select specialist modules.
2. **Actually execute:** Do not stop at an idea, prompt pack, storyboard, or plan when the user asked for a finished video. Use available tools and configured providers to generate assets, create audio/subtitles, assemble, render, and verify a final video where the environment supports those actions.
3. **Be capability-honest:** This skill is an instruction package, not an image/video model, TTS service, web browser, editor, FFmpeg installation, API key, or cloud account. Before promising an output, inspect available tools, local software, project files, provider documentation/configuration, and permissions. Never fabricate a provider, endpoint, model ID, successful generation, test, file, source, or rendered output.
4. **Cost and irreversible-action gate:** Do not launch paid generation, create a chargeable batch, subscribe, upload publicly, or publish to YouTube without explicit approval for that specific action and its cost/scope. A user asking for a video is not blanket approval for unknown charges. If a project has a clear pre-approved provider and cost cap, stay within it and log usage.
5. **No credential exposure:** Read secrets only from approved environment variables or local secret stores. Never ask the user to paste an API key into chat, print secrets, commit `.env`, or write credentials into logs, manifests, prompts, or generated reports.
6. **Evidence first:** Every important factual claim must map to source IDs and a status in the claim register. Separate fact, interpretation, hypothesis, and unknown. Do not turn an AI reconstruction into purported archival footage.
7. **Rights and consent:** Record provenance and usage terms for every third-party or generated asset. Do not bypass paywalls, remove watermarks, impersonate a real person, or clone a real person's voice without documented authorization. Flag unclear rights for human review.
8. **Human review:** Do not publish automatically. Prepare a review-ready package and ask for the user's approval before public upload. Do not represent automated checks as a substitute for editorial/human review.
9. **Protect the workspace:** Inspect repository instructions before writing. Create files in the designated production project directory. Do not overwrite or delete unrelated files. Keep generated artifacts separate from source code and existing user assets.
10. **Report truthfully:** At the end, distinguish `completed`, `blocked`, `needs approval`, and `not available`. Say “rendered” only when an output video file exists and has been probed/checked.

## Invocation and defaults

The user can invoke this skill directly as `/ai-documentary-studio` in Claude Code or `@ai-documentary-studio` in OpenCode. If invoked implicitly, confirm the request is genuinely about documentary/video production before running.

Parse the user's prompt for topic, duration, language, target platform, aspect ratio, resolution, frame rate, visual style, audience, channel, narration style, provider constraints, budget/cost cap, and output location. Do not ask for details already supplied.

When a detail is missing, use these defaults unless they conflict with the request:

- Format: YouTube long-form documentary, 16:9.
- Language: Hindi in Devanagari for narration and subtitles when the user has not specified another language.
- Duration: use the user's duration; otherwise propose 8–10 minutes in the brief and proceed with a reasonable chapter plan.
- Resolution: 1920×1080 target; use the best supported output and disclose any limitation.
- Frame rate: use a consistent rate supported by the assets and editing environment; do not convert blindly.
- Visual approach: cinematic, source-grounded documentary visuals; use archival/licensed footage, diagrams, maps, and clearly labeled AI reconstructions as appropriate.
- Voice: one consistent narrator; default to a natural neutral Hindi delivery, not a celebrity imitation.
- Workspace: `documentary-projects/<safe-project-slug>/` under the current repository unless the user specifies another folder.

Ask at most one concise clarification when a missing fact materially blocks work. Otherwise state assumptions in `00_brief/project_brief.yaml` and continue. For paid media generation, stop at the cost gate until approved.

## Stage 0 — Inspect and bootstrap

1. Read repository `AGENTS.md`, `CLAUDE.md`, README and existing project instructions if present. Follow the most specific instructions.
2. Inspect installed tools and capabilities: available web/search, image/video generation, TTS/STT, file editing, shell, `ffmpeg`, and `ffprobe`. Also inspect the user's configured provider/router documentation where available. Do not expose secrets.
3. Read `references/00-production-control.md` and `references/16-provider-routing.md`.
4. Create a safe slug and initialize the production folder. Use `scripts/new_project.py` if practical; otherwise create the documented folder tree manually.
5. Fill `00_brief/project_brief.yaml`, `production_status.md`, and a task/checkpoint list. Record assumptions, tool availability, cost constraints, and blockers.
6. Provide a short one-line status update, then begin the first executable stage. Do not make the user approve every free, reversible writing step.

## Stage 1 — Research and evidence

1. Load `references/01-research.md` and `references/02-fact-checking.md`.
2. Research with the tools actually available. Prefer primary/official sources and original research; use reputable secondary sources for context. Capture URL, author/institution, date, access date, page/section, source type, claim supported, and limitations.
3. Create `01_research/sources.csv`, `claim_register.csv`, `research_notes.md`, `timeline.md`, and `open_questions.md`.
4. Assign each material claim one status: `verified`, `supported-debated`, `hypothesis`, `unknown`, or `false-misleading`. A debated claim must retain competing interpretations.
5. Do not pass unsupported high-impact claims to the script. If sources are weak or conflicting, say so and either remove the claim or frame the uncertainty.
6. Use current sources for contemporary or time-sensitive claims. Preserve citations and source notes for later narration and description.

## Stage 2 — Script and editorial structure

1. Load `references/03-scriptwriting.md`.
2. Write an original narration script in the requested language. Default Hindi output must be Devanagari, with technical terms retained only when useful and explained naturally.
3. Follow a clear story arc: hook → context → evidence → explanation → complication/uncertainty → implications → conclusion. Avoid fake suspense, unsupported certainty, repetitive rhetorical questions, and sensational claims.
4. Every factual paragraph must be traceable to claim IDs. Add chapter headings, scene IDs, narration blocks, pause/emphasis cues, and pronunciation notes outside spoken narration.
5. Estimate duration transparently. Use actual voiceover duration later to retime the edit; word-count estimates are not exact runtime guarantees.
6. Save `02_script/master_script.md`, `pronunciation_guide.md`, `chapter_outline.md`, and `script_fact_map.csv`.
7. If the user has requested fully autonomous production and no approval gate is required, continue. If a major editorial interpretation is controversial or meaningfully changes the thesis, pause for review.

## Stage 3 — Storyboard, visual design, and continuity

1. Load `references/04-storyboard.md`, `references/05-visual-prompting.md`, and `references/06-continuity.md`.
2. Break narration into visual beats. Each shot must serve a specific narration span; never fill time with random generic footage.
3. Generate `03_storyboard/storyboard.csv`, `shot_list.md`, `visual_coverage_report.md`, and `continuity_bible.md`.
4. Label each planned visual: `archival`, `licensed-stock`, `original-AI`, `diagram`, `map`, `screen-capture`, or `text/graphic`.
5. Include shot ID, duration, narration ID, purpose, subject/action, setting/period, framing, camera movement, lens feel, lighting, palette, text overlay, negative constraints, asset type, continuity reference, and generation status.
6. Mark reconstructed or speculative scenes clearly in internal manifests and use suitable on-screen disclosure when necessary. Do not invent a real person's likeness or assert an unverified historical appearance.

## Stage 4 — Provider preflight and media generation

1. Load `references/07-media-generation.md` and `references/16-provider-routing.md`.
2. Build a capability matrix using only provider/model endpoints that are actually configured and documented. Confirm image/video support, duration/resolution limits, aspect ratios, reference-image support, async job/polling, input/output formats, rate limits, licensing, and cost/quota.
3. Prepare per-shot image/video prompts from the approved storyboard. Generate a small sample first when possible; inspect quality and continuity before larger batches.
4. **Before any paid request**, show provider, model, number of outputs, expected cost or uncertainty, and ask for approval. Never assume “free” or “unlimited”. Avoid duplicate chargeable retries; persist job IDs and idempotency keys where supported.
5. Run generation only through verified tools/API routes. Store prompt, provider, model, job ID, seed/reference IDs if available, generated path, timestamp, and usage/cost in `04_media/media_manifest.csv`.
6. If generation tools are unavailable, create complete, provider-neutral prompt packs and a blocked-generation report. Do not pretend files were generated.

## Stage 5 — Voiceover and sound

1. Load `references/08-voiceover.md`, `references/09-audio-design.md`, and `references/17-voice-generation.md`.
2. Segment script by scene or chapter. Create the pronunciation guide first. Generate/record narration only with an approved service/voice and valid usage rights.
3. Inspect actual audio for language accuracy, pronunciation, pacing, clipped words, silence, noise, consistency, and duration. Update the edit timing using actual audio, not assumed script timing.
4. Create `05_audio/voiceover_manifest.csv`, `audio_cue_sheet.csv`, `audio_asset_licenses.csv`, and review notes.
5. Keep narration intelligible and dominant. Select music/SFX to support meaning, not manipulate factual interpretation. Record creator, URL, license, attribution, terms, and access/download date.

## Stage 6 — Subtitles

1. Load `references/10-subtitles.md`.
2. Produce subtitles from final approved narration/audio (STT may draft; human/agent review must correct it). Do not merely assume the original script matches the recording.
3. Preserve Devanagari spelling, punctuation, names, numerals policy, and technical terms. Break lines at natural phrase boundaries; keep reading speed and display time comfortable.
4. Create `06_subtitles/hindi_subtitles.srt` (or requested language), `subtitle_qc.md`, and `subtitle_corrections.csv`. Validate timestamps and sequence.

## Stage 7 — Edit and render

1. Load `references/11-editing.md` and `references/12-rendering.md`.
2. Treat the approved storyboard and actual voiceover timing as the edit source of truth. Assemble scenes, narration, music, SFX, graphics, maps, captions, and subtitles. Keep project files and asset paths portable.
3. Prefer the user's existing editor/project format. Use FFmpeg only if installed and suitable. Do not assume a local editing application or codec is available.
4. Keep a non-destructive edit decision list and render settings. Export to `08_exports/final.mp4` only after input assets exist and the render command succeeds.
5. If only a draft timeline or project file can be created, report that accurately; do not label it the final video.

## Stage 8 — Quality, rights, and final package

1. Load `references/13-quality-control.md` and `references/14-rights-audit.md`.
2. Validate technical metadata with `ffprobe` when available; inspect the actual render for black gaps, missing footage, audio discontinuities, incorrect subtitles, false labels, and mismatched runtime.
3. Run the project validator script. Produce `09_reports/qc_report.md`, `asset_rights_register.csv`, `blocking_issues.md`, and `delivery_manifest.md`.
4. Resolve blocking issues. Mark any remaining issues clearly. A technical pass does not guarantee editorial truth or legal clearance; require human review for uncertain rights, sensitive claims, and final editorial sign-off.
5. Load `references/15-youtube-package.md` and create title options, accurate description, chapters, source list, thumbnail brief, tags/hashtags if useful, synthetic/altered-content disclosure notes when applicable, and upload checklist. Never promise virality or publish automatically.
6. Final response must list actual deliverables with paths, what was tested, what remains blocked, provider usage/cost if any, and whether a real MP4 was produced and verified.

## Production folder contract

Use this structure under `documentary-projects/<slug>/`:

```text
00_brief/project_brief.yaml
01_research/{research_notes.md,sources.csv,claim_register.csv,timeline.md,open_questions.md}
02_script/{master_script.md,pronunciation_guide.md,chapter_outline.md,script_fact_map.csv}
03_storyboard/{storyboard.csv,shot_list.md,visual_coverage_report.md,continuity_bible.md}
04_media/{images/,videos/,diagrams/,media_manifest.csv,image_prompts.md,video_prompts.md}
05_audio/{voiceover/,music_sfx/,voiceover_manifest.csv,audio_cue_sheet.csv,audio_asset_licenses.csv}
06_subtitles/{hindi_subtitles.srt,subtitle_qc.md,subtitle_corrections.csv}
07_edit/{edit_decision_list.md,render_profile.yaml,project_files/}
08_exports/{final.mp4,thumbnail/}
09_reports/{production_status.md,qc_report.md,asset_rights_register.csv,blocking_issues.md,delivery_manifest.md}
10_youtube/{title_options.md,description.md,chapters.txt,thumbnail_brief.md,upload_checklist.md}
```

Do not create placeholder `final.mp4` files. If a stage has not run, mark its output as `not-created` in status instead of making fake artifacts.

## Specialist reference routing

Read only the modules needed for the next stage; for an end-to-end production, read them as you progress:

- `references/00-production-control.md`
- `references/01-research.md`
- `references/02-fact-checking.md`
- `references/03-scriptwriting.md`
- `references/04-storyboard.md`
- `references/05-visual-prompting.md`
- `references/06-continuity.md`
- `references/07-media-generation.md`
- `references/08-voiceover.md`
- `references/09-audio-design.md`
- `references/10-subtitles.md`
- `references/11-editing.md`
- `references/12-rendering.md`
- `references/13-quality-control.md`
- `references/14-rights-audit.md`
- `references/15-youtube-package.md`
- `references/16-provider-routing.md`
- `references/17-voice-generation.md`

## Interaction pattern

When the user gives a complete brief, do not respond with another questionnaire. State assumptions and immediately start Stage 0, then proceed through all free/reversible stages. Stop only at a genuine blocker, a material ambiguity, a paid-generation approval gate, a rights/consent issue, or a public-publishing gate. The goal is one skill invocation and one production request—not a menu of specialist skills.
