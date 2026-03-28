# Obsidian 工作层

这是三层知识系统的第一层：日常工作层。

## 目录结构

```
00_inbox/          # 收件箱：所有新内容的入口
  ├── daily/       # 每日笔记
  ├── meetings/    # 会议记录
  └── fleeting/    # 临时想法

01_projects/       # 项目笔记（如 gamma 测量）

02_papers/         # 论文阅读笔记
  └── 2026/        # 按年份组织

03_concepts/       # 概念笔记

04_code/           # 代码片段

05_questions/      # 待解决问题
```

## 工作流程

1. **每日开始**：使用 `daily-note` 模板创建当天笔记
2. **阅读论文**：使用 `paper-quick-read` 模板快速记录
3. **项目进展**：使用 `project-note` 模板跟踪项目
4. **会议记录**：使用 `meeting-note` 模板
5. **周末复盘**：使用 `weekly-review` 模板

## 精炼流程

- 每周从 inbox 中提取有价值的内容
- 精炼后的内容进入 `knowledge-base/`（私人知识库）
- 最终输出到 `hep-home/`（公开展示）

## 模板使用

所有模板位于 `templates/` 目录，在 Obsidian 中可通过模板插件快速插入。
