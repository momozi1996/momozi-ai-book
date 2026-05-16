# 天涯神贴大神智囊团 - OpenClaw安装指南

## 安装方法

### 方法1: 直接复制到OpenClaw Skill目录

```bash
# 1. 复制文件夹到OpenClaw Skill目录
cp -r ~/Downloads/tianya-gods-framework ~/.stepclaw/workspace/.agents/skills/

# 2. 重命名为标准格式（可选）
mv ~/.stepclaw/workspace/.agents/skills/tianya-gods-framework \
   ~/.stepclaw/workspace/.agents/skills/tianya-gods-team

# 3. 验证安装
ls ~/.stepclaw/workspace/.agents/skills/tianya-gods-team/
```

### 方法2: 使用install.sh自动安装

```bash
cd ~/Downloads/tianya-gods-framework
bash install.sh
```

## 使用方法

安装完成后，在OpenClaw中使用以下触发词：

```
「启动天涯智囊团」我现在该不该买房？
「召集大神」该选择体制内还是体制外？
「20位大神分析」如何分析当前的职场困境？
```

## 文件结构

```
~/.stepclaw/workspace/.agents/skills/tianya-gods-team/
├── SKILL.md              # 主文件（必须符合OpenClaw格式）
├── README.md             # 说明文档
├── references/           # 参考资料
│   └── research/
│       ├── 01-writings.md
│       ├── 02-conversations.md
│       ├── 03-expression-dna.md
│       ├── 04-external-views.md
│       ├── 05-decisions.md
│       └── 06-timeline.md
└── scripts/              # 可选：脚本文件
    ├── __init__.py
    └── team-orchestrator.py
```

## 注意事项

1. **SKILL.md 必须放在根目录**，这是OpenClaw识别Skill的关键
2. **SKILL.md 必须包含 frontmatter**（--- 开头的元数据）
3. **name字段**用于触发词匹配
4. **description字段**用于Skill描述和触发条件
5. **type: skill** 表示这是一个Skill文件

## GitHub发布

如果要发布到GitHub供他人使用：

1. 创建GitHub仓库
2. 上传整个文件夹
3. 在README中提供安装说明
4. 用户下载后按上述方法安装

## 触发词说明

本Skill支持以下触发词：

- `「启动天涯智囊团」` — 启动完整分析
- `「召集大神」` — 召集大神分析
- `「20位大神分析」` — 20位大神并行分析
- `「天涯智囊团」` — 简写触发

## 依赖

- Python 3.7+（用于运行scripts中的脚本）
- asyncio（Python标准库）

## 测试

```bash
cd ~/.stepclaw/workspace/.agents/skills/tianya-gods-team
bash test.sh
```
