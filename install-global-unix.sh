#!/usr/bin/env bash
set -euo pipefail
FORCE="${1:-}"
SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.claude/skills/ai-documentary-studio"
DEST_PARENT="$HOME/.claude/skills"
DEST="$DEST_PARENT/ai-documentary-studio"
[[ -f "$SOURCE/SKILL.md" ]] || { echo "Skill source not found: $SOURCE" >&2; exit 1; }
mkdir -p "$DEST_PARENT"
if [[ -e "$DEST" ]]; then
  if [[ "$FORCE" != "--force" ]]; then
    echo "Destination already exists: $DEST" >&2
    echo "Review it, then rerun with --force to replace it." >&2
    exit 1
  fi
  rm -rf -- "$DEST"
fi
cp -R "$SOURCE" "$DEST"
echo "Installed ai-documentary-studio to $DEST"
echo "Open a new Claude Code/OpenCode session and invoke /ai-documentary-studio or @ai-documentary-studio."
