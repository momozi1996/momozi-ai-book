#!/bin/bash

# 天涯神贴大神智囊团 - 一键安装脚本
# 基于ClawTeam多Agent架构

set -e

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     天涯神贴大神智囊团 - 一键安装程序                     ║"
echo "║     Tianya Gods Team - One-Click Installer               ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查Python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo -e "${GREEN}✓${NC} 检测到 Python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    echo -e "${GREEN}✓${NC} 检测到 Python"
else
    echo -e "${RED}✗${NC} 未检测到 Python，请先安装 Python 3.7+"
    exit 1
fi

# 检查Python版本
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo -e "${BLUE}ℹ${NC} Python版本: $PYTHON_VERSION"

# 创建安装目录
INSTALL_DIR="$HOME/.stepclaw/skills/tianya-gods-team"
echo ""
echo "📁 创建安装目录: $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"
mkdir -p "$INSTALL_DIR/scripts"
mkdir -p "$INSTALL_DIR/references/research"

# 复制文件
echo ""
echo "📋 复制文件..."
cp SKILL.md "$INSTALL_DIR/"
cp README.md "$INSTALL_DIR/"
cp scripts/team-orchestrator.py "$INSTALL_DIR/scripts/"
cp references/research/*.md "$INSTALL_DIR/references/research/"

# 创建__init__.py
touch "$INSTALL_DIR/scripts/__init__.py"

# 创建启动脚本
echo ""
echo "🚀 创建启动脚本..."
cat > "$INSTALL_DIR/tianya-gods" << 'EOF'
#!/bin/bash
# 天涯神贴大神智囊团 - 启动脚本

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -z "$1" ]; then
    echo "使用方法: tianya-gods '你的问题'"
    echo "示例: tianya-gods '我现在该不该买房？'"
    exit 1
fi

python3 "$SCRIPT_DIR/scripts/team-orchestrator.py" "$@"
EOF

chmod +x "$INSTALL_DIR/tianya-gods"

# 创建符号链接
if [ -d "$HOME/.local/bin" ]; then
    ln -sf "$INSTALL_DIR/tianya-gods" "$HOME/.local/bin/tianya-gods"
    echo -e "${GREEN}✓${NC} 已创建命令: tianya-gods"
fi

# 创建OpenClaw Skill链接
if [ -d "$HOME/.stepclaw/workspace/.agents/skills" ]; then
    ln -sf "$INSTALL_DIR" "$HOME/.stepclaw/workspace/.agents/skills/tianya-gods-team"
    echo -e "${GREEN}✓${NC} 已链接到 OpenClaw Skill 目录"
fi

# 创建requirements.txt
cat > "$INSTALL_DIR/requirements.txt" << 'EOF'
# 天涯神贴大神智囊团依赖
# Python 3.7+
EOF

# 创建配置文件
cat > "$INSTALL_DIR/config.json" << 'EOF'
{
  "name": "tianya-gods-team",
  "version": "3.0.0",
  "description": "天涯神贴大神智囊团 - 20位传奇大神多Agent决策系统",
  "author": "女娲 · Skill造人术",
  "trigger_words": [
    "启动天涯智囊团",
    "召集大神",
    "20位大神分析",
    "天涯智囊团"
  ],
  "gods_count": 20,
  "technology": "multi-agent-swarm",
  "architecture": "ClawTeam"
}
EOF

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║              ✅ 安装完成！                                ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "📊 安装信息:"
echo "  • 安装目录: $INSTALL_DIR"
echo "  • 大神数量: 20位"
echo "  • 触发词: 启动天涯智囊团、召集大神、20位大神分析"
echo ""
echo "🚀 使用方法:"
echo ""
echo "  方式1 - 命令行:"
echo "    tianya-gods '我现在该不该买房？'"
echo ""
echo "  方式2 - Python API:"
echo "    cd $INSTALL_DIR"
echo "    python3 -c \""
echo "    import asyncio"
echo "    from scripts.team_orchestrator import TianyaGodsTeam"
echo "    async def main():"
echo "        team = TianyaGodsTeam()"
echo "        result = await team.analyze('我现在该不该买房？')"
echo "        print(result)"
echo "    asyncio.run(main())"
echo "    \""
echo ""
echo "  方式3 - OpenClaw触发词:"
echo "    「启动天涯智囊团」我现在该不该买房？"
echo ""
echo "📚 更多信息请查看: $INSTALL_DIR/README.md"
echo ""
