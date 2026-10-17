---
name: linkedin-style-writer
description: Draft high-signal, practitioner-first LinkedIn posts with zero AI slop, automatic Markdown-to-Unicode conversion, U+2800 line-break protection, and programmatic developer cheat sheet graphics.
---

# LinkedIn Style Writer

When writing a technical post for LinkedIn, you must strictly adhere to the following writing style, tone, and formatting pipeline.

## 1. Tone and Voice (The Practitioner Standard)
- **Practitioner-First, Zero Fluff**: Write strictly as a hands-on engineer sharing battlefield notes. Never preach from an ivory tower or use corporate PR speak.
- **Banned "AI Slop" Vocabulary**: NEVER use generic AI cliches such as: *delve, testament, tapestry, landscape, revolutionize, furthermore, moreover, beacon, game changer (unless backed by exact metrics), in today's fast-paced world, thrilled to announce*.
- **Sentence Rhythm & Cadence**:
  - Mix short, punchy anchor sentences (3 to 6 words) with clear explanatory statements.
  - Keep paragraphs strictly under 3 sentences. Give text plenty of visual breathing room.
  - Use natural contractions ("it's", "you've", "let's", "don't") to preserve conversational warmth.
- **Typography Constraint**: Use colons, parentheses, commas, or standard hyphens instead of em-dashes or en-dashes.
- **Concrete Metrics over Adjectives**: Replace subjective hype with real empirical numbers (e.g., "10x latency drop (250ms to 25ms)" instead of "dramatically faster").
- **Second-Person & Inclusive**: Talk directly to the reader ("you've probably faced this before", "if you run local agents daily").
- **Language Blending**: Crisp technical English, allowing conversational phrasing where it aids intuition.

## 2. Structure and Formatting Patterns
- **Hook → Problem → Alternatives → Solution → Payoff**:
  - **Strong hooks**: Jump straight in media res (e.g., "Someone just built...", "Most AI tools try too hard to look smart...", "I got tired of generic review prompts...").
  - **Problem Setup**: Clearly surface a production pain point in 1-2 lines.
  - **Alternatives**: Briefly explain why current approaches fall short.
  - **Solution / The Core Mechanic**: Introduce the solution and break down how it works step-by-step.
- **Bullet-Heavy Explanations**:
  - Use clean bullet lists (`•` or emojis like `🧠`, `⚡`, `🛡️`, `🎯`) for features, workflows, and use cases.
- **CTA Pattern (Call to Action)**:
  - Close with a grounded question for discussion (e.g., "What is the most frustrating thing about X in your team right now? Let's talk in the comments 👇").

## 3. LinkedIn Native Formatting (No Raw Markdown Asterisks)
- **The Formatting Constraint**: LinkedIn post inputs do not support native Markdown (`**bold**` or `### Header`). Raw Markdown renders as literal syntax asterisks.
- **The Solution**: Convert headers and bold keywords into **Unicode Mathematical Sans-Serif Bold** (e.g., 𝗪𝗵𝘆 𝗦𝗮𝗮𝗦 𝗳𝗼𝘂𝗻𝗱𝗲𝗿𝘀 𝗮𝗿𝗲 𝘀𝘄𝗲𝗮𝘁𝗶𝗻𝗴, 𝗣𝗿𝗼𝗽𝗿𝗶𝗲𝘁𝗮𝗿𝘆 𝗗𝗮𝘁𝗮) so formatting renders natively in the feed.
- **Line Break & Paragraph Spacing Protection (CRITICAL)**:
  - When text is pasted into LinkedIn, its sanitizer strips empty newlines and collapses paragraphs into a dense wall of text.
  - **The Solution**: Inject the invisible **Braille Pattern Blank character (`\u2800` / `⠀`)** onto every empty spacer line between paragraphs. LinkedIn recognizes `⠀` as a real character and will NEVER strip or collapse the spacing on desktop or mobile.

## 4. Programmatic Matte-Black Developer Graphics
- **No Generic AI Illustrations**: NEVER generate cartoonish, glossy, or uncanny AI illustrations. The image MUST look like a clean, human-designed developer artifact (Linear/Vercel aesthetic).
- **Generation Method**: Generate the image programmatically using Python (Pillow) with system fonts (San Francisco, Helvetica, Arial, or Menlo monospace) via the provided script `scripts/generate_infographic.py`.
- **Canvas & Theme**:
  - **Resolution**: 1200x1200 high-resolution square (1:1 aspect ratio, optimal for LinkedIn feeds).
  - **Background**: Deep matte black (`#050505`) with a subtle frame border (`#161616`).
  - **Typography & Mobile Readability Scale**:
    - Main Titles: 42px to 46px bold.
    - Card Headings: 24px to 26px bold.
    - Body Bullets: 20px to 22px minimum.
    - Terminal Code: 18px to 20px monospace.
  - **Layout**:
    - Top metadata pill badge + repo tag + bold title + 1-line subtitle.
    - 2-to-3 horizontal stacked cards with hand-drawn vector checkmarks (`✓` in `#2ecc71`) or crosses (`✕` in `#ff4d4d`).
    - Bottom row: macOS terminal card with colored window dots + practitioner takeaway quote box.

## 5. Output Deliverables
Whenever drafting a post, provide:
1. Canonical source draft saved as a `.md` file in `./output/linkedin_posts/`.
2. LinkedIn-ready text file (`_linkedin_ready.txt`) processed via `scripts/md_to_linkedin.py` with full Unicode bold and `U+2800` line spacing.
3. High-resolution 1200x1200 developer graphic (`.jpg`) rendered via `scripts/generate_infographic.py`.
4. In the chat response, always output the direct-paste text block so the user can copy it straight into LinkedIn.
