#!/bin/bash
# 一键安装 momozi-ai-book Novelists Skill库到 OpenClaw
# 用法: bash install-novelists.sh

set -e

REPO_URL="https://github.com/momozi1996/momozi-ai-book"
SKILLS_DIR="${HOME}/.stepclaw/skills"
TEMP_DIR="/tmp/momozi-ai-book-$$"

echo "🚀 开始安装 Novelists Skill库..."
echo "📦 仓库: ${REPO_URL}"
echo "📁 目标目录: ${SKILLS_DIR}"
echo ""

# 创建临时目录
mkdir -p "${TEMP_DIR}"
cd "${TEMP_DIR}"

# 下载仓库（只下载Novelists目录）
echo "⬇️  正在下载仓库..."
curl -sL "${REPO_URL}/archive/refs/heads/main.zip" -o repo.zip
unzip -q repo.zip

# 进入Novelists目录
cd momozi-ai-book-main/Novelists

# 定义要安装的skill列表
SKILLS=(
    "liucixin-skill:刘慈欣"
    "yuhua-skill:余华"
    "moyan-skill:莫言"
    "zhangailing-skill:张爱玲"
    "ximurong-skill:席慕容"
    "qiongyao-skill:琼瑶"
    "libaihua-skill:李碧华"
    "dangnianmingyue-skill:当年明月"
)

# 安装每个skill
INSTALLED=0
FAILED=0

for skill_info in "${SKILLS[@]}"; do
    skill_name="${skill_info%%:*}"
    author_name="${skill_info##*:}"
    
    if [ -d "${skill_name}" ]; then
        target_dir="${SKILLS_DIR}/${skill_name}"
        
        # 如果已存在，先备份
        if [ -d "${target_dir}" ]; then
            echo "🔄 更新 ${author_name} (${skill_name})..."
            rm -rf "${target_dir}.backup"
            mv "${target_dir}" "${target_dir}.backup"
        else
            echo "📥 安装 ${author_name} (${skill_name})..."
        fi
        
        # 复制skill到目标目录
        cp -r "${skill_name}" "${target_dir}"
        
        # 验证安装
        if [ -f "${target_dir}/SKILL.md" ]; then
            echo "   ✅ ${author_name} 安装成功"
            ((INSTALLED++))
        else
            echo "   ❌ ${author_name} 安装失败"
            ((FAILED++))
        fi
    else
        echo "⚠️  跳过 ${author_name} (${skill_name}) - 目录不存在"
        ((FAILED++))
    fi
done

# 清理临时目录
cd /
rm -rf "${TEMP_DIR}"

echo ""
echo "========================================"
echo "✅ 安装完成!"
echo "========================================"
echo "📊 统计:"
echo "   成功: ${INSTALLED} 个Skill"
echo "   失败: ${FAILED} 个Skill"
echo ""
echo "📁 安装位置: ${SKILLS_DIR}"
echo ""
echo "🎯 使用方法:"
echo "   在OpenClaw中直接使用触发词:"
echo "   • 刘慈欣视角 | 像刘慈欣那样写"
echo "   • 余华视角 | 像余华那样写"
echo "   • 莫言视角 | 像莫言那样写"
echo "   • 张爱玲视角 | 像张爱玲那样写"
echo "   • 席慕容视角 | 像席慕容那样写"
echo "   • 琼瑶视角 | 像琼瑶那样写"
echo "   • 李碧华视角 | 像李碧华那样写"
echo "   • 当年明月视角 | 像当年明月那样写"
echo ""
echo "⭐ 如果对你有帮助，请给仓库点个 star:"
echo "   ${REPO_URL}"
echo "========================================"
