import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

# Canvas setup: 1080x1350 (4:5 LinkedIn mobile vertical format)
W, H = 1080, 1350
img = Image.new("RGB", (W, H), "#F6F4ED")  # Warm cream / paper canvas
draw = ImageDraw.Draw(img)

# System Fonts
helv_font = "/System/Library/Fonts/Helvetica.ttc"
menlo_font = "/System/Library/Fonts/Menlo.ttc"

def get_font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
    except Exception:
        return ImageFont.load_default()

font_title_bold = get_font(helv_font, 48, index=1)
font_title_sub = get_font(helv_font, 22)
font_badge = get_font(helv_font, 18, index=1)
font_card_title = get_font(helv_font, 22, index=1)
font_card_sub = get_font(helv_font, 16)
font_body = get_font(helv_font, 15)
font_body_bold = get_font(helv_font, 15, index=1)
font_mono = get_font(menlo_font, 14)
font_step_num = get_font(helv_font, 26, index=1)

def draw_card(ctx, xy, bg_color="#FFFFFF", border_color="#1A1A1A", width=2, radius=12):
    ctx.rounded_rectangle(xy, radius=radius, fill=bg_color, outline=border_color, width=width)

def draw_check(ctx, cx, cy, size=14, color="#16A34A", width=2):
    p1 = (cx - size/2, cy)
    p2 = (cx - size/6, cy + size/2)
    p3 = (cx + size/2, cy - size/2)
    ctx.line([p1, p2], fill=color, width=width)
    ctx.line([p2, p3], fill=color, width=width)

def draw_selection_handles(ctx, x1, y1, x2, y2, color="#2563EB", size=8):
    corners = [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]
    hs = size // 2
    for cx, cy in corners:
        ctx.rectangle([cx - hs, cy - hs, cx + hs, cy + hs], fill="#FFFFFF", outline=color, width=2)

def draw_wrapped_text(ctx, text, x, y, font, color, max_chars, line_spacing=22):
    lines = textwrap.wrap(text, width=max_chars)
    cy = y
    for l in lines:
        ctx.text((x, cy), l, fill=color, font=font)
        cy += line_spacing
    return cy

# --- HEADER SECTION ---
header_y = 45
draw_card(draw, [40, header_y, 280, header_y + 36], bg_color="#FED7AA", border_color="#1A1A1A", width=2, radius=8)
draw.text((55, header_y + 8), "DECISION ENGINE v1", fill="#7C2D12", font=font_badge)

draw.text((W - 320, header_y + 8), "Local Edge Inference | Ollama", fill="#4B5563", font=font_body_bold)

ty = header_y + 55
draw.text((40, ty), "Inside a Local ", fill="#1A1A1A", font=font_title_bold)
w_prefix = draw.textlength("Inside a Local ", font=font_title_bold)
draw.text((40 + w_prefix, ty), "Decision Model", fill="#2563EB", font=font_title_bold)

draw.text((40, ty + 60), "How 42ms edge routing protects privacy and slashes 85% of LLM prompt tokens.", fill="#4B5563", font=font_title_sub)
draw.line([(40, ty + 105), (W - 40, ty + 105)], fill="#D1D5DB", width=1)

# --- MIDDLE SECTION: 3 BENTO CARDS ---
mid_y = 285
col_w = 310
gap = 25

# 1. Left Card: User & Local Hook
c1_x1, c1_x2 = 40, 40 + col_w
draw_card(draw, [c1_x1, mid_y, c1_x2, mid_y + 520], bg_color="#FFFFFF", border_color="#1A1A1A", width=2, radius=12)

draw_card(draw, [c1_x1 + 16, mid_y + 16, c1_x1 + 130, mid_y + 48], bg_color="#FEF08A", border_color="#1A1A1A", width=2, radius=6)
draw.text((c1_x1 + 26, mid_y + 22), "Input 01", fill="#713F12", font=font_badge)

draw.text((c1_x1 + 16, mid_y + 65), "Terminal Query", fill="#1A1A1A", font=font_card_title)
draw_wrapped_text(draw, "Developer prompt submitted in Claude Code or Antigravity.", c1_x1 + 16, mid_y + 98, font_card_sub, "#4B5563", max_chars=34, line_spacing=22)

items_left = [
    ("Prompt Event", "PreInvocation Hook intercepts query before network call."),
    ("Zero Egress", "Prompt stays strictly inside local memory boundary."),
    ("Latency Impact", "Instant execution with zero network roundtrip lag.")
]
sy = mid_y + 165
for label, desc in items_left:
    draw_card(draw, [c1_x1 + 16, sy, c1_x2 - 16, sy + 95], bg_color="#F8FAFC", border_color="#CBD5E1", width=1, radius=8)
    draw_check(draw, c1_x1 + 34, sy + 25, color="#2563EB")
    draw.text((c1_x1 + 48, sy + 15), label, fill="#1E293B", font=font_body_bold)
    draw_wrapped_text(draw, desc, c1_x1 + 24, sy + 42, font_body, "#64748B", max_chars=32, line_spacing=20)
    sy += 112

# 2. Middle Card: Ollama Decision Engine (Hero)
c2_x1, c2_x2 = c1_x2 + gap, c1_x2 + gap + col_w
draw_card(draw, [c2_x1, mid_y, c2_x2, mid_y + 520], bg_color="#EFF6FF", border_color="#1D4ED8", width=2, radius=12)
draw_selection_handles(draw, c2_x1, mid_y, c2_x2, mid_y + 520, color="#1D4ED8")

draw_card(draw, [c2_x1 + 16, mid_y + 16, c2_x1 + 165, mid_y + 48], bg_color="#BFDBFE", border_color="#1D4ED8", width=2, radius=6)
draw.text((c2_x1 + 26, mid_y + 22), "Decision 02", fill="#1E3A8A", font=font_badge)

draw.text((c2_x1 + 16, mid_y + 65), "Ollama tev1:4b", fill="#1E3A8A", font=font_card_title)
draw_wrapped_text(draw, "Single forward pass classification via TypeSafe JEV spec.", c2_x1 + 16, mid_y + 98, font_card_sub, "#1E40AF", max_chars=34, line_spacing=22)

items_mid = [
    ("PII Gatekeeper", "Catches unmasked PAN, keys, or credentials locally."),
    ("Category Routing", "Maps query to exact 1-2 candidate files in 42ms."),
    ("Zero Cloud Token", "Calibrated categorical logits. Zero token billing.")
]
sy = mid_y + 165
for label, desc in items_mid:
    draw_card(draw, [c2_x1 + 16, sy, c2_x2 - 16, sy + 95], bg_color="#FFFFFF", border_color="#93C5FD", width=1, radius=8)
    draw_check(draw, c2_x1 + 34, sy + 25, color="#16A34A")
    draw.text((c2_x1 + 48, sy + 15), label, fill="#1E3A8A", font=font_body_bold)
    draw_wrapped_text(draw, desc, c2_x1 + 24, sy + 42, font_body, "#3B82F6", max_chars=32, line_spacing=20)
    sy += 112

# 3. Right Card: Cloud Reasoning (System 2)
c3_x1, c3_x2 = c2_x2 + gap, c2_x2 + gap + col_w
draw_card(draw, [c3_x1, mid_y, c3_x2, mid_y + 520], bg_color="#FFFFFF", border_color="#1A1A1A", width=2, radius=12)

draw_card(draw, [c3_x1 + 16, mid_y + 16, c3_x1 + 145, mid_y + 48], bg_color="#BBF7D0", border_color="#1A1A1A", width=2, radius=6)
draw.text((c3_x1 + 26, mid_y + 22), "Output 03", fill="#14532D", font=font_badge)

draw.text((c3_x1 + 16, mid_y + 65), "Cloud LLM", fill="#1A1A1A", font=font_card_title)
draw_wrapped_text(draw, "Claude Sonnet receives clean, pruned context without bloat.", c3_x1 + 16, mid_y + 98, font_card_sub, "#4B5563", max_chars=34, line_spacing=22)

items_right = [
    ("Targeted Context", "Passes 1.2k tokens instead of 45k repo tokens."),
    ("High Precision", "Zero hallucination on internal engineering rules."),
    ("Fast Execution", "Cloud model synthesizes solution in under 2s.")
]
sy = mid_y + 165
for label, desc in items_right:
    draw_card(draw, [c3_x1 + 16, sy, c3_x2 - 16, sy + 95], bg_color="#F8FAFC", border_color="#CBD5E1", width=1, radius=8)
    draw_check(draw, c3_x1 + 34, sy + 25, color="#16A34A")
    draw.text((c3_x1 + 48, sy + 15), label, fill="#1E293B", font=font_body_bold)
    draw_wrapped_text(draw, desc, c3_x1 + 24, sy + 42, font_body, "#64748B", max_chars=32, line_spacing=20)
    sy += 112

# Connecting arrows between middle columns
def draw_arrow(ctx, x1, y1, x2, y2, color="#1A1A1A"):
    ctx.line([(x1, y1), (x2, y1)], fill=color, width=2)
    ctx.polygon([(x2, y1), (x2 - 8, y1 - 5), (x2 - 8, y1 + 5)], fill=color)

draw_arrow(draw, c1_x2 + 4, mid_y + 260, c2_x1 - 4, mid_y + 260)
draw_arrow(draw, c2_x2 + 4, mid_y + 260, c3_x1 - 4, mid_y + 260)

# --- BOTTOM SECTION: 5-STEP PIPELINE RUNTIME ---
bot_y = 835
draw_card(draw, [40, bot_y, W - 40, bot_y + 440], bg_color="#FFFFFF", border_color="#1A1A1A", width=2, radius=12)

draw_card(draw, [60, bot_y - 18, 380, bot_y + 22], bg_color="#FED7AA", border_color="#1A1A1A", width=2, radius=8)
draw.text((75, bot_y - 10), "THE 4-STAGE PIPELINE RUNTIME", fill="#7C2D12", font=font_badge)

stages = [
    ("1", "User Prompt", "Query submitted in terminal CLI.", "#EFF6FF", "#1D4ED8"),
    ("2", "Pre-Hook", "Intercepts prompt in 2ms on-device.", "#FEF08A", "#713F12"),
    ("3", "Ollama tev1", "42ms decision pass: PII & routing.", "#EFF6FF", "#1D4ED8"),
    ("4", "Pruned Context", "Injects 1-2 exact candidate files.", "#DCFCE7", "#15803D"),
    ("5", "Cloud Sonnet", "High-speed reasoned answer.", "#F3E8FF", "#6B21A8")
]

step_w = (W - 80 - 40 - (4 * 16)) // 5
sx = 60
card_top = bot_y + 45
for num, title, desc, bg, txt_c in stages:
    draw_card(draw, [sx, card_top, sx + step_w, card_top + 280], bg_color=bg, border_color="#1A1A1A", width=2, radius=10)
    
    draw.ellipse([sx + step_w//2 - 20, card_top + 16, sx + step_w//2 + 20, card_top + 56], fill="#FFFFFF", outline="#1A1A1A", width=2)
    draw.text((sx + step_w//2 - 8, card_top + 22), num, fill="#1A1A1A", font=font_step_num)
    
    draw.text((sx + 12, card_top + 75), title, fill=txt_c, font=font_body_bold)
    draw_wrapped_text(draw, desc, sx + 12, card_top + 115, font_body, "#374151", max_chars=18, line_spacing=24)
        
    sx += step_w + 16

# Footer Quote / Signature
draw.line([(60, bot_y + 355), (W - 60, bot_y + 355)], fill="#E5E7EB", width=1)
draw.text((60, bot_y + 375), "Architecture Rule:", fill="#1A1A1A", font=font_body_bold)
draw.text((205, bot_y + 375), "Run local decision models for reflexes. Keep cloud LLMs for synthesis.", fill="#2563EB", font=font_body_bold)

draw.text((W - 320, bot_y + 375), "Open Source | Atish Maske", fill="#6B7280", font=font_body)

out_path = "output/linkedin_posts/2026-10-18_1604_local_decision_models/decision_model_bento.jpg"
img.save(out_path, quality=98)
print("Saved clean bright bento graphic to:", out_path)
