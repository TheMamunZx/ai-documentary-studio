param([switch]$Force)
$ErrorActionPreference = 'Stop'
$source = Join-Path $PSScriptRoot '.claude\skills\ai-documentary-studio'
$parent = Join-Path $HOME '.claude\skills'
$destination = Join-Path $parent 'ai-documentary-studio'
if (-not (Test-Path (Join-Path $source 'SKILL.md'))) { throw "Skill source not found: $source" }
New-Item -ItemType Directory -Force -Path $parent | Out-Null
if (Test-Path $destination) {
  if (-not $Force) { throw "Destination already exists: $destination. Review it, then rerun with -Force to replace it." }
  Remove-Item -LiteralPath $destination -Recurse -Force
}
Copy-Item -LiteralPath $source -Destination $destination -Recurse
Write-Host "Installed ai-documentary-studio to $destination"
Write-Host "Open a new Claude Code/OpenCode session and invoke /ai-documentary-studio or @ai-documentary-studio."
