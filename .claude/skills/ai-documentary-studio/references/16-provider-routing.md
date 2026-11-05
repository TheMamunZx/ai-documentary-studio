# Provider & API Router Integration

## Capability matrix
For each image/video/TTS/STT/LLM provider actually configured, record: provider, model ID, endpoint/base URL, auth source variable name (never its value), input/output schema, accepted formats, max duration/resolution, async job lifecycle, polling endpoint, retry/error behavior, rate limits, quota/cost, retention/privacy, and usage/license terms.

## How to inspect
Read the user's existing router config and official provider documentation. Never assume a route based on a model name or a previous project. Avoid exposing API keys or dumping environment variables. Redact tokens from errors and logs.

## Test before production
Use a non-billable or explicitly approved minimum test request. Verify result URL/file, dimensions/duration, and actual download. Use idempotency keys or persisted job IDs where available. For ambiguous timeout, query the existing job before retrying to prevent duplicate charges.

## Provider selection
Compare only configured and authorized services. If no video-generation route is available, report that limitation and produce the shot prompts or an edit/animation fallback. Do not claim image generation is equivalent to video generation.
