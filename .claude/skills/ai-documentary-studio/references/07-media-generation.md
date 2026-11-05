# Image & Video Media Generation

## Preflight
Before generation, confirm available provider/tool, current model identifier, endpoint, authentication source (environment variable name only), allowed input/output formats, max duration/resolution, aspect ratio, reference support, asynchronous job/poll method, error codes, rate limits, quota, cost, content/usage terms, and data retention conditions.

## Execution
1. Prepare shot-level prompt batches from the approved storyboard.
2. Check user-supplied reference assets and their usage rights.
3. Generate one representative sample per visual style/provider if possible.
4. Review output for factual plausibility, visual errors, continuity, framing, and prompt adherence.
5. Obtain approval for paid generation with provider/model, quantity, estimated cost or unknown-cost warning, and cap.
6. Persist job IDs, request IDs, idempotency keys, prompt hash, and status. Poll asynchronous jobs according to provider documentation. Do not repeat a chargeable request because the UI timed out without checking the prior job.
7. Download only from approved provider results; verify file type, dimensions, duration, and corruption.
8. Store assets with stable shot-based names and update the manifest immediately.

## Fallback
If no actual media-generation tool/provider is configured, produce provider-neutral prompts and a `generation_blockers.md` report. Do not create dummy image/video files or label prompts as generated media.
