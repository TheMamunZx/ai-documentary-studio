#!/usr/bin/env python3
"""Validate the single-entry AI Documentary Studio library (stdlib only)."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.claude' / 'skills' / 'ai-documentary-studio'
errors=[]; warnings=[]
required = [BASE/'SKILL.md', BASE/'references'/'INDEX.md', BASE/'scripts'/'new_project.py', BASE/'scripts'/'validate_project.py', ROOT/'README.md', ROOT/'README_BN.md', ROOT/'AGENTS.md']
for p in required:
    if not p.is_file(): errors.append(f'Missing required file: {p.relative_to(ROOT)}')
skill = BASE/'SKILL.md'
if skill.exists():
    text=skill.read_text(encoding='utf-8')
    if not text.startswith('---\n') or text.count('---') < 2: errors.append('SKILL.md YAML frontmatter missing or malformed')
    for token in ['name: ai-documentary-studio','description:','## Non-negotiable operating contract','## Stage 0','## Specialist reference routing']:
        if token not in text: errors.append(f'SKILL.md missing required section/token: {token}')
    links=re.findall(r'`(references/[^`]+\.md)`', text)
    for rel in sorted(set(links)):
        if not (BASE/rel).is_file(): errors.append(f'Broken skill reference: {rel}')
ref_files=list((BASE/'references').glob('*.md'))
if len(ref_files) != 19: errors.append(f'Expected 19 reference markdown files including INDEX.md; found {len(ref_files)}')
# Ensure exactly one discoverable skill directory
skill_files=list((ROOT/'.claude'/'skills').rglob('SKILL.md'))
if len(skill_files)!=1: errors.append(f'Expected exactly one discoverable SKILL.md, found {len(skill_files)}')
# Readme local relative links
readme=(ROOT/'README.md').read_text(encoding='utf-8')
for link in re.findall(r'\]\(([^)]+)\)', readme):
    if link.startswith(('http://','https://','#','mailto:')): continue
    target=(ROOT/link.split('#',1)[0]).resolve()
    if not target.exists(): errors.append(f'Broken README path: {link}')
# scripts syntax check
for p in [BASE/'scripts'/'new_project.py', BASE/'scripts'/'validate_project.py', ROOT/'scripts'/'validate_library.py']:
    if p.exists():
        import py_compile
        try: py_compile.compile(str(p), doraise=True)
        except Exception as e: errors.append(f'Python compile error in {p.relative_to(ROOT)}: {e}')
print(f'Root: {ROOT}')
print(f'Discoverable skills: {len(skill_files)}')
print(f'Reference markdown files: {len(ref_files)}')
print(f'Errors: {len(errors)} | Warnings: {len(warnings)}')
for x in errors: print('ERROR:', x)
for x in warnings: print('WARN:', x)
if errors: sys.exit(1)
print('Library structure validation passed. This does not test external providers or actual media rendering.')
