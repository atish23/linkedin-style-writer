#!/usr/bin/env python3
"""
Convert standard Markdown to LinkedIn-ready Unicode formatted text.

Solves two fundamental LinkedIn limitations:
1. No native markdown support: Converts **bold**, *italic*, headers, bullets to Unicode symbols.
2. Collapsing blank lines: Injects Braille Pattern Blank (U+2800 '⠀') on empty lines so LinkedIn never strips line breaks.

Usage:
    python3 scripts/md_to_linkedin.py input.md output.txt
    python3 scripts/md_to_linkedin.py input.md
    cat input.md | python3 scripts/md_to_linkedin.py
"""

import sys
import re

def to_unicode_bold(text: str) -> str:
    # Mathematical Sans-Serif Bold
    res = []
    for char in text:
        code = ord(char)
        if 65 <= code <= 90:  # A-Z
            res.append(chr(0x1D5D4 + (code - 65)))
        elif 97 <= code <= 122:  # a-z
            res.append(chr(0x1D5EE + (code - 97)))
        elif 48 <= code <= 57:  # 0-9
            res.append(chr(0x1D7EC + (code - 48)))
        else:
            res.append(char)
    return "".join(res)

def to_unicode_italic(text: str) -> str:
    # Mathematical Sans-Serif Italic
    res = []
    for char in text:
        code = ord(char)
        if 65 <= code <= 90:  # A-Z
            res.append(chr(0x1D608 + (code - 65)))
        elif 97 <= code <= 122:  # a-z
            res.append(chr(0x1D622 + (code - 97)))
        else:
            res.append(char)
    return "".join(res)

def to_unicode_mono(text: str) -> str:
    # Mathematical Monospace
    res = []
    for char in text:
        code = ord(char)
        if 65 <= code <= 90:  # A-Z
            res.append(chr(0x1D670 + (code - 65)))
        elif 97 <= code <= 122:  # a-z
            res.append(chr(0x1D68A + (code - 97)))
        elif 48 <= code <= 57:  # 0-9
            res.append(chr(0x1D7F6 + (code - 48)))
        else:
            res.append(char)
    return "".join(res)

def convert_markdown_to_linkedin(md_text: str) -> str:
    lines = md_text.splitlines()
    out_lines = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        # Handle code block boundaries
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            # Monospace format for code blocks
            out_lines.append("  " + to_unicode_mono(line.strip()))
            continue

        # Handle empty lines: inject U+2800 (Braille blank) to protect spacing
        if not stripped:
            out_lines.append("\u2800")
            continue

        cur = line

        # Headers: ### Header -> Bold text
        header_match = re.match(r"^#{1,6}\s+(.+)$", cur)
        if header_match:
            header_text = header_match.group(1).strip()
            cur = to_unicode_bold(header_text)
            out_lines.append(cur)
            continue

        # Bullet lists: - item or * item -> • item
        bullet_match = re.match(r"^(\s*)[-*]\s+(.+)$", cur)
        if bullet_match:
            indent = bullet_match.group(1)
            content = bullet_match.group(2)
            cur = f"{indent}• {content}"

        # Inline Bold: **text**
        cur = re.sub(r"\*\*(.+?)\*\*", lambda m: to_unicode_bold(m.group(1)), cur)

        # Inline Italic: *text*
        cur = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", lambda m: to_unicode_italic(m.group(1)), cur)

        # Inline Code: `text`
        cur = re.sub(r"`([^`]+?)`", lambda m: to_unicode_mono(m.group(1)), cur)

        out_lines.append(cur)

    return "\n".join(out_lines)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            content = f.read()
        converted = convert_markdown_to_linkedin(content)
        if len(sys.argv) > 2:
            with open(sys.argv[2], "w", encoding="utf-8") as f:
                f.write(converted)
            print(f"Saved LinkedIn formatted text to: {sys.argv[2]}")
        else:
            print(converted)
    else:
        content = sys.stdin.read()
        print(convert_markdown_to_linkedin(content))
