#!/bin/bash

# 天涯神贴大神智囊团 - 测试脚本

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     天涯神贴大神智囊团 - 安装测试                         ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

TEST_PASSED=0
TEST_FAILED=0

# 测试函数
test_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} 文件存在: $1"
        ((TEST_PASSED++))
    else
        echo -e "${RED}✗${NC} 文件缺失: $1"
        ((TEST_FAILED++))
    fi
}

test_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} 目录存在: $1"
        ((TEST_PASSED++))
    else
        echo -e "${RED}✗${NC} 目录缺失: $1"
        ((TEST_FAILED++))
    fi
}

test_executable() {
    if [ -x "$1" ]; then
        echo -e "${GREEN}✓${NC} 可执行: $1"
        ((TEST_PASSED++))
    else
        echo -e "${RED}✗${NC} 不可执行: $1"
        ((TEST_FAILED++))
    fi
}

echo "📁 检查文件结构..."
test_file "SKILL.md"
test_file "README.md"
test_file "install.sh"
test_file "config.json"
test_file "requirements.txt"
test_file "tianya-gods"
test_file "scripts/team-orchestrator.py"
test_file "scripts/__init__.py"
test_file "references/research/01-writings.md"
test_file "references/research/02-conversations.md"
test_file "references/research/03-expression-dna.md"
test_file "references/research/04-external-views.md"
test_file "references/research/05-decisions.md"
test_file "references/research/06-timeline.md"

echo ""
echo "📂 检查目录结构..."
test_dir "scripts"
test_dir "references"
test_dir "references/research"

echo ""
echo "🔧 检查可执行权限..."
test_executable "install.sh"
test_executable "tianya-gods"

echo ""
echo "🐍 检查Python环境..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    echo -e "${GREEN}✓${NC} Python环境: $PYTHON_VERSION"
    ((TEST_PASSED++))
else
    echo -e "${RED}✗${NC} Python3未安装"
    ((TEST_FAILED++))
fi

echo ""
echo "📋 检查配置文件..."
if [ -f "config.json" ]; then
    if python3 -c "import json; json.load(open('config.json'))" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} config.json 格式正确"
        ((TEST_PASSED++))
    else
        echo -e "${RED}✗${NC} config.json 格式错误"
        ((TEST_FAILED++))
    fi
fi

echo ""
echo "🚀 检查Python脚本..."
if python3 -m py_compile scripts/team-orchestrator.py 2>/dev/null; then
    echo -e "${GREEN}✓${NC} team-orchestrator.py 语法正确"
    ((TEST_PASSED++))
else
    echo -e "${RED}✗${NC} team-orchestrator.py 语法错误"
    ((TEST_FAILED++))
fi

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                   测试结果                                ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "通过: $TEST_PASSED"
echo "失败: $TEST_FAILED"
echo ""

if [ $TEST_FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ 所有测试通过！安装包完整。${NC}"
    echo ""
    echo "使用方法:"
    echo "  1. 运行安装: bash install.sh"
    echo "  2. 使用命令: tianya-gods '你的问题'"
    echo "  3. 触发词: 「启动天涯智囊团」+ 问题"
    exit 0
else
    echo -e "${RED}❌ 部分测试失败，请检查文件完整性。${NC}"
    exit 1
fi
