# Technical & Editorial Quality Control

## Technical checklist
- Correct aspect ratio, dimensions, frame rate, codec, pixel format, and audio streams.
- Runtime near target, with any variance explained.
- No missing/offline assets, black gaps, freeze frames, unintended flashes, or silent sections.
- Voiceover intelligible and consistent; no clipping, abrupt edits, or music masking speech.
- Subtitle language, spelling, timing, readability, and sync correct.
- Maps, labels, numbers, names, dates, and on-screen text accurate.
- No generated reconstruction presented as real archival footage.
- Opening, chapter transitions, ending, and thumbnail align with the actual content.

## Editorial checklist
- Major claims trace to approved sources.
- Counter-evidence and uncertainty are fairly represented.
- No fabricated quotes, scenes, motives, or causal links.
- All rights and disclosure notes are recorded.
- Final cut reviewed by a human before publication.

## Report format
`qc_report.md` must include `PASS`, `FAIL`, or `NOT RUN` per check, timestamped issue, severity, evidence/file path, owner, and fix. Do not mark a check as pass if it was not inspected.
