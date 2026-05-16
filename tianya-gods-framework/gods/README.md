# 天涯神贴大神单独Skill文件

本目录包含20位天涯大神的单独Skill文件，每个文件都可以作为独立的OpenClaw Skill使用。

## 文件列表

### 已创建的大神Skill

1. **dapeng-jinchimingwang.md** - 大鹏金翅明王（权谋分析）
2. **kkndme.md** - KKNDME（经济预言）
3. **dangnianmingyue.md** - 当年明月（历史解读）
4. **ningcaishen.md** - 宁财神（文化解构）
5. **murongxuecun.md** - 慕容雪村（都市情感）

### 待创建的大神Skill

6. **chanshuozhongchan.md** - 缠中说禅（技术分析）
7. **kongergou.md** - 孔二狗（黑帮江湖）
8. **tianxiabachang.md** - 天下霸唱（盗墓探险）
9. **nanpaisanshu.md** - 南派三叔（盗墓探险）
10. **yanleisheng.md** - 燕垒生（玄幻武侠）
11. **jinheza.md** - 今何在（西游解构）
12. **jiangnan.md** - 江南（青春幻想）
13. **maoni.md** - 猫腻（权谋玄幻）
14. **fenghuoxizhuhou.md** - 烽火戏诸侯（武侠玄幻）
15. **xiaoqixiao.md** - 骁骑校（都市异能）
16. **zhouhaohui.md** - 周浩晖（悬疑推理）
17. **leimi.md** - 雷米（心理犯罪）
18. **fayiqinming.md** - 法医秦明（法医刑侦）
19. **yueguan.md** - 月关（历史穿越）
20. **jieyu2.md** - 孑与2（历史穿越）

## 使用方法

### 单独使用某位大神

```bash
# 复制某位大神的Skill到OpenClaw目录
cp dapeng-jinchimingwang.md ~/.stepclaw/workspace/.agents/skills/

# 在OpenClaw中使用触发词
「大鹏金翅明王视角」分析这个权力结构
```

### 批量使用所有大神

```bash
# 复制所有大神Skill到OpenClaw目录
cp *.md ~/.stepclaw/workspace/.agents/skills/
```

## 文件格式

每个大神Skill文件遵循OpenClaw标准格式：

```yaml
---
name: [大神名]-perspective
description: |
  [描述]
  触发词：「[触发词]」
  擅长：[擅长领域]
type: perspective
author: 女娲 · Skill造人术
created: 2026-04-28
---

# [大神名] · [思维类型]

> [经典语录]

## 身份卡
...

## 回答工作流
...

## 心智模型
...

## 表达DNA
...
```

## 批量生成脚本

如需批量生成剩余大神的Skill文件，可以使用以下脚本：

```python
# generate_gods.py
# 批量生成大神Skill文件

gods = [
    ("chanshuozhongchan", "缠中说禅", "技术分析", "技术分析、市场规律、走势预测"),
    ("kongergou", "孔二狗", "黑帮江湖", "江湖规则、人情世故、社会边缘"),
    # ... 其他大神
]

for god_id, name, type, abilities in gods:
    # 生成Skill文件
    pass
```

## 注意事项

1. 每个Skill文件都是独立的，可以单独使用
2. 触发词在description中定义
3. 所有Skill都遵循相同的格式规范
4. 可以单独更新某位大神的Skill

## 更新日志

- 2026-04-28: 创建前5位大神Skill
- 待续: 创建剩余15位大神Skill
