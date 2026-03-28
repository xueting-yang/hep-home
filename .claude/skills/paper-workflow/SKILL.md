---
name: paper-workflow
description: Fetch and curate recent arXiv papers from hep-ex, hep-ph, and hep-th. Use when user asks to update paper collection, fetch recent papers, curate knowledge base, or review latest arXiv submissions. Automatically filters papers, extracts physics insights, generates study notes, and updates papers.json.
---

# Paper Workflow

自动化高能物理论文的获取、筛选、整理和知识库更新流程。

## 工作流程

```
获取最近一周论文 → AI 筛选核心文章 → 提取物理洞察 → 生成学习笔记 → 更新 papers.json
```

## 使用场景

- "更新本周的论文"
- "从 arXiv 获取最新的 hep-ex 论文"
- "帮我整理这周的高能物理文章"

## 执行步骤

### 1. 获取论文列表

从 arXiv API 获取最近 7 天的论文：
- **主要来源**: hep-ex (实验高能物理)
- **辅助来源**: hep-ph (唯象理论), hep-th (理论物理)

使用 arXiv API 查询：
```
https://export.arxiv.org/api/query?search_query=cat:hep-ex+AND+submittedDate:[YYYY-MM-DD+TO+YYYY-MM-DD]&sortBy=submittedDate&sortOrder=descending&max_results=100
```

### 2. 智能筛选与分类

从获取的论文中筛选 8-12 篇核心文章，按四大类别分类：

**类别 1: 实验 (hep-ex)**
- LHCb 实验论文（用户主要研究方向）
- 味物理：B/D 介子、CP 破坏、强子谱、稀有衰变
- 其他大型实验：ATLAS, CMS, Belle II 的重要结果

**类别 2: 理论 (hep-ph, hep-th)**
- 与味物理相关的唯象理论
- QCD、有效场论
- 标准模型精确计算

**类别 3: 软硬件技术/预研**
- 探测器技术
- 数据分析方法
- 未来实验预研

**类别 4: 相关领域**
- 宇宙学、暗物质、暗能量
- 新物理搜索（超对称、额外维度等）
- 高能天体物理（中微子天文、引力波）
- 突破性实验结果（Nature/Science 级别）

筛选优先级：
1. LHCb + 味物理（必选）
2. 突破性结果（必选）
3. 新物理搜索
4. 相关理论和技术

### 3. 提取物理洞察

对每篇筛选出的论文，生成结构化信息：

```json
{
  "title": "论文标题",
  "authors": "作者 (简化为合作组名或前 3 位作者)",
  "arxivId": "YYMM.NNNNN",
  "published": "YYYY-MM-DD",
  "experiment": "实验名称 · 加速器",
  "category": "实验|理论|技术|相关领域",
  "physics": {
    "question": "这篇论文要回答什么物理问题？(1-2 句话)",
    "result": "核心实验结果是什么？(1-2 句话)",
    "significance": "为什么这个结果重要？(1-2 句话)",
    "category": "物理分类标签"
  },
  "summary": "摘要 (保持原文或适当精简)",
  "status": "unread",
  "tags": ["自动生成的标签"],
  "addedDate": "YYYY-MM-DD"
}
```

**物理洞察生成指南**：
- `question`: 用通俗语言解释物理动机，避免过多术语
- `result`: 聚焦核心发现（观测/未观测、测量值、显著性）
- `significance`: 说明对理解自然的意义，或对标准模型的检验价值
- `category`: 如"Higgs · 顶夸克"、"新物理 · 暗物质"、"B物理 · CP破坏"

### 4. 生成学习笔记

为每篇论文创建 Markdown 笔记文件，保存到 `notes/papers/`：

**文件命名**: `notes/papers/{arxivId}.md`

**笔记模板**:
```markdown
# {title}

**arXiv**: [{arxivId}](https://arxiv.org/abs/{arxivId})
**发表日期**: {published}
**实验**: {experiment}
**状态**: 未读

## 物理问题

{physics.question}

## 核心成果

{physics.result}

## 重要意义

{physics.significance}

## 摘要

{summary}

## 学习笔记

<!-- 待补充：阅读后的理解和思考 -->

## 关键概念

<!-- 待补充：论文中的重要概念和方法 -->

## 相关论文

<!-- 待补充：关联的其他论文 -->
```

### 5. 更新 papers.json

**重要**: 保留历史数据，采用追加模式：

1. 读取现有的 `data/papers.json`
2. 将新论文追加到数组开头（最新的在前）
3. 保持文件可读性（适当的缩进和换行）
4. 备份旧版本到 `data/papers.backup.{timestamp}.json`

**不要**删除或覆盖已有的论文条目。

### 6. 输出总结

完成后，向用户报告：
- 本次获取的论文总数
- 筛选出的核心文章数量
- 新增的笔记文件列表
- papers.json 更新状态

## 脚本工具

### `scripts/fetch_arxiv.py`

从 arXiv API 获取论文元数据的 Python 脚本。

**用法**:
```bash
python scripts/fetch_arxiv.py --category hep-ex --days 7 --max-results 100
```

**输出**: JSON 格式的论文列表

### `scripts/analyze_paper.py`

使用 AI 分析论文摘要，生成物理洞察。

**用法**:
```bash
python scripts/analyze_paper.py --title "..." --abstract "..." --arxiv-id "..."
```

**输出**: 结构化的 physics 字段 JSON

## 注意事项

- arXiv API 有速率限制，请求间隔至少 3 秒
- 如遇 CORS 问题，使用代理或后端请求
- 物理洞察生成需要理解高能物理背景，确保准确性
- 保持 papers.json 的历史完整性，不要删除旧数据
- 笔记文件使用 UTF-8 编码

## 未来扩展

- 与完整知识库系统集成
- 添加论文间的关联关系
- 支持手动标注和分类
- 创建配套的 `paper-study` skill 用于深度学习
