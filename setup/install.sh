#!/usr/bin/env bash
set -e

echo "=============================================="
echo "  Installing linkedin-style-writer skill"
echo "=============================================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Ensure Python scripts are executable
chmod +x "$SCRIPT_DIR/scripts/md_to_linkedin.py"
chmod +x "$SCRIPT_DIR/scripts/generate_infographic.py"

# Check Python and Pillow
if ! command -v python3 &>/dev/null; then
    echo "Warning: python3 is not installed or not in PATH."
else
    if ! python3 -c "import PIL" &>/dev/null; then
        echo "Note: Pillow (PIL) is not installed. Installing Pillow for infographic generation..."
        python3 -m pip install Pillow || echo "Please install Pillow manually: pip install Pillow"
    fi
fi

# Detect environments
INSTALLED_TARGETS=0

# 1. Claude Code global directory
CLAUDE_SKILLS_DIR="$HOME/.claude/skills/linkedin-style-writer"
mkdir -p "$CLAUDE_SKILLS_DIR"
cp -r "$SCRIPT_DIR/SKILL.md" "$SCRIPT_DIR/scripts" "$CLAUDE_SKILLS_DIR/"
echo "✓ Installed to Claude Code skills: $CLAUDE_SKILLS_DIR"
INSTALLED_TARGETS=$((INSTALLED_TARGETS + 1))

# 2. Antigravity skills directory
AGY_SKILLS_DIR="$HOME/.gemini/antigravity/skills/linkedin-style-writer"
mkdir -p "$AGY_SKILLS_DIR"
cp -r "$SCRIPT_DIR/SKILL.md" "$SCRIPT_DIR/scripts" "$AGY_SKILLS_DIR/"
echo "✓ Installed to Antigravity skills: $AGY_SKILLS_DIR"
INSTALLED_TARGETS=$((INSTALLED_TARGETS + 1))

# 3. Local project .claude/skills directory if present
if [ -d "$PWD/.claude" ]; then
    LOCAL_SKILLS_DIR="$PWD/.claude/skills/linkedin-style-writer"
    mkdir -p "$LOCAL_SKILLS_DIR"
    cp -r "$SCRIPT_DIR/SKILL.md" "$SCRIPT_DIR/scripts" "$LOCAL_SKILLS_DIR/"
    echo "✓ Installed to local project .claude skills: $LOCAL_SKILLS_DIR"
fi

echo ""
echo "=============================================="
echo "  Installation Complete!"
echo "  Run '/linkedin-style-writer' in your agent"
echo "=============================================="
