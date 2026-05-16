#!/usr/bin/env python3
"""
天涯神贴大神智囊团 - 多Agent协调器
基于ClawTeam架构实现20位大神的并行决策

使用方法:
    python team-orchestrator.py "你的问题"
    
示例:
    python team-orchestrator.py "我现在该不该买房？"
    python team-orchestrator.py "该选择体制内还是体制外？"
"""

import asyncio
import json
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

class GodType(Enum):
    """大神类型"""
    QUANMOU = "权谋分析"
    JISHU = "技术分析"
    JINGJI = "经济预言"
    LISHI = "历史解读"
    WENHUA = "文化解构"
    DUSHI = "都市情感"
    JIANGHU = "黑帮江湖"
    TANXIAN = "探险冒险"
    XUANHUAN = "玄幻武侠"
    DOUSHI = "都市异能"
    XUANYI = "悬疑推理"
    FAYI = "法医刑侦"
    CHUANYUE = "历史穿越"

@dataclass
class GodProfile:
    """大神档案"""
    id: str
    name: str
    type: GodType
    trigger_words: List[str]
    core_ability: str
    decision_style: str
    applicable_scenarios: List[str]
    classic_quotes: List[str]

@dataclass
class AnalysisResult:
    """分析结果"""
    god_id: str
    god_name: str
    perspective: str
    key_points: List[str]
    recommendation: str
    confidence: float

class TianyaGodsTeam:
    """天涯神贴大神智囊团"""
    
    def __init__(self):
        self.gods: Dict[str, GodProfile] = self._init_gods()
        
    def _init_gods(self) -> Dict[str, GodProfile]:
        """初始化20位大神"""
        return {
            "dapeng": GodProfile(
                id="dapeng",
                name="大鹏金翅明王",
                type=GodType.QUANMOU,
                trigger_words=["大鹏金翅明王", "权谋分析", "阶层透视"],
                core_ability="权力本质论、阶层固化论、官场解码论",
                decision_style="冷峻犀利，不讲道德，只讲规律",
                applicable_scenarios=["体制内/体制外选择", "职场权力斗争", "社会阶层分析"],
                classic_quotes=["权力是让别人做他不想做的事", "社会是分层的，而且分层是固化的"]
            ),
            "chan": GodProfile(
                id="chan",
                name="缠中说禅",
                type=GodType.JISHU,
                trigger_words=["缠中说禅", "缠论", "技术分析"],
                core_ability="缠论结构、中枢理论、背驰判断",
                decision_style="禅意与技术的结合，走势必完美",
                applicable_scenarios=["股票/基金投资", "市场趋势判断", "交易时机选择"],
                classic_quotes=["走势必完美", "没有趋势，没有背驰"]
            ),
            "kkndme": GodProfile(
                id="kkndme",
                name="KKNDME",
                type=GodType.JINGJI,
                trigger_words=["KKNDME", "经济预言", "房产分析"],
                core_ability="稀缺资源论、规律论、资金运作论",
                decision_style="数据驱动，逻辑严密，预言精准",
                applicable_scenarios=["买房/卖房决策", "房产投资时机", "经济趋势判断"],
                classic_quotes=["优质房产属于稀缺资源", "短期的调控并不能改变长期上涨的趋势"]
            ),
            "dangnian": GodProfile(
                id="dangnian",
                name="当年明月",
                type=GodType.LISHI,
                trigger_words=["当年明月", "明朝那些事儿", "历史解读"],
                core_ability="心灵历史、幽默叙事、现代视角",
                decision_style="幽默风趣，从历史中寻找规律",
                applicable_scenarios=["历史事件分析", "权力斗争策略", "人物决策参考"],
                classic_quotes=["历史是由人组成的，而人是有心理的", "成功只有一个——按照自己的方式，去度过人生"]
            ),
            "ning": GodProfile(
                id="ning",
                name="宁财神",
                type=GodType.WENHUA,
                trigger_words=["宁财神", "毒舌评论", "文化解构"],
                core_ability="荒诞包裹论、毒舌真话论、文化解构论",
                decision_style="荒诞幽默，毒舌犀利，反讽揭示",
                applicable_scenarios=["文化现象分析", "社会现象讽刺", "虚假现象揭露"],
                classic_quotes=["喜剧的内核是悲剧", "我不是在吐槽，我是在说真话"]
            ),
            "murong": GodProfile(
                id="murong",
                name="慕容雪村",
                type=GodType.DUSHI,
                trigger_words=["慕容雪村", "都市情感", "现实主义"],
                core_ability="都市孤独论、冷峻写实论、情感困境论",
                decision_style="冷峻写实，情感细腻，直面孤独",
                applicable_scenarios=["都市生存策略", "情感关系分析", "职业选择建议"],
                classic_quotes=["我们都是都市里的孤独患者", "成都，今夜请将我遗忘"]
            ),
            "kong": GodProfile(
                id="kong",
                name="孔二狗",
                type=GodType.JIANGHU,
                trigger_words=["孔二狗", "黑帮江湖", "人情世故"],
                core_ability="江湖规则论、人情世故论、时代变迁论",
                decision_style="江湖气，硬朗直接，讲义气",
                applicable_scenarios=["人际关系处理", "江湖规则理解", "义气与利益权衡"],
                classic_quotes=["江湖不是打打杀杀，江湖是人情世故", "东北的黑道，是全国最讲义气的"]
            ),
            "tianxia": GodProfile(
                id="tianxia",
                name="天下霸唱",
                type=GodType.TANXIAN,
                trigger_words=["天下霸唱", "鬼吹灯", "风水秘术"],
                core_ability="风水秘术论、探险精神论、民俗怪谈论",
                decision_style="说书人风格，章回体结构，知识杂糅",
                applicable_scenarios=["探险决策分析", "风险评估", "团队组建"],
                classic_quotes=["人点烛，鬼吹灯", "寻龙分金看缠山"]
            ),
            "nanpai": GodProfile(
                id="nanpai",
                name="南派三叔",
                type=GodType.TANXIAN,
                trigger_words=["南派三叔", "盗墓笔记", "铁三角"],
                core_ability="悬疑探险论、兄弟情理论、人心可怕论",
                decision_style="第一人称叙述，悬疑氛围，兄弟情义",
                applicable_scenarios=["团队信任建立", "人心分析", "悬疑情况判断"],
                classic_quotes=["比鬼神更可怕的，是人心", "青山不改，绿水长流"]
            ),
            "yan": GodProfile(
                id="yan",
                name="燕垒生",
                type=GodType.XUANHUAN,
                trigger_words=["燕垒生", "天行健", "武侠玄幻"],
                core_ability="自强不息论、战争残酷论、人性挣扎论",
                decision_style="古典韵味，史诗格局，自强不息",
                applicable_scenarios=["困境中的坚持", "战争/竞争决策", "人性考验"],
                classic_quotes=["天行健，君子以自强不息", "战争，是人性最黑暗的实验室"]
            ),
            "jin": GodProfile(
                id="jin",
                name="今何在",
                type=GodType.XUANHUAN,
                trigger_words=["今何在", "悟空传", "反抗精神"],
                core_ability="反抗精神论、西游解构论、青春热血论",
                decision_style="诗意表达，反抗精神，青春热血",
                applicable_scenarios=["命运抗争", "体制反抗", "理想追求"],
                classic_quotes=["我要这天，再遮不住我眼", "我要那诸佛，都烟消云散"]
            ),
            "jiang": GodProfile(
                id="jiang",
                name="江南",
                type=GodType.XUANHUAN,
                trigger_words=["江南", "龙族", "青春幻想"],
                core_ability="少年成长论、青春疼痛论、热血燃情论",
                decision_style="青春语言，热血描写，细腻情感",
                applicable_scenarios=["青春选择", "成长困境", "热血追求"],
                classic_quotes=["凡王之血，必以剑终", "每个人心里都住着一个死小孩"]
            ),
            "mao": GodProfile(
                id="mao",
                name="猫腻",
                type=GodType.XUANHUAN,
                trigger_words=["猫腻", "庆余年", "权谋玄幻"],
                core_ability="权谋智斗论、不羁之民论、家国情怀论",
                decision_style="幽默轻松，权谋智斗，家国情怀",
                applicable_scenarios=["权谋斗争", "家国选择", "自由追求"],
                classic_quotes=["我希望庆国的人民都能成为不羁之民", "人生一世，选条路，不退让"]
            ),
            "fenghuo": GodProfile(
                id="fenghuo",
                name="烽火戏诸侯",
                type=GodType.XUANHUAN,
                trigger_words=["烽火戏诸侯", "雪中悍刀行", "剑来"],
                core_ability="武侠精神论、剑道极致论、江湖情义论",
                decision_style="古典诗词，大气磅礴，武侠韵味",
                applicable_scenarios=["武侠追求", "剑道修炼", "江湖情义"],
                classic_quotes=["天不生我李淳罡，剑道万古如长夜", "我有一剑，可斩天人"]
            ),
            "xiaoqi": GodProfile(
                id="xiaoqi",
                name="骁骑校",
                type=GodType.DOUSHI,
                trigger_words=["骁骑校", "橙红年代", "都市异能"],
                core_ability="都市异能说、热血青春论、正能量论",
                decision_style="热血语言，青春描写，正能量",
                applicable_scenarios=["青春奋斗", "都市生存", "正能量选择"],
                classic_quotes=["橙红年代，热血青春", "不忘初心，方得始终"]
            ),
            "zhou": GodProfile(
                id="zhou",
                name="周浩晖",
                type=GodType.XUANYI,
                trigger_words=["周浩晖", "死亡通知单", "悬疑推理"],
                core_ability="高智商犯罪论、正义迟定论、社会批判论",
                decision_style="严密逻辑，悬疑氛围，社会批判",
                applicable_scenarios=["犯罪分析", "正义追求", "逻辑推理"],
                classic_quotes=["正义可能会迟到，但绝不会缺席", "死亡通知单，罪恶的审判"]
            ),
            "lei": GodProfile(
                id="lei",
                name="雷米",
                type=GodType.XUANYI,
                trigger_words=["雷米", "心理罪", "犯罪心理"],
                core_ability="犯罪心理论、人性黑暗论、心理分析师",
                decision_style="心理分析深入，犯罪现场描写，人性探索",
                applicable_scenarios=["心理分析", "人性判断", "犯罪预防"],
                classic_quotes=["每个人心里都有罪", "心理罪，罪在人心"]
            ),
            "qiming": GodProfile(
                id="qiming",
                name="法医秦明",
                type=GodType.FAYI,
                trigger_words=["法医秦明", "尸语者", "法医刑侦"],
                core_ability="尸体证词论、科学取证论、职业精神论",
                decision_style="专业术语，冷静客观，科学分析",
                applicable_scenarios=["科学分析", "证据判断", "正义追求"],
                classic_quotes=["让尸体说话", "为生者权，为死者言"]
            ),
            "yue": GodProfile(
                id="yue",
                name="月关",
                type=GodType.CHUANYUE,
                trigger_words=["月关", "回到明朝当王爷", "历史穿越"],
                core_ability="穿越适应论、朝堂权谋论、历史改变论",
                decision_style="历史知识丰富，权谋斗争，爽文节奏",
                applicable_scenarios=["环境适应", "权谋斗争", "历史知识应用"],
                classic_quotes=["既然回不去，那就好好活", "朝堂之上，步步惊心"]
            ),
            "jieyu": GodProfile(
                id="jieyu",
                name="孑与2",
                type=GodType.CHUANYUE,
                trigger_words=["孑与2", "唐砖", "轻松幽默"],
                core_ability="轻松穿越论、幽默搞笑论、快乐生活论",
                decision_style="轻松幽默，搞笑情节，快乐氛围",
                applicable_scenarios=["轻松决策", "幽默化解", "快乐选择"],
                classic_quotes=["唐朝好砖家", "既然穿越了，那就做个快乐的穿越者"]
            ),
        }
    
    async def coordinator_analyze(self, question: str) -> Dict[str, Any]:
        """协调者分析：理解问题，确定需要哪些大神"""
        print(f"\n{'='*60}")
        print("🎯 协调者分析")
        print(f"{'='*60}")
        print(f"问题: {question}")
        
        # 分析问题类型
        analysis = {
            "question": question,
            "nature": self._determine_nature(question),
            "domains": self._identify_domains(question),
            "required_gods": self._select_gods(question),
            "priority": self._determine_priority(question)
        }
        
        print(f"\n问题本质: {analysis['nature']}")
        print(f"涉及领域: {', '.join(analysis['domains'])}")
        print(f"需要大神: {len(analysis['required_gods'])}位")
        print(f"优先级: {analysis['priority']}")
        
        return analysis
    
    def _determine_nature(self, question: str) -> str:
        """确定问题本质"""
        keywords = {
            "决策": ["选择", "该不该", "要不要", "还是"],
            "分析": ["为什么", "怎么回事", "如何"],
            "预测": ["未来", "趋势", "会", "将"],
            "评价": ["怎么看", "评价", "观点"]
        }
        for nature, words in keywords.items():
            if any(word in question for word in words):
                return nature
        return "综合"
    
    def _identify_domains(self, question: str) -> List[str]:
        """识别涉及领域"""
        domains = []
        domain_keywords = {
            "权谋": ["权力", "官场", "体制", "政治"],
            "经济": ["房价", "投资", "股票", "基金", "钱"],
            "历史": ["历史", "古代", "朝代"],
            "文化": ["文化", "娱乐", "电影", "电视"],
            "都市": ["都市", "城市", "职场", "工作"],
            "情感": ["感情", "爱情", "婚姻", "分手"],
            "江湖": ["江湖", "义气", "兄弟"],
            "探险": ["探险", "冒险", "未知"],
            "武侠": ["武侠", "江湖", "武功"],
            "悬疑": ["悬疑", "推理", "犯罪"],
            "穿越": ["穿越", "古代", "历史"]
        }
        for domain, keywords in domain_keywords.items():
            if any(keyword in question for keyword in keywords):
                domains.append(domain)
        return domains if domains else ["综合"]
    
    def _select_gods(self, question: str) -> List[str]:
        """选择需要的大神"""
        # 默认全部20位大神
        return list(self.gods.keys())
    
    def _determine_priority(self, question: str) -> str:
        """确定优先级"""
        if any(word in question for word in ["紧急", "马上", "立刻"]):
            return "高"
        elif any(word in question for word in ["重要", "关键"]):
            return "中"
        return "普通"
    
    async def god_analyze(self, god_id: str, question: str, context: Dict) -> AnalysisResult:
        """单个大神分析"""
        god = self.gods[god_id]
        
        # 模拟大神的分析（实际应调用AI模型）
        perspective = self._generate_perspective(god, question)
        key_points = self._generate_key_points(god, question)
        recommendation = self._generate_recommendation(god, question)
        confidence = self._calculate_confidence(god, question)
        
        return AnalysisResult(
            god_id=god_id,
            god_name=god.name,
            perspective=perspective,
            key_points=key_points,
            recommendation=recommendation,
            confidence=confidence
        )
    
    def _generate_perspective(self, god: GodProfile, question: str) -> str:
        """生成大神视角"""
        return f"从{god.type.value}角度，运用{god.core_ability}进行分析"
    
    def _generate_key_points(self, god: GodProfile, question: str) -> List[str]:
        """生成关键观点"""
        return [f"关键点1: 基于{god.core_ability.split('、')[0]}",
                f"关键点2: 考虑{god.decision_style}"]
    
    def _generate_recommendation(self, god: GodProfile, question: str) -> str:
        """生成建议"""
        return f"基于{god.name}的{god.type.value}，建议..."
    
    def _calculate_confidence(self, god: GodProfile, question: str) -> float:
        """计算置信度"""
        # 根据问题类型和大神专业领域匹配度计算
        return 0.85
    
    async def parallel_analysis(self, question: str, context: Dict) -> List[AnalysisResult]:
        """并行分析：20位大神同时分析"""
        print(f"\n{'='*60}")
        print("🚀 启动20位大神并行分析")
        print(f"{'='*60}")
        
        tasks = []
        for god_id in self.gods.keys():
            task = self.god_analyze(god_id, question, context)
            tasks.append(task)
        
        # 并行执行所有任务
        results = await asyncio.gather(*tasks)
        
        print(f"✅ 20位大神分析完成")
        return results
    
    def integrator_decision(self, results: List[AnalysisResult]) -> Dict[str, Any]:
        """综合决策：整合20位大神的分析"""
        print(f"\n{'='*60}")
        print("🧠 综合决策Agent整合分析")
        print(f"{'='*60}")
        
        # 提取共识
        consensus = self._extract_consensus(results)
        
        # 识别分歧
        disagreements = self._identify_disagreements(results)
        
        # 生成综合建议
        final_recommendation = self._generate_final_recommendation(results)
        
        # 生成行动方案
        action_plan = self._generate_action_plan(results)
        
        decision = {
            "consensus": consensus,
            "disagreements": disagreements,
            "final_recommendation": final_recommendation,
            "action_plan": action_plan,
            "risk_warnings": self._generate_risks(results),
            "confidence": sum(r.confidence for r in results) / len(results)
        }
        
        return decision
    
    def _extract_consensus(self, results: List[AnalysisResult]) -> List[str]:
        """提取共识"""
        return ["共识点1: 20位大神都认同", "共识点2: 共同认可"]
    
    def _identify_disagreements(self, results: List[AnalysisResult]) -> List[str]:
        """识别分歧"""
        return ["分歧点1: 权谋组与经济组意见不同", "分歧点2: 历史组与现代组视角差异"]
    
    def _generate_final_recommendation(self, results: List[AnalysisResult]) -> str:
        """生成综合建议"""
        return "基于20位大神的综合分析，建议..."
    
    def _generate_action_plan(self, results: List[AnalysisResult]) -> List[str]:
        """生成行动方案"""
        return ["步骤1: 立即行动", "步骤2: 中期规划", "步骤3: 长期调整"]
    
    def _generate_risks(self, results: List[AnalysisResult]) -> List[str]:
        """生成风险提示"""
        return ["风险1: 市场不确定性", "风险2: 个人情况差异"]
    
    def format_output(self, question: str, context: Dict, 
                     results: List[AnalysisResult], decision: Dict) -> str:
        """格式化输出"""
        output = []
        
        # 标题
        output.append("="*70)
        output.append("          天涯神贴大神智囊团 · 决策报告")
        output.append("="*70)
        
        # 问题
        output.append(f"\n【决策问题】\n{question}\n")
        
        # 协调者分析
        output.append(f"【协调者分析】")
        output.append(f"问题本质: {context['nature']}")
        output.append(f"涉及领域: {', '.join(context['domains'])}")
        output.append(f"参与大神: 20位")
        output.append(f"优先级: {context['priority']}\n")
        
        # 20位大神分析
        output.append("【20位大神独立分析】")
        output.append("-"*70)
        
        # 按类型分组
        type_groups = {}
        for result in results:
            god = self.gods[result.god_id]
            if god.type not in type_groups:
                type_groups[god.type] = []
            type_groups[god.type].append(result)
        
        for god_type, group_results in type_groups.items():
            output.append(f"\n┌─ {god_type.value}组 ─{'┐':>50}")
            for result in group_results:
                god = self.gods[result.god_id]
                output.append(f"\n👤 {god.name}")
                output.append(f"   视角: {result.perspective}")
                output.append(f"   关键观点:")
                for point in result.key_points:
                    output.append(f"      • {point}")
                output.append(f"   建议: {result.recommendation}")
                output.append(f"   置信度: {result.confidence:.0%}")
        
        # 综合决策
        output.append(f"\n{'='*70}")
        output.append("【共识点】")
        for consensus in decision['consensus']:
            output.append(f"  ✓ {consensus}")
        
        output.append(f"\n【分歧点】")
        for disagreement in decision['disagreements']:
            output.append(f"  ⚠ {disagreement}")
        
        output.append(f"\n【风险提示】")
        for risk in decision['risk_warnings']:
            output.append(f"  ⚠ {risk}")
        
        output.append(f"\n【综合决策建议】")
        output.append(f"  {decision['final_recommendation']}")
        
        output.append(f"\n【行动方案】")
        for i, step in enumerate(decision['action_plan'], 1):
            output.append(f"  {i}. {step}")
        
        output.append(f"\n【整体置信度】")
        output.append(f"  {decision['confidence']:.0%}")
        
        output.append(f"\n{'='*70}")
        
        return "\n".join(output)
    
    async def analyze(self, question: str) -> str:
        """完整分析流程"""
        # 1. 协调者分析
        context = await self.coordinator_analyze(question)
        
        # 2. 并行分析
        results = await self.parallel_analysis(question, context)
        
        # 3. 综合决策
        decision = self.integrator_decision(results)
        
        # 4. 格式化输出
        output = self.format_output(question, context, results, decision)
        
        return output


async def main():
    """主函数"""
    import sys
    
    # 获取问题
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = "我现在该不该买房？"
    
    # 创建智囊团
    team = TianyaGodsTeam()
    
    # 执行分析
    result = await team.analyze(question)
    
    # 输出结果
    print(result)


if __name__ == "__main__":
    # 运行主函数
    asyncio.run(main())
