# Repository Instructions

- The only discoverable entry-point skill in this repository is `.claude/skills/ai-documentary-studio/SKILL.md`.
- Treat `references/` as internal specialist playbooks, not separate skills. Do not create additional `SKILL.md` files inside this skill directory.
- Preserve all production templates and helper scripts unless the user explicitly requests a change.
- Do not claim actual image/video/audio generation or MP4 rendering unless the output files exist and have been inspected.
- Obtain explicit approval before paid provider requests, public uploads, or publishing.
- Never store credentials, `.env`, API keys, or tokens in Git.
- Use the bundled validator when a project workspace is created or updated; interpret warnings accurately.
- Keep generated documentary work under `documentary-projects/<slug>/` by default, not mixed with repository source files.
