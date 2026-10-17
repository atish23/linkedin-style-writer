#!/usr/bin/env python3
"""
Generate high-contrast, dark-mode developer graphics (1200x1200) for LinkedIn.
Eliminates generic AI illustration slop with clean programmatic typography and geometric vector glyphs.

Requirements:
    pip install Pillow

Usage:
    python3 scripts/generate_infographic.py --output output.jpg
"""

import os
import sys
import argparse
import textwrap
from PIL import Image, ImageDraw, ImageFont

def find_system_font(preferred_list):
    for path in preferred_list:
        if os.path.exists(path):
            return path
    return None

def load_fonts():
    # Candidates across macOS, Linux, and Windows
    sans_candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNS.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "C:\\Windows\\Fonts\\arial.ttf"
    ]
    mono_candidates = [
        "/System/Library/Fonts/Menlo.ttc",
        "/Library/Fonts/Monaco.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
        "C:\\Windows\\Fonts\\consola.ttf"
    ]

    sans_path = find_system_font(sans_candidates)
    mono_path = find_system_font(mono_candidates)

    def get_font(path, size, index=0):
        if path:
            try:
                return ImageFont.truetype(path, size, index=index)
            except Exception:
                pass
        return ImageFont.load_default()

    return {
        "tag": get_font(mono_path, 15),
        "title": get_font(sans_path, 42, index=1),
        "subtitle": get_font(sans_path, 21),
        "tier_title": get_font(sans_path, 25, index=1),
        "tier_badge": get_font(mono_path, 14),
        "tier_sub": get_font(sans_path, 16),
        "bullet": get_font(sans_path, 21),
        "code_header": get_font(mono_path, 14),
        "code_main": get_font(mono_path, 17),
        "code_sub": get_font(mono_path, 15),
        "card_title": get_font(sans_path, 22, index=1),
        "punchline": get_font(sans_path, 21, index=1)
    }

def draw_check(ctx, cx, cy, size=15, color="#2ecc71", width=3):
    p1 = (cx - size / 2, cy)
    p2 = (cx - size / 6, cy + size / 2)
    p3 = (cx + size / 2, cy - size / 2)
    ctx.line([p1, p2], fill=color, width=width)
    ctx.line([p2, p3], fill=color, width=width)

def draw_cross(ctx, cx, cy, size=14, color="#ff4d4d", width=3):
    half = size / 2
    ctx.line([(cx - half, cy - half), (cx + half, cy + half)], fill=color, width=width)
    ctx.line([(cx - half, cy + half), (cx + half, cy - half)], fill=color, width=width)

def generate_graphic(output_path, title, subtitle, tag_badge, right_tag, tiers, terminal_lines, takeaway_dict):
    W, H = 1200, 1200
    img = Image.new("RGB", (W, H), "#050505")
    draw = ImageDraw.Draw(img)
    fonts = load_fonts()

    # Outer frame border
    draw.rectangle([25, 25, W - 25, H - 25], outline="#161616", width=1)

    # Top Bar
    draw.rounded_rectangle([50, 48, 280, 80], radius=6, fill="#111111", outline="#222222", width=1)
    draw.text((64, 55), tag_badge, fill="#888888", font=fonts["tag"])
    draw.text((W - 360, 55), right_tag, fill="#666666", font=fonts["tag"])

    # Header Title & Subtitle
    draw.text((50, 102), title, fill="#FFFFFF", font=fonts["title"])
    draw.text((50, 158), subtitle, fill="#999999", font=fonts["subtitle"])

    # Divider
    draw.line([(50, 204), (W - 50, 204)], fill="#1a1a1a", width=1)

    # 3 Horizontal Stacked Cards
    card_w = W - 100
    card_h = 165
    start_y = 225
    gap_y = 22

    cur_y = start_y
    for t in tiers:
        draw.rounded_rectangle([50, cur_y, 50 + card_w, cur_y + card_h], radius=10, fill="#0a0a0a", outline=t.get("border_color", "#1c354e"), width=1)

        left_box_w = 325
        draw.rounded_rectangle([70, cur_y + 18, 70 + 85, cur_y + 42], radius=4, fill=t.get("bg_color", "#0d1f2d"), outline=t.get("border_color", "#1c354e"), width=1)
        draw.text((78, cur_y + 23), t.get("tier_badge", "TIER"), fill=t.get("color", "#388bfd"), font=fonts["tier_badge"])

        draw.text((70, cur_y + 56), t.get("name", ""), fill="#FFFFFF", font=fonts["tier_title"])
        draw.text((70, cur_y + 98), t.get("role", ""), fill="#888888", font=fonts["tier_sub"])

        draw.line([(50 + left_box_w, cur_y + 16), (50 + left_box_w, cur_y + card_h - 16)], fill="#1a1a1a", width=1)

        b_start_x = 50 + left_box_w + 30
        b_y1 = cur_y + 36
        b_y2 = cur_y + 96

        bullets = t.get("bullets", ["", ""])
        draw_check(draw, b_start_x + 8, b_y1 + 10, size=15, color=t.get("color", "#2ecc71"), width=3)
        draw.text((b_start_x + 28, b_y1), bullets[0], fill="#e6edf3", font=fonts["bullet"])

        if len(bullets) > 1:
            draw_check(draw, b_start_x + 8, b_y2 + 10, size=15, color=t.get("color", "#2ecc71"), width=3)
            draw.text((b_start_x + 28, b_y2), bullets[1], fill="#e6edf3", font=fonts["bullet"])

        cur_y += card_h + gap_y

    # Bottom Grid: Terminal + Takeaway Box
    bot_y = 815
    bot_h = 350
    half_w = 535
    col_gap = 30
    left_x = 50
    right_x = left_x + half_w + col_gap

    # Terminal card
    draw.rounded_rectangle([left_x, bot_y, left_x + half_w, bot_y + bot_h], radius=10, fill="#0a0a0a", outline="#222222", width=1)
    draw.ellipse([left_x + 20, bot_y + 20, left_x + 28, bot_y + 28], fill="#333333")
    draw.ellipse([left_x + 34, bot_y + 20, left_x + 42, bot_y + 28], fill="#333333")
    draw.ellipse([left_x + 48, bot_y + 20, left_x + 56, bot_y + 28], fill="#333333")
    draw.text((left_x + 75, bot_y + 16), "terminal: execution session", fill="#555555", font=fonts["code_header"])

    t_y = bot_y + 55
    for text_line, color in terminal_lines:
        draw.text((left_x + 24, t_y), text_line, fill=color, font=fonts["code_main"] if t_y == bot_y + 55 else fonts["code_sub"])
        t_y += 36

    # Takeaway card
    draw.rounded_rectangle([right_x, bot_y, right_x + half_w, bot_y + bot_h], radius=10, fill="#0c0e12", outline="#182333", width=1)
    draw.text((right_x + 28, bot_y + 20), takeaway_dict.get("badge", "PRACTITIONER STANDARD"), fill="#58a6ff", font=fonts["tag"])
    draw.text((right_x + 28, bot_y + 58), takeaway_dict.get("title_1", ""), fill="#FFFFFF", font=fonts["card_title"])
    draw.text((right_x + 28, bot_y + 88), takeaway_dict.get("title_2", ""), fill="#FFFFFF", font=fonts["card_title"])

    lines1 = textwrap.wrap(takeaway_dict.get("desc", ""), width=42)
    d_y = bot_y + 135
    for l in lines1:
        draw.text((right_x + 28, d_y), l, fill="#999999", font=fonts["tier_sub"])
        d_y += 24

    draw.line([(right_x + 28, bot_y + 205), (right_x + half_w - 28, bot_y + 205)], fill="#1a2433", width=1)
    draw.text((right_x + 28, bot_y + 225), takeaway_dict.get("sub_badge", ""), fill="#e6edf3", font=fonts["tier_badge"])
    draw.text((right_x + 28, bot_y + 252), takeaway_dict.get("sub_desc", ""), fill="#888888", font=fonts["tier_sub"])
    draw.text((right_x + 28, bot_y + 290), takeaway_dict.get("punchline", ""), fill="#58a6ff", font=fonts["punchline"])

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    img.save(output_path, quality=98)
    print(f"Successfully generated clean developer graphic at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 1200x1200 developer graphic")
    parser.add_argument("--output", default="output/sample_infographic.jpg", help="Output path")
    args = parser.parse_args()

    # Default developer sample
    sample_tiers = [
        {
            "tier_badge": "TIER 1",
            "name": "Executor / Builder",
            "role": "Active code author & session driver",
            "color": "#388bfd",
            "bg_color": "#0d1f2d",
            "border_color": "#1c354e",
            "bullets": [
                "Runs interactive commands and handles rapid code refactoring.",
                "High velocity, low latency, and balanced cost for continuous building."
            ]
        },
        {
            "tier_badge": "TIER 2",
            "name": "Parallel Scouts",
            "role": "Read-only background exploration",
            "color": "#2ecc71",
            "bg_color": "#0a1f14",
            "border_color": "#164529",
            "bullets": [
                "Maps file tree, searches call sites, and pulls documentation.",
                "Executes searches in parallel at fraction-of-cent token cost."
            ]
        },
        {
            "tier_badge": "TIER 3",
            "name": "Advisory Judge",
            "role": "Strategic reviewer on call (0 idle tokens)",
            "color": "#f39c12",
            "bg_color": "#2b1a09",
            "border_color": "#593713",
            "bullets": [
                "Only summoned on critical triggers: Plan Lock, Error x2, Final Audit.",
                "Delivers senior architectural judgement with 80%+ session token savings."
            ]
        }
    ]

    sample_terminal = [
        ("$ agent --model builder --advisor judge", "#388bfd"),
        ("✓ Driver assigned to active editing session", "#2ecc71"),
        ("✓ Read-only subagents spawned for search & grep", "#888888"),
        ("✓ Strategic advisor on call (0 tokens consumed)", "#888888"),
        ("→ Rule: Consult advisor before plan lock or error x2", "#e5a93c")
    ]

    sample_takeaway = {
        "badge": "PRACTITIONER STANDARD",
        "title_1": "Reviews should spot real bugs,",
        "title_2": "not argue about variable names.",
        "desc": "Don't spend flagship models on routine bash tasks. Split your agents into execution tiers and advisory tiers.",
        "sub_badge": "System One Micro-Routing:",
        "sub_desc": "Fast deterministic checks run in milliseconds for micro-cents.",
        "punchline": "Big models only see complex decisions."
    }

    generate_graphic(args.output, "THE MULTI-TIER AGENT STACK", "Split your workflow into specialized tiers. Each model handles what it does best.", "AGENT ARCHITECTURE", "github.com/developer/project", sample_tiers, sample_terminal, sample_takeaway)
