#!/bin/bash
# ClawTeam导演智囊团 - 导演匹配脚本
# 根据创作需求匹配最适合的导演组合

# 用法: ./match_directors.sh "需求描述"

DEMAND="$1"

if [ -z "$DEMAND" ]; then
    echo "用法: $0 \"创作需求描述\""
    echo "示例: $0 \"科幻悬疑片，关于时间循环\""
    exit 1
fi

echo "=========================================="
echo "🎬 ClawTeam导演智囊团 - 导演匹配"
echo "=========================================="
echo ""
echo "创作需求: $DEMAND"
echo ""

# 关键词匹配逻辑
if echo "$DEMAND" | grep -qi "科幻\|未来\|时间\|空间"; then
    echo "📌 匹配类型: 科幻"
    echo ""
    echo "推荐导演组合:"
    echo "  🎬 克里斯托弗·诺兰 - 时空叙事专家"
    echo "  🎬 詹姆斯·卡梅隆 - 技术先驱"
    echo "  🎬 斯皮尔伯格 - 科幻情感平衡"
    echo ""
    echo "首席导演: 诺兰"
    echo "协作模式: 顺序链 (视觉→叙事→技术)"
fi

if echo "$DEMAND" | grep -qi "爱情\|都市\|孤独\|情感"; then
    echo "📌 匹配类型: 都市情感"
    echo ""
    echo "推荐导演组合:"
    echo "  🎬 王家卫 - 感官诗学"
    echo "  🎬 侯孝贤 - 真实感"
    echo "  🎬 是枝裕和 - 日常温情"
    echo ""
    echo "首席导演: 王家卫"
    echo "协作模式: 主席团 (王家卫统筹)"
fi

if echo "$DEMAND" | grep -qi "武侠\|江湖\|动作"; then
    echo "📌 匹配类型: 武侠/动作"
    echo ""
    echo "推荐导演组合:"
    echo "  🎬 张艺谋 - 视觉奇观"
    echo "  🎬 徐克 - 武侠革新"
    echo "  🎬 李安 - 文化融合"
    echo ""
    echo "首席导演: 张艺谋"
    echo "协作模式: 辩论投票"
fi

if echo "$DEMAND" | grep -qi "犯罪\|悬疑\|黑色"; then
    echo "📌 匹配类型: 犯罪/黑色"
    echo ""
    echo "推荐导演组合:"
    echo "  🎬 大卫·芬奇 - 冷峻悬疑"
    echo "  🎬 杜琪峰 - 宿命黑色"
    echo "  🎬 朴赞郁 - 华丽暴力"
    echo ""
    echo "首席导演: 大卫·芬奇"
    echo "协作模式: 顺序链"
fi

if echo "$DEMAND" | grep -qi "社会\|阶级\|现实"; then
    echo "📌 匹配类型: 社会现实"
    echo ""
    echo "推荐导演组合:"
    echo "  🎬 奉俊昊 - 阶级批判"
    echo "  🎬 贾樟柯 - 纪实凝视"
    echo "  🎬 杨德昌 - 都市解剖"
    echo ""
    echo "首席导演: 奉俊昊"
    echo "协作模式: 主席团"
fi

echo ""
echo "=========================================="
echo "使用建议:"
echo "1. 激活对应导演Agent"
echo "2. 选择协作模式"
echo "3. 开始创意会诊"
echo "=========================================="
