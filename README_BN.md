# AI Documentary Studio — বাংলা নির্দেশিকা

**একটি Skill নির্বাচন, একটি Prompt, সম্পূর্ণ Documentary Workflow।**

এই Repository-তে আলাদা আলাদা ১৮টি Skill নির্বাচন করতে হবে না। Claude Code বা OpenCode-এ শুধু `ai-documentary-studio` চালু করলে Master Skill কাজের প্রয়োজন অনুযায়ী নিজের `references/` ফোল্ডারের বিশেষজ্ঞ নির্দেশনা পড়বে। এগুলো আলাদা discoverable Skills নয়; একটি Skill-এর অভ্যন্তরীণ playbook।

## কীভাবে চালাবে

Claude Code:

```text
/ai-documentary-studio
Create an 8–10 minute Hindi documentary about [TOPIC].
Research, fact-check, write the script, storyboard, generate visuals and voice,
edit, render, and quality-check the complete video.
```

OpenCode:

```text
@ai-documentary-studio
Create an 8–10 minute Hindi documentary about [TOPIC].
Research, fact-check, write the script, storyboard, generate visuals and voice,
edit, render, and quality-check the complete video.
```

## Install

সম্পূর্ণ এই ফোল্ডারটি target project-এর `.claude/skills/`-এ রাখবে:

```text
.claude/skills/ai-documentary-studio/
```

`SKILL.md`, `references/`, `scripts/`, `templates/`, `assets/`—সব একসঙ্গে রাখতে হবে। OpenCode Claude-compatible `.claude/skills/` path-ও discover করে।

## কী কী করে

1. Research ও source collection
2. Claim register ও fact-check
3. Hindi/অনুরোধকৃত ভাষায় script
4. Scene-by-scene storyboard
5. Image/video prompt ও continuity
6. Configured provider দিয়ে media generation
7. Voiceover, music ও sound design
8. Final audio থেকে subtitle
9. Editing timeline ও rendering
10. Technical/editorial QC, rights register ও YouTube package

## গুরুত্বপূর্ণ সীমাবদ্ধতা

এই Skill নিজে AI model, API credit, video-generation service, TTS, বা FFmpeg install করে না। তোমার computer ও configured tools-এ এগুলো থাকতে হবে। না থাকলে Skill prompt pack ও blocker report তৈরি করবে; generated file হয়েছে বলে মিথ্যা দাবি করবে না। Paid generation, public upload বা YouTube publishing-এর আগে অনুমতি লাগবে। API key কখনো README, Git, বা chat-এ রাখবে না।

## Helper scripts

Project scaffold:

```bash
python .claude/skills/ai-documentary-studio/scripts/new_project.py --title "Documentary Topic"
```

Project validate:

```bash
python .claude/skills/ai-documentary-studio/scripts/validate_project.py documentary-projects/documentary-topic
```

Validation কেবল folder/CSV/SRT structure পরীক্ষা করে; factual truth, copyright clearance বা video quality নিশ্চিত করে না।
