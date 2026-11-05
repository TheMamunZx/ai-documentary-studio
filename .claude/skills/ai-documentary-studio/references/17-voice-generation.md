# AI Voice Generation & Speech Pipeline

## Scope
Generate narration audio from approved text; this module does not choose the editorial direction (voiceover direction) or design the soundscape (audio design).

## Preflight
Verify configured TTS provider, model/voice ID, supported Hindi/Devanagari pronunciation, SSML/phoneme support, sample rate, output codecs, voice consistency controls, segment limits, usage terms, commercial publication rules, and cost/quota.

## Workflow
1. Split approved narration into logical chunks within provider limits.
2. Normalize text carefully without altering claims; add provider-supported pronunciation hints only where necessary.
3. Generate one short approved sample and listen for accent, pronunciation, prosody, and voice quality.
4. Get explicit cost approval before paid batch generation.
5. Generate chunked audio, track job IDs, and retry only after checking prior job state.
6. Join with appropriate pauses/crossfades; inspect word boundaries and segment transitions.
7. Measure actual duration and update storyboard/edit timing.
8. Use STT or forced alignment to draft word/phrase timestamps, then review captions.

## Voice identity and consent
Use a stock/authorized synthetic voice or a real narrator. Do not clone a real person's voice without documented authorization. Do not claim a generated voice is a particular real person.

## Deliverables
Per-scene WAV/MP3 files, voice manifest, pronunciation exceptions, usage record, and audio QA report.
