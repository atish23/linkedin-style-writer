---
name: linkedin-style-writer
description: Use this skill when asked to write a LinkedIn post. It enforces the user's personal writing style based on their technical background, AI tool evangelism, and educator-builder tone.
---

# LinkedIn Style Writer

When writing a LinkedIn post for the user, you must strictly adhere to the following writing style, tone, and structure based on their historical LinkedIn posts and long-form technical articles.

## Tone and Voice (Atish's English Writing Style)
- **Practitioner-First, Zero Fluff**: Write strictly as a hands-on engineer sharing battlefield notes. Never preach from an ivory tower.
- **Banned "AI Slop" Vocabulary**: NEVER use generic AI cliches such as: *delve, testament, tapestry, landscape, revolutionize, furthermore, moreover, beacon, game changer (unless backed by exact metrics), in today's fast-paced world*.
- **Empirical Prompt Telemetry & Typing DNA (Mined from 629+ User Prompts)**:
  - **Prompt Distribution Baseline**: 49% concise queries (6-25 words), 22% ultra-short commands (<=5 words), average prompt ~32 words.
  - **Raw Input Habit**: Atish types lowercase, fast, high-velocity instructions with zero throat-clearing ("can u check", "what about zapier", "make it tool agnostic", "do one thing").
  - **Mapping from Prompts to Posts**:
    - **No Preambles**: Never start with "In today's fast-paced AI era..." or corporate fluff. Start immediately in media res: "I got tired of generic AI review bots...", "Most AI code reviews feel like an over-eager intern...".
    - **High Signal-to-Noise**: Every line must carry technical weight. If a sentence can be cut without losing meaning, cut it.
    - **Concrete Code & CLI Commands**: Always provide real, copy-pasteable terminal commands (`git clone ...`, `bash setup/install.sh`) instead of high-level hand-waving.
    - **Battlefield Verification**: Highlight real metrics, edge cases, and verification steps (e.g., "Mines 400+ historical PR comments", "Kills over 70% of false alarms").
- **Sentence Rhythm & Cadence**:
  - Mix short, punchy anchor sentences (3 to 6 words) with clear explanatory statements.
  - Keep paragraphs strictly under 3 sentences. Give text plenty of visual breathing room.
  - Use natural contractions ("it's", "you've", "let's", "don't") to preserve conversational warmth.
- **Typography Constraint (STRICT)**: NEVER use em-dashes or en-dashes. Use colons, parentheses, commas, or standard hyphens instead.
- **Concrete Metrics over Adjectives**: Replace subjective hype with real empirical numbers (e.g., "10x latency drop (250ms to 25ms)" instead of "dramatically faster").
- **Conversational & Pedagogical**: Use natural rhetorical prompts ("Sounds reasonable, right?", "What is the problem with X?", "Can you explain it to a five-year-old?").
- **Second-Person & Inclusive**: Talk directly to the reader ("you've probably faced this before", "if you run local agents daily").
- **Language Blending**: Primarily crisp technical English, with occasional natural Hinglish phrasing when it aids intuitive understanding.
- **Anti-Slop Stance**: Explicitly reject generic AI buzzwords, repetitive summaries, and boilerplate disclaimers.

## Structure and Formatting Patterns
- **Ultra-Short & High-Crux (NO Long Posts on LinkedIn - STRICT)**:
  - People on LinkedIn do not read walls of text. Keep posts ultra-short and high-signal.
  - Strict length cap: **75 to 130 words total (strictly 5 to 8 short lines / punchy bullets)**.
  - Total mobile reading time must be under **20 seconds**.
  - Canonical 4-part structure:
    1. Line 1: Killer hook (the blunt observation, personal friction, or pain point).
    2. Lines 2-3: The crux (what was built and what it replaces).
    3. Lines 4-7: 3 to 4 punchy bullet takeaways with concrete metrics.
    4. Line 8: Direct GitHub repo / resource link or crisp concluding takeaway.
- **Dual Publishing Strategy (LinkedIn Crux + Hashnode Deep-Dive)**:
  - **LinkedIn Post**: Ultra-short teaser delivering the core crux in 20 seconds.
  - **Hashnode Blog**: If an architecture breakdown requires multi-step code walkthroughs, benchmark tables, or long-form essays, write a separate comprehensive article on Hashnode (`output/hashnode_blogs/<slug>.md`) and link to it.
- **Bullet-Heavy Explanations**:
  - Lean on bullet lists to explain features, step-by-step flows, and use cases.
- **Emphasis**: Use bold text for key metrics and important technical terminology to make the post highly scannable.
- **LinkedIn Native Formatting (No Raw Markdown Asterisks)**:
  - LinkedIn post inputs do not support native Markdown (`**bold**` or `### Header`).
  - Convert bold headers and phrases into **Unicode Mathematical Sans-Serif Bold** (e.g., 𝗪𝗵𝘆 𝗦𝗮𝗮𝗦 𝗳𝗼𝘂𝗻𝗱𝗲𝗿𝘀 𝗮𝗿𝗲 𝘀𝘄𝗲𝗮𝘁𝗶𝗻𝗴, 𝗣𝗿𝗼𝗽𝗿𝗶𝗲𝘁𝗮𝗿𝘆 𝗗𝗮𝘁𝗮) so formatting renders directly without ugly markdown asterisks.
  - Use clean Unicode bullets (`•` or `👉` or `⚡`) instead of plain hyphens.
- **Line Break & Paragraph Spacing Protection (CRITICAL)**:
  - When text is pasted into LinkedIn, LinkedIn's post sanitizer strips empty lines and collapses paragraphs into a dense wall of text.
  - **The Solution**: Inject the invisible **Braille Pattern Blank character (`\u2800` / `⠀`)** onto every empty spacer line between paragraphs. LinkedIn recognizes `⠀` as a real character and will NEVER strip or collapse the spacing on desktop or mobile.
- **NEVER Include ASCII Box Diagrams in Post Text (STRICT)**:
  - NEVER insert ASCII flowcharts, box-and-arrow diagrams (e.g., `[ Prompt ] -> | v [ Hook ] -> [ LLM ]`), or text-based architecture trees into the LinkedIn post text.
  - In LinkedIn feeds, ASCII box art breaks across mobile screen widths, suffers from variable kerning, and looks cluttered.
  - All architecture workflows, pipelines, and step-by-step system interactions must be rendered into the companion programmatic developer graphic or animated GIF instead. Keep the post text clean, punchy, bullet-driven, and narrative-first.
- **Ending & Closing Rules (No Engagement Bait - STRICT)**:
  - NEVER end posts with generic engagement-bait questions such as: "Let's discuss in the comments 👇", "What do you think? Drop a comment below", "How are you handling X in your workflows? Let's discuss in the comments".
  - These lines feel like generic marketing slop and dilute practitioner credibility.
  - Instead, end decisively on:
    1. A sharp technical takeaway or architecture principle (e.g., "Keep your reflexive routing local, and save your cloud tokens for heavy reasoning.").
    2. A concrete CLI command, resource, or GitHub repository link.
    3. Stop as soon as the technical thought is complete with zero synthetic throat-clearing.

## Empirical Post Performance Hierarchy & Archetypes (From Live Telemetry)

Mined directly from Atish's live LinkedIn feed metrics:

### Tier 1: Viral Reach & Mass Engagement (100 to 350+ reactions)
- **Archetype**: Deeply personal career transitions, long-tenure reflections, and in-person conference/meetup attendance.
- **Examples**:
  - *Farewell to EdCast (346 reactions, 52 comments, 10.3K impressions)*: 8-year milestone, vulnerable reflection ("Some endings are not just professional. They are personal."), and human gratitude.
  - *Deccan Queen on Rails Kickoff (95 reactions, 5 comments, 3.8K impressions)*: High-energy in-person conference arrival in Pune.
- **Visual Requirement**: Mandate **Multi-Photo Collages (3 to 4 real photos)** showing human faces, colleagues, team events, or conference stages. Real human faces drive 5x higher feed engagement than digital diagrams.

### Tier 2: High Developer Authority & Engagement (35 to 50 reactions)
- **Archetype**: Direct practitioner pain-point fixes, RFC standards, and hands-on utility.
- **Examples**:
  - *HTTP QUERY Verb RFC (48 reactions, 4 comments, 3K impressions)*: Solved an immediate annoying backend developer headache with clean problem-solution framing.
  - *RTK Token Proxy for Claude Code (37 reactions, 1.6K impressions)*: Addressed explosive agent CLI token costs with real, measurable savings.
  - *n8n + Gemini Weekend Automation (32 reactions, 1.2K impressions)*: "This weekend I had free time, so I built X to solve Y."
- **Key Formula**: Frame around personal operational friction: "I got tired of X burning my budget/time, so I built/tested Y."

### Tier 3: Deep Architectural Specs & Micro-Routing (15 to 30 reactions)
- **Archetype**: Local model routing, sub-50ms edge hooks, on-device AI, and agent orchestrators.
- **Examples**:
  - *Local Decision Models / Ollama tev1:4b (27 reactions)*.
  - *Gemma 4 on-device AI (24 reactions)*.
  - *Paperclip agent orchestrator (17 reactions)*.
- **Value**: High authority among senior leads and architects. Keeps technical signal high. Pair with Warm Bento graphics or clean GitHub repo screenshots.

### Tier 4: Strictly Banned Anti-Patterns (Under 12 reactions)
Telemetry reveals the exact patterns that reliably flop:
1. **Third-Party PR Announcements**: Never post generic vendor news ("Exciting News in Long-Context AI: SubQ has launched 12M tokens..." received only 9 reactions). If you did not test it locally, do not post it.
2. **Passive News & Drama Curation**: Never curate corporate controversy without hands-on code implications (Alibaba distillation attack received 10 reactions).
3. **Passive Link-Drops in Comments**: Never post generic teasers that offload the value to comment links ("Will AI replace your job? Link is in comments" received 12 reactions). Every post must deliver complete value natively.
4. **Textbook Summaries**: Never explain abstract study concepts (Feynman technique, basic SOLID) without anchoring them in a real production outage, concurrency crash, or concrete personal experiment.

## The "Personal Skin in the Game" Hook Rule
Every technical post MUST anchor its opening line in one of three personal foundations:
1. **An In-Person Conversation or Local Event**: *"Last week at Deccan Queen on Rails in Pune, someone asked: 'With AI writing code so fast, what should developers focus on?'"*
2. **Direct Operational Friction**: *"Using AI agents in your terminal burns through tokens because the LLM reads raw command logs. I was looking into RTK to stop this."*
3. **A Hands-on Weekend Build**: *"This weekend I had some free time, so I decided to finally fix how I manage my daily ideas and tasks."*

Never open with passive market commentary or third-party press releases.

## Thematic Focus Areas
1. **AI Tools Evangelism**: Highlight cutting-edge tools. Explain what problem they solve, how they work conceptually, and why they matter for practitioners.
2. **Systems & Architecture**: Abstract complex systems into intuitive mental models (e.g., "Diagrams do not fail. Systems do.").
3. **Knowledge-Management Storytelling**: Present patterns as practical workflows.
4. **Career Narrative & Gratitude**: For milestone posts, be emotionally rich, people-centric, and thank leaders/peers by name.

## Visual Asset Guidelines
- **No Pitch-Black Terminal Dumps**: Avoid gloomy, all-black (`#050505`) code screenshots that blend into the feed and get ignored.
- **Standard Visual Formats**:
  1. **Multi-Photo Collages (Default for Events, Meetups & Milestones)**:
     - 3 to 4 real camera photos of human faces, team members, conference auditoriums, or meetup sessions.
     - Highest engagement driver across the entire profile.
  2. **Warm Bento Architecture Graphic (Default for Architecture & Systems)**:
     - **Canvas & Aspect Ratio**: 1080x1350 (4:5 vertical portrait) to capture 30% more vertical screen real estate on mobile feeds.
     - **Color Palette**: Warm cream paper background (`#F6F4ED` / `#FAF8F5`), crisp dark container borders (`#1A1A1A`), and soft pastel badges (`#FEF08A`, `#BFDBFE`, `#BBF7D0`, `#FED7AA`).
     - **Layout Hierarchy**: Top hero title with colored accent keyword + 3 Bento cards (Input / Engine / Output) + 5-step horizontal pipeline cards across the bottom.
     - **Generator Template**: Adapt `/Users/atishmaske/Documents/LLM WIKI/scripts/generate_bright_infographic.py`.
  3. **GitHub Repository Screenshots (Default for Open-Source & Repo Posts)**:
     - Clean, high-resolution screenshot of the GitHub repo header, star badge, and clear README introduction.
     - Authentic, instantly recognized, and trusted by developers.
  4. **Remotion Motion Graphics & Animated GIFs (For Workflows, Signals & Terminal Pipelines)**:
     - **Persistent Architecture Rule (MANDATORY)**: Never start with a blank screen or sequentially reveal empty cards. All bento cards, titles, and diagrams must be 100% visible and readable from frame 0 so mobile viewers capture the full context in the first second.
     - **Ambient Motion Focus**: Animate the continuous *signal movement* (looping energy dots traveling along connectors, subtle cycling spotlight on active pipeline stages, and pulsing terminal cursors) rather than building basic UI.
     - Render as 1080x1350 (4:5 vertical) or 800x1000 looping GIF (`.gif`) under 5MB.
  5. **Video Posts Caution**: Post text must be 100% self-sufficient. Assume mobile users will not unmute or play the video.

## Persistence and Output Deliverables (CRITICAL)
- **Dedicated Topic Bundle Folder Structure with Date & Time (MANDATORY)**:
  - NEVER dump loose post files or media assets directly into the root of `output/linkedin_posts/`.
  - Every LinkedIn post MUST have its own dedicated topic folder prefixed with the creation date and time:
    `/Users/atishmaske/Documents/LLM WIKI/output/linkedin_posts/YYYY-MM-DD_HHMM_<topic_slug>/`
    (Example: `2026-10-18_1604_local_decision_models`, `2026-10-17_1311_linkedin_style_writer`)
  - Inside that topic folder, keep everything related to the post self-contained:
    1. `<topic_slug>_post.md` (or `post.md`): Canonical markdown draft.
    2. `<topic_slug>_post_linkedin_ready.txt`: Direct-paste LinkedIn text generated via `scripts/md_to_linkedin.py`.
    3. Media assets: Multi-photo collages (`.jpg`), Warm Bento infographics (`.jpg`), animated GIFs (`.gif`), or videos (`.mp4`).
    4. Generator scripts: Any custom Python script used to render the post's visual assets.
- **Save Dual Post Formats**:
  1. Save the canonical source draft as a markdown file (`.md`) inside the post's dedicated timestamped topic folder.
  2. Automatically generate and save the **direct-paste LinkedIn version** (`<filename>_linkedin_ready.txt`) inside the same topic folder by running:
     `python3 "/Users/atishmaske/Documents/LLM WIKI/scripts/md_to_linkedin.py" "<path_to_md>" "<path_to_txt>"`
     This guarantees the user has a 1-click copy-paste text file with full Unicode bold and `U+2800` line-break protection.
  3. In the chat response, ALWAYS output the LinkedIn-ready direct-paste text block so the user can copy it immediately.
- **Personal Persona Blueprint & Prompt Telemetry**: Cross-reference `/Users/atishmaske/Documents/LLM WIKI/memory/user_persona.md`, `/Users/atishmaske/Documents/LLM WIKI/memory/user_prompts.jsonl`, `/Users/atishmaske/Documents/LLM WIKI/memory/persona_telemetry.json`, and `/Users/atishmaske/Documents/LLM WIKI/wiki/concepts/atish-maske-writing-voice.md` to guarantee alignment with Atish's syntax, cognitive pacing, and anti-slop rules.

Follow these rules strictly whenever tasked with drafting, editing, or reviewing a LinkedIn post for the user.
