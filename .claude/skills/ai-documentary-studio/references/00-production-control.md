# Production Control & Orchestration

## Role
Coordinate all stages as one studio workflow. This is not a separate agent skill: it is the operating protocol for the single `ai-documentary-studio` entry point.

## Intake schema
Capture: `project_title`, `topic`, `thesis_or_question`, `duration_target`, `language`, `audience`, `platform`, `aspect_ratio`, `resolution`, `frame_rate`, `visual_style`, `narrator_style`, `provider_constraints`, `budget_cap`, `output_dir`, `deadline`, `user_assets`, and `approval_notes`.

If duration or language is absent, use the main skill's defaults. Ask only when the missing item blocks production or changes cost, safety, rights, or the editorial thesis.

## Stage state model
Use one status per stage: `not-started`, `in-progress`, `needs-review`, `blocked`, `approved`, `completed`, `skipped-with-reason`. Record: stage, owner/tool, input paths, output paths, timestamp, blocker, approval reference, and next action.

## Dependency graph
Brief → Research → Fact-check → Script → Storyboard → Visual/media preflight → Media generation → Voice/audio → Subtitles → Edit/render → QC/rights → YouTube package.

Parallelize only independent tasks (for example, music research can happen while image prompts are drafted). Do not generate final assets against an unapproved script/storyboard if it would create rework or cost.

## Decision gates
- Free, reversible research and drafting: proceed.
- Editorial thesis materially uncertain: request review.
- Paid generation or non-refundable service usage: explicit approval and amount/cap required.
- Real-person likeness/voice: authorization required.
- Rights unclear: block that asset or find an eligible replacement.
- Public upload or account action: user approval required.

## Status reporting
Send brief progress updates after each major stage. Avoid long silent periods. The final report must separate finished artifacts from planned or blocked work.
