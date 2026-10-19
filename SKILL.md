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
- **Ultra-Short & High-Crux (NO Long Posts on LinkedIn - STRICT)**:
  - People on LinkedIn do not read walls of text. Keep posts ultra-short, punchy, and high-signal.
  - Strict length cap: **75 to 130 words total (strictly 5 to 8 short lines / punchy bullets)**.
  - Total mobile reading time must be under **20 seconds**.
  - Canonical 4-part structure:
    1. Line 1: Killer hook (the blunt observation or pain point).
    2. Lines 2-3: The crux (what was built and what it replaces).
    3. Lines 4-7: 3 to 4 punchy bullet takeaways with concrete metrics.
    4. Line 8: Direct GitHub repo / resource link.
- **Dual Publishing Strategy (LinkedIn Crux + Hashnode Deep-Dive)**:
  - **LinkedIn Post**: Ultra-short teaser delivering the core crux in 20 seconds.
  - **Hashnode / Technical Blog**: If an architecture breakdown requires multi-step code walkthroughs, benchmark tables, or long-form essays, write a separate comprehensive article on Hashnode (`output/hashnode_blogs/<slug>.md`) and link to it.
- **Bullet-Heavy Explanations**:
  - Use clean bullet lists (`•` or emojis like `🧠`, `⚡`, `🛡️`, `🎯`) for features, workflows, and use cases.
- **NEVER Include ASCII Box Diagrams in Post Text (STRICT)**:
  - NEVER insert ASCII flowcharts, box-and-arrow diagrams (e.g., `[ Prompt ] -> │ ▼ [ Hook ] -> [ LLM ]`), or text trees into the LinkedIn post body.
  - In LinkedIn feeds, ASCII box art breaks across mobile screen widths, suffers from variable font kerning, and looks cluttered.
  - All architecture workflows, pipelines, and step-by-step system interactions must be rendered into the companion visual graphic or animated GIF instead. Keep post text clean, bullet-focused, and narrative-first.
- **Ending & Closing Rules (No Engagement Bait - STRICT)**:
  - NEVER end posts with generic engagement-bait questions such as: "Let's discuss in the comments 👇", "What do you think? Drop a comment below", or "How are you handling X in your workflows?".
  - These lines feel like generic marketing slop and dilute technical credibility.
  - Instead, end decisively on:
    1. A sharp technical takeaway or architecture principle.
    2. A concrete CLI command, resource, or GitHub repository link.
    3. Stop as soon as the technical thought is complete with zero synthetic throat-clearing.

## 3. LinkedIn Native Formatting (No Raw Markdown Asterisks)
- **The Formatting Constraint**: LinkedIn post inputs do not support native Markdown (`**bold**` or `### Header`). Raw Markdown renders as literal syntax asterisks.
- **The Solution**: Convert headers and bold keywords into **Unicode Mathematical Sans-Serif Bold** (e.g., 𝗪𝗵𝘆 𝗦𝗮𝗮𝗦 𝗳𝗼𝘂𝗻𝗱𝗲𝗿𝘀 𝗮𝗿𝗲 𝘀𝘄𝗲𝗮𝘁𝗶𝗻𝗴, 𝗣𝗿𝗼𝗽𝗿𝗶𝗲𝘁𝗮𝗿𝘆 𝗗𝗮𝘁𝗮) so formatting renders natively in the feed.
- **Line Break & Paragraph Spacing Protection (CRITICAL)**:
  - When text is pasted into LinkedIn, its sanitizer strips empty newlines and collapses paragraphs into a dense wall of text.
  - **The Solution**: Inject the invisible **Braille Pattern Blank character (`\u2800` / `⠀`)** onto every empty spacer line between paragraphs. LinkedIn recognizes `⠀` as a real character and will NEVER strip or collapse the spacing on desktop or mobile.

## 4. Visual Asset Guidelines (Warm Bento Architecture & GitHub Screenshots)
- **No Pitch-Black Terminal Dumps**: Avoid gloomy, all-black (`#050505`) code screenshots that blend into the feed and get ignored.
- **Standard Visual Formats**:
  1. **Warm Bento Architecture Graphic (Default for Architecture & Concepts)**:
     - **Canvas & Aspect Ratio**: 1080x1350 (4:5 vertical portrait) to capture 30% more vertical screen real estate on mobile feeds.
     - **Color Palette**: Warm cream paper background (`#F6F4ED` / `#FAF8F5`), crisp dark container borders (`#1A1A1A`), and soft pastel badges (`#FEF08A`, `#BFDBFE`, `#BBF7D0`, `#FED7AA`).
     - **Layout Hierarchy**: Top hero title with colored accent keyword + 3 Bento cards (Input / Engine / Output) + 5-step horizontal pipeline cards across the bottom.
     - **Generator Template**: Adapt `scripts/generate_bright_infographic.py`.
  2. **GitHub Repository Screenshots (Default for Open-Source & Repo Posts)**:
     - Whenever introducing, launching, or referencing an open-source GitHub repository, take a clean, high-resolution screenshot of the GitHub repository's main page and README header.
     - Real GitHub UI (repo title, stars, badges, and clean markdown intro) is instantly recognized, authentic, and trusted by developers.
  3. **Sequential Animated GIF (For Terminal Hooks & Pipelines)**:
     - Multi-frame looping GIF (1000x1000, 150-250KB) showing step-by-step CLI execution, hook interception, and runtime results.
- **Generation Method**: Generated programmatically using Python (Pillow) with system fonts (San Francisco, Helvetica, Arial, or Menlo monospace).

## 5. Output Deliverables & Folder Structure
Whenever drafting a post, organize deliverables into a dedicated timestamped topic bundle:
- **Topic Folder Path**: `./output/linkedin_posts/YYYY-MM-DD_HHMM_<topic_slug>/`
- **Inside the Topic Folder**:
  1. `<topic_slug>_post.md`: Canonical source draft markdown (under 130 words).
  2. `<topic_slug>_post_linkedin_ready.txt`: Pre-compiled LinkedIn-ready text processed via `scripts/md_to_linkedin.py` with full Unicode bold and `U+2800` line spacing.
  3. Visual assets: Warm bento architecture graphic (`.jpg`), GitHub repo screenshot (`.png`), or animated workflow GIF (`.gif`).
  4. Generator script: Python script used to render the visual assets.
- In the chat response, always output the direct-paste text block so the user can copy it straight into LinkedIn.
