# Visual Prompt Engineering

## Prompt schema
For each storyboard shot, create: purpose, source/visual type, subject, action, environment and period, composition, shot size, camera angle, camera movement, lens/optical feel, lighting, color palette, material detail, motion constraints, aspect ratio, duration (video only), continuity references, negative constraints, and evidence caveat.

## Accuracy rules
- Start from the claim and shot purpose, not from an impressive image idea.
- Distinguish a documentary reconstruction from an actual archival photograph/film.
- Do not invent exact clothing, architecture, tools, flags, labels, signage, or technical details when sources do not establish them.
- Do not ask an image/video model to render legible titles or subtitles; add typography in editing unless the task specifically requires model-generated text.
- Avoid fake logos, fake citations, fake maps, impossible hand movements, sudden object changes, identity drift, and unrelated action.
- Video prompts should describe one primary action and one coherent camera move. Avoid multi-event action sequences in a single short generation.
- For factual diagrams, generate/author a clean diagram from verified data rather than a photorealistic image that implies evidence.

## Prompt outputs
Store prompt IDs and exact prompts in `image_prompts.md` and `video_prompts.md`; link each to storyboard `shot_id`, provider/model, reference assets, and generation settings in `media_manifest.csv`.
