# 从 Obsidian 到 Knowledge Base 的提炼工作流

## 提炼时机

**每周末**：集中提炼本周 inbox 内容
**项目结束**：立即提炼项目经验
**重要决策后**：当天记录决策过程

## 提炼流程

### 1. 扫描 Obsidian Inbox

打开 `obsidian-vault/00_inbox/`，检查：
- `daily/` - 本周的每日笔记
- `meetings/` - 会议记录
- `fleeting/` - 临时想法

**标记原则**：
- ⭐ 有价值，需要提炼
- ❓ 不确定，暂时保留
- ✅ 已提炼，可归档

### 2. 识别对象类型

根据内容性质，判断应该提炼成什么：

| 内容类型 | 提炼对象 | 目标位置 |
|---------|---------|---------|
| 项目进展、关键决策 | Project Dossier | `04_research_line/` |
| 论文核心理解 | Concept Note | `02_core_concepts/` |
| 方法使用经验 | Method Note | `05_toolbox/` |
| 领域全景理解 | Knowledge Map | `01_frontier_map/` |
| 简化解释 | Feynman Note | `06_feynman_lab/` |
| 重要选择 | Decision | `09_decisions/` |
| 新的思考视角 | Agent Entry | `07_agents/` |

### 3. 使用模板提炼

从 `knowledge-base/08_templates/` 选择对应模板：
- `project_template.md`
- `concept_template.md`
- `method_template.md`
- `knowledge_map_template.md`
- `feynman_template.md`
- `decision_template.md`

**提炼要点**：
- 不是复制粘贴，是重新组织
- 强调"为什么"而非"是什么"
- 包含判断和决策
- 标注理解盲点

### 4. 质量检查

提炼后的内容应该满足：

✅ **回答了核心问题**
- 不是流水账，有明确的问题导向

✅ **包含判断和决策**
- 不只是事实，有你的思考

✅ **结构清晰**
- 使用模板，易于后续查找

✅ **可复用**
- 未来遇到类似问题能直接参考

✅ **有链接**
- 与相关对象建立连接

### 5. 建立链接

在提炼的对象中添加链接：
```markdown
## 相关内容
- 使用的方法：[[method_name]]
- 相关概念：[[concept_name]]
- 所属项目：[[project_name]]
```

在相关对象中反向链接：
```markdown
## 被使用于
- [[project_name]]
```

### 6. 更新仪表盘

编辑 `knowledge-base/00_dashboard/index.md`：
- 在"最近更新"中添加本次提炼的内容
- 更新"活跃项目"状态
- 检查"当前聚焦"是否需要调整

## 低摩擦技巧

### 渐进式完善
- 第一遍：填充模板框架（20%）
- 第二遍：补充核心内容（60%）
- 第三遍：完善细节和链接（100%）

使用状态标签：
- `status: draft` - 初稿
- `status: refining` - 完善中
- `status: stable` - 稳定版本

### 批量处理
- 同类型内容一起提炼
- 使用相同模板，保持一致性
- 一次性建立链接

### 快速决策
**5 分钟规则**：如果 5 分钟内无法判断是否有价值，标记为 ❓ 下周再看

**3 次规则**：如果一个想法出现 3 次，必须提炼

## 示例：从 Daily Note 到 Decision

**Obsidian Daily Note**：
```markdown
## 遇到的问题
今天在分析中纠结要不要用 sPlot，担心 systematic 太大。
最后决定先用 sPlot 跑一版，看看 systematic 到底多大。
```

**提炼为 Decision**：
```markdown
# Decision: 使用 sPlot 进行背景扣除

## 决策背景
项目：gamma 测量
问题：需要从数据中扣除背景，但担心 sPlot 的系统误差

## 可选方案
方案 A: sPlot - 快速但可能系统误差大
方案 B: Fit - 精确但需要建模

## 选择与理由
选择：先用 sPlot
理由：快速验证分析流程，评估系统误差量级

## 实际结果
（待补充）
```

## 周末提炼 Checklist

- [ ] 扫描本周 daily notes
- [ ] 标记有价值内容
- [ ] 识别对象类型
- [ ] 使用模板提炼
- [ ] 质量检查
- [ ] 建立链接
- [ ] 更新仪表盘
- [ ] 归档已提炼的 inbox 内容
