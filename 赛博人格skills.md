# AI 赛博人格蒸馏技能（Skill）完整汇总表

# AI 赛博人格蒸馏技能库
一份全网最全、持续更新的 **AI 人格蒸馏 Skill 合集**，覆盖7大场景，全部为可直接导入使用的开源 Agent Skill：
1. **自我蒸馏**  ；  **职场关系**
2.  **名人思维** ；  **情感陪伴** 
3. **玄学术数**  ；  **二次元角色**
4. **SBTI人格测试**

<img width="1000" height="558" alt="Gemini_Generated_Image_gaz0fggaz0fggaz0_副本" src="https://github.com/user-attachments/assets/a5ecb800-3123-4ff2-bd24-f12b770d5ada" />

## 文档介绍
本文档整理并收录当前互联网主流 **Persona Distill Skills**，所有项目均来自 GitHub 开源社区，按场景清晰分类、附带完整项目地址，方便快速查找、安装与使用。

你可以用它：
- 一键复刻名人思维框架
- 蒸馏自己/亲友/同事的数字人格
- 搭建情感陪伴、回忆疗愈AI
- 做职业规划、升学咨询、内容创作助手
- 体验二次元角色、玄学测算等特色Skill

所有技能遵循 **AgentSkills 规范**，支持 Claude Code / Cursor / OpenClaw 等主流平台直接使用。


---

# 怎么赛博蒸馏skill?
### 某博主的指南

[文档链接：赛博蒸馏skill实操指南pdf](https://github.com/momozi1996/momozi-ai-book/blob/main/%E8%B5%9B%E5%8D%9A%E8%92%B8%E9%A6%8FSkill%E5%AE%9E%E6%93%8D%E6%8C%87%E5%8D%97.pdf)

### 我自己的经验

1、安装女娲skill：
```bash
npx skills add alchaincyf/nuwa-skill
```

2、利用女娲skill蒸馏其他人物
```bash
非常好，用nuwa-skill蒸馏另一个作家-莫言， 我希望你能先查他的所有资料和书写风格尤其是小说的书写， 构造一个最像他的。
```
3、等待openclaw完成任务。（我自己用的阶跃AI的stepclaw）
 stepclaw也会一步一步执行，执行完成以后会向用户反馈结果。。
 
4、保存压缩包到本地
```bash
把这个 莫言Skill 相关的文件，做成文件夹保存到我的电脑本地的下载的目录里吧。 （检查所有的文件不要出错，也不要为空）
```

# 完整 Skill 清单文档

---

## 一、自我蒸馏 & 元工具 & 特殊技能
| Skill 名称 | 核心功能 | 项目地址 |
| --- | --- | --- |
| 女娲.skill | 通用人格蒸馏工具，自动提炼任何人的心智与表达 | https://github.com/alchaincyf/nuwa-skill |
| 自己.skill | 蒸馏自身语料，打造数字分身与第二大脑 | https://github.com/notdog1998/yourself-skill |
| 蒸馏.skill | 人格蒸馏引擎，支持自己/亲友/他人角色构建 | https://github.com/YIKUAIBANZI/forge-skill |
| 反蒸馏.skill | 技能文档“投毒”，核心知识自留，打工人自保 | https://github.com/leilei926524-tech/anti-distill |
| 图鉴.skill | Skill 调度器，按意图智能推荐角色 | https://github.com/Aar0nPB/curator-skill |
| 数字人生.skills | 从数字痕迹提炼结构化自我画像 | https://github.com/wildbyteai/digital-life |
| 永生.skill | 多维人格蒸馏，实现数字永生 | https://github.com/agenmod/immortal-skill |
| midas.skill | 财富模型蒸馏，挖掘个人财富信号 | https://github.com/realteamprinz/midas-skill |
| 数字生命开源计划 | 个人知识库 → 数字分身框架 | https://github.com/weixr18/my-digital-life |

---


## 二、职场 & 自媒体系列
| Skill 名称 | 核心功能 | 项目地址 |
| --- | --- | --- |
| 同事.skill | 蒸馏真实同事的沟通风格与协作习惯，生成 AI 同事 | https://github.com/titanwings/colleague-skill |
| 老板.skill | 提炼老板决策逻辑、评审风格，解放自身生产力 | https://github.com/vogtsw/boss-skills |
| 博主.skill | 基于社媒语料生成可对话自媒体人格 | https://github.com/YourongZhou/chat_with_me |
| X导师.skill | Twitter/X 运营导师，推文写作与账号诊断 | https://github.com/alchaincyf/x-mentor-skill |
| HR.skill | 从招聘流程反向拆解 HR 筛选与决策模式 | https://github.com/Schlaflied/hr-skill |
| 大学老师.skill | 提炼教学风格、评分逻辑、复习重点与出题偏好 | https://github.com/CommitHu502Craft/professor-skill |
| 导师.skill | 学术导师指导风格、研究偏好与评审逻辑 |https://github.com/ybq22/supervisor|
| 师兄.skill | 课题组师兄技术风格、解题思路与指导方式 | https://github.com/zhanghaichao520/senpai-skill |
| 户晨风.skill | 消费现实主义视角，职业/城市分析 | https://github.com/Janlaywss/hu-chenfeng-skill |
| VibePortrait | 从对话提炼开发者风格与技术偏好 | https://github.com/dadwadw233/VibePortrait |

---

## 三、名人思维系列
| Skill 名称 | 核心功能 | 项目地址 |
| --- | --- | --- |
| 乔布斯.skill | 产品审美、现实扭曲力场、演讲与决策风格 | https://github.com/alchaincyf/steve-jobs-skill |
| 马斯克.skill | 第一性原理、极致执行力、推文与战略思维 | https://github.com/alchaincyf/elon-musk-skill |
| 芒格.skill | 多元思维模型、反向思考、投资决策框架 | https://github.com/alchaincyf/munger-skill |
| 费曼.skill | 极简讲解、复杂问题拆解、高效学习法 | https://github.com/alchaincyf/feynman-skill |
| 纳瓦尔.skill | 财富逻辑、幸福哲学、杠杆与判断力框架 | https://github.com/alchaincyf/naval-skill |
| 塔勒布.skill | 黑天鹅、反脆弱、风险与不确定性判断 | https://github.com/alchaincyf/taleb-skill |
| 张一鸣.skill | 算法思维、产品迭代、延迟满足与管理哲学 | https://github.com/alchaincyf/zhang-yiming-skill |
| 张雪峰.skill | 升学志愿、职业规划、接地气建议与吐槽 | https://github.com/alchaincyf/zhangxuefeng-skill |
| Paul Graham.skill | 创业、写作、独立思考与产品哲学 | https://github.com/alchaincyf/paul-graham-skill |
| Karpathy.skill | AI 教学、工程直觉、深度学习实践思维 | https://github.com/alchaincyf/karpathy-skill |
| Ilya Sutskever.skill | AGI 认知、模型哲学、对齐与前沿判断 | https://github.com/alchaincyf/ilya-sutskever-skill |
| MrBeast.skill | 爆款逻辑、病毒传播、短视频内容创作 | https://github.com/alchaincyf/mrbeast-skill |
| 特朗普.skill | 谈判风格、舆论话术、权力博弈思维 | https://github.com/alchaincyf/trump-skill |
| 毛泽东.skill | 战略判断、矛盾分析、调查研究方法论 | https://github.com/wwwaapplleecu-source/mao-skill |
| 毛选.skill | 实事求是、群众路线、根据地思维 | https://github.com/leezythu/maoxuan-skill |
| 新青年.Skill | 蒸馏毛选全文，形成现实分析与决策技能 | https://github.com/SamadhiFire/xinqingnian-skill |
| 郭德纲.skill | 语言结构、幽默表达、人情世故判断 | https://github.com/ByteRax/guodegang-skills |
| 峰哥亡命天涯 Skill | 现实主义、止损思维、黑色幽默表达 |https://github.com/rottenpen/fengge-wangmingtianya-perspective|
| 宝玉 baoyu-skills | 宝玉分享的 Claude Code 技能集，提升日常工作效率。 | https://github.com/JimLiu/baoyu-skills/blob/main/README.zh.md |


---

## 四、亲密关系 & 生活系列
| Skill 名称 | 核心功能 | 项目地址 |
| --- | --- | --- |
| 前任.skill | 蒸馏前任语气与共同记忆，模拟对话 | https://github.com/therealXiaomanChu/ex-skill |
| 父母.skill | 提炼亲人语气、习惯与家庭记忆 | https://github.com/xiaoheizi8/parents-skills |
| MamaSkill | 基于语音与聊天构建家人陪伴 AI | https://github.com/jiangziyan-693/MamaSkill |
| 兄弟.skill | 蒸馏好友说话风格、口头禅与社交模式 | https://github.com/realteamprinz/brother-skill |
| 暗恋对象.skill | 从聊天记录模拟对话风格，用于情感练习 | https://github.com/xiaoheizi8/crush-skills |
| 恋爱训练营.skill | 模拟心动对象，练习表达、邀约与沟通 | https://github.com/TammyTan516/relationship-training-skill |
| Reunion Skill | 基于数字遗物构建已故亲友纪念型 AI | https://github.com/yangdongchen66-boop/reunion-skill |

---

## 五、传统 & 玄学 & 术数系列
| Skill 名称 | 核心功能 | 项目地址 |
| --- | --- | --- |
| 华夏老祖宗.skill | 华夏老祖宗智慧：老祖宗指出你的认知偏差，直接给融合方案，还带口音——34个框架，每个都有独特的分析方法和专属口吻：| https://github.com/liangjfblue/huaxia-wisdom |
| 赛博算命.skill | 八字排盘、四柱命理、运势分析 | https://github.com/jinchenma94/bazi-skill |
| 月老·姻缘测算.skill | 术数合婚、桃花分析、姻缘测算 | https://github.com/Ming-H/yinyuan-skills |
| 奇门遁甲、紫微斗数.skill | 低幻觉排盘，传统术数 AI 分析 | https://github.com/FANzR-arch/Numerologist_skills |
| 大师.skill | 汉传佛教祖师大德风格讲解与对话 | https://github.com/xr843/Master-skill |
| 金刚经.skill | 基于金刚经的讲解、对话与解读框架 |https://github.com/dull-bird/diamond-sutra-skill |
| 🎭 七情六欲.skill | AI 七情六欲增强 Skill — 让 AI 拥有类人的情感、观点和人格 | https://github.com/Lniosy/qiqing-liuyu |

>**七情**出自《礼记·礼运》："何谓人情？喜、怒、哀、惧、爱、恶、欲，七者弗学而能。"意思是这七种情感不用学就会，是人的本能。**六欲**出自佛家"六根"——眼、耳、鼻、舌、身、意，指人与世界交互的六种感官通道，也是六种欲望的来源。


---

## 六、二次元 & 主播系列
| Skill 名称 | 核心功能 | 项目地址 |
| --- | --- | --- |
| 永雏塔菲.skill | 一键成为永雏塔菲， 学会包括经典的喵喵句尾、专注 RP（RolePlay）的 taffy 自称等等细节；像塔菲一样聊天、发微博，给视频起标题，给动态写文案。同时，得利于对永雏塔菲用词习惯的蒸馏，我们显著提升了永雏塔菲切片视频中的语音识别正确率。 | https://github.com/ly-xxx/ace-taffy-skill |
|  Waifu-Skill | Waifu-Skill 是一个"反向异世界"系统——不是你穿越到二次元，而是把二次元角色召唤到现实。能够从小说、设定集等原材料中提取虚拟角色的人格特征和世界观设定，生成可对话的AI Skill。| https://github.com/miunasu/waifu-skill |
| lolimom.skill | 你喜欢的二次元软萌妈妈气质，蒸馏成一个会哄你、会照顾你、会记住你习惯的 AI Skill。 |https://github.com/yuuiwa1551/lolimom.skill|
| vtb.skill · 虚拟主播.skill |把喜欢过、追过、想认真留下来的虚拟主播，整理成一个能安装、能维护、还能继续补料的 .skill | https://github.com/ly-xxx/vtb.skill |
| 陈泽.skill |基于斗鱼/抖音主播 陈泽 真实语料蒸馏，涵盖身份认知、价值观、表达风格、幽默模式、互动规则五大维度。| https://github.com/Xiaooooo434680/chenze-skill |

## 七、夺舍 系列
| Skill 名称 | 核心功能 | 项目地址 |
| --- | --- | --- |
| 夺舍.skill | AI夺舍角色灵魂，让TA在你面前活过来。有官方Wiki的游戏都能夺舍。 | https://github.com/Summer907/possession-skill |

>支持哪些游戏？简单来说：有官方Wiki的游戏都行。
>想扮演芙宁娜？夺舍她。让AI用她的灵魂和你说话。想扮演钟离？夺舍他。让AI用「欲买桂花同载酒」的沧桑回应你。想扮演自己喜欢的角色？现在就能夺舍。
>想和喜欢的角色聊天？夺舍TA。想写同人但拿不准人设？夺舍TA。想做个角色扮演机器人？夺舍TA。想让自己写的角色更立体？——也可以夺舍自己写的人。
>只要能获取角色的官方设定、语音台词、背景故事，就能夺舍。
>支持哪些游戏？简单来说：有官方Wiki的游戏都行。
游戏	Wiki来源	状态
🌟原神	： 萌娘百科 / BWIKI / Fandom        	✅ 已支持
🚄崩坏：星穹铁道	： 萌娘百科 / BWIKI / Fandom	✅ 已支持
🔫三角洲行动	： BWIKI / 萌娘百科            	✅ 已支持
🎮其他	：手动提供Wiki链接                  	📋 待扩展
只要能获取角色的官方设定、语音台词、背景故事，就能夺舍。


---

## 八、测试系列
| Skill 名称 | 核心功能 | 项目地址 |
| --- | --- | --- |
|🧠 SBTI 赛博人格测试 Skill| 互联网最火的沙雕人格测试，现在可以在你的 AI agent 里玩了。30 道题，15 个维度，27 种人格 — 测自己，或者测你的龙虾 🦞 | https://github.com/nexu-io/sbti-skill |

---

### 说明
- 无地址项为原 awesome 仓库收录但未附外链，可 GitHub 直接搜 Skill 名称查找
- 全部遵循 Skill 流规范，可直接导入支持 Agent Skill 的 AI 平台使用
