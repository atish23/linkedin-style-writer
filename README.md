# linkedin-style-writer

> Turn your AI coding agent into a high-signal, practitioner-first LinkedIn technical writer.
> Solves two fundamental LinkedIn pain points: **collapsed empty line spaces** and **lack of Markdown support**, plus generates **programmatic matte-black developer graphics** without generic AI illustration slop.

Works with **Claude Code**, **Google Antigravity**, **Cursor**, **Codex**, or standalone via CLI.

---

## Why This Exists

Most technical LinkedIn posts drafted by AI fail for three reasons:
1. **AI Slop & Corporate Fluff**: Overusing buzzwords (*delve, tapestry, landscape, revolutionize, furthermore, game-changer*), long throat-clearing intros, and passive corporate language.
2. **LinkedIn Breaks Formatting**: LinkedIn post inputs do not support native Markdown (`**bold**` shows raw asterisks), and LinkedIn's post sanitizer automatically strips empty newlines, condensing your structured bullet points into an unreadable wall of text.
3. **Generic AI Image Slop**: Image generators produce glossy, cartoonish, uncanny 3D illustrations that developer audiences immediately scroll past.

`linkedin-style-writer` replaces that entire mess with a battle-tested technical pipeline.

---

## Features

### 1. The Practitioner Voice (Zero Fluff Standard)
- **Battlefield Notes**: Writes strictly as a hands-on engineer sharing technical lessons.
- **Strict Banned Vocabulary**: Enforces an anti-slop dictionary.
- **Rhythm & Breathing Room**: Paragraphs strictly capped under 3 sentences with punchy anchor lines.
- **Concrete Metrics**: Replaces subjective hype with real empirical numbers ("10x latency drop (250ms to 25ms)" instead of "dramatically faster").

### 2. Built-in LinkedIn Formatting Engine (`md_to_linkedin.py`)
- **Mathematical Unicode Alphanumeric Conversion**: Translates `**bold**`, `*italic*`, and monospace into native Mathematical Unicode characters (`𝗪𝗵𝘆 𝗦𝗮𝗮𝗦 𝗳𝗼𝘂𝗻𝗱𝗲𝗿𝘀 𝗮𝗿𝗲 𝘀𝘄𝗲𝗮𝘁𝗶𝗻𝗴`) that render natively in LinkedIn feeds without asterisks.
- **Line Spacing Defense (`U+2800` Braille Blank)**: Injects the invisible Unicode Braille Pattern Blank (`⠀`) onto every empty spacer line. LinkedIn registers `⠀` as a non-whitespace character, permanently preventing collapsed lines on mobile and desktop feeds.

### 3. Programmatic Matte-Black Developer Graphics (`generate_infographic.py`)
- **Zero AI Illustrations**: Programmatically rendered using Python Pillow (`PIL`) with clean system typography.
- **1200x1200 High-Res Square**: Optimized for desktop and mobile feeds.
- **Mobile-Scale Typography**: Main titles (42px-44px), card titles (24px-26px), and bullets (20px-22px minimum) ensuring complete legibility on smartphones without pinching or zooming.
- **macOS Terminal Window**: Built-in CLI card with colored window controls and execution status.
- **Vector Glyphs**: Coordinate-drawn vector checkmarks (`✓`) and crosses (`✕`) to prevent missing font box artifacts (`▯`).

---

## ⚡ Quickstart (2-Minute Setup)

### 1. Clone the repository
```bash
git clone https://github.com/atish23/linkedin-style-writer.git
cd linkedin-style-writer
```

### 2. Run the installer
```bash
bash setup/install.sh
```
This registers the skill in:
- `~/.claude/skills/linkedin-style-writer` (Claude Code)
- `~/.gemini/antigravity/skills/linkedin-style-writer` (Antigravity)
- Local project `.claude/skills/` (if present)

---

## 💻 Usage

### Inside Your Agent (Claude Code / Antigravity / Cursor)

Simply invoke the slash command:
```bash
/linkedin-style-writer write a post about my new open-source CLI tool and why developers need it
```

Or pass a URL or file:
```bash
/linkedin-style-writer https://github.com/my-org/my-repo research this tool and draft a post
```

The agent will automatically produce:
1. Canonical `.md` source draft.
2. LinkedIn-ready text file (`_linkedin_ready.txt`) with Unicode bold and `U+2800` line spacing.
3. 1200x1200 dark-mode developer graphic (`.jpg`).
4. 1-click copy-paste text block in the conversation.

---

### Standalone CLI Usage

#### Convert any Markdown file to LinkedIn-ready text:
```bash
python3 scripts/md_to_linkedin.py draft.md output.txt
```

#### Generate a clean developer graphic:
```bash
python3 scripts/generate_infographic.py --output output/developer_cheat_sheet.jpg
```

---

## Project Structure

```
linkedin-style-writer/
├── SKILL.md                          # The core agent skill definition
├── scripts/
│   ├── md_to_linkedin.py             # Markdown → Unicode + U+2800 spacer converter
│   └── generate_infographic.py       # Programmatic 1200x1200 developer graphic generator
├── setup/
│   └── install.sh                    # Multi-agent installer script
├── LICENSE                           # MIT License
└── README.md                         # Documentation
```

---

## License

MIT © 2026. Built for developers who care about signal over slop.
