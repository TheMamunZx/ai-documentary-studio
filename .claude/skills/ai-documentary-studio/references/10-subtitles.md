# Subtitle & Caption Production

## Source of truth
Create captions from the final approved voice recording or a verified transcript of it—not from the first script draft alone. Use STT as a draft only; review manually or with a second-pass language check.

## Hindi/Devanagari guidelines
Preserve spelling, punctuation, names, technical terms, and the project's number style. Break lines at natural phrase boundaries. Avoid dense lines and flashes too short to read. Keep captions synchronized to spoken words, not just scene boundaries.

## SRT QA
Ensure sequential cue numbers, `HH:MM:SS,mmm --> HH:MM:SS,mmm` timestamps, positive cue duration, monotonic order, no unintended overlaps, and no out-of-range cues beyond the final video. Check punctuation, spelling, speaker labels, and forced captions separately.

## Deliverables
Language-specific `.srt`, transcript source, `subtitle_qc.md`, and corrections list. If the final audio changes, regenerate/re-time captions.
