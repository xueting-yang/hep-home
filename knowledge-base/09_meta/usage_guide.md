# Knowledge Base 使用指南

## 三层知识系统

```
Obsidian (工作层)
    ↓ 周末提炼
Knowledge Base (产出层 / Private)
    ↓ 选择性转换
HEP Home (展示层 / Public)
```

## 日常工作流

### 每日
1. 在 `obsidian-vault/00_inbox/daily/` 创建当日笔记
2. 记录工作进展、遇到的问题、新的想法
3. 会议用 `meeting-note` 模板
4. 临时想法放 `fleeting/`

### 每周
1. 周末打开 `refinement_workflow.md`
2. 扫描本周 inbox，标记有价值内容
3. 使用模板提炼到 knowledge-base
4. 更新 `00_dashboard/index.md`
5. 归档已提炼的内容

### 每月
1. 回顾 `current_focus.md`，调整重点
2. 检查活跃项目进展
3. 评估是否有内容可转 public

## 对象类型速查

| 我想记录... | 使用对象 | 模板 | 位置 |
|-----------|---------|------|------|
| 项目经验 | Project Dossier | project_template | 04_research_line/ |
| 领域全景 | Knowledge Map | knowledge_map_template | 01_frontier_map/ |
| 核心概念 | Concept Note | concept_template | 02_core_concepts/ |
| 分析方法 | Method Note | method_template | 05_toolbox/ |
| 简化讲解 | Feynman Note | feynman_template | 06_feynman_lab/ |
| 重要决策 | Decision | decision_template | 09_decisions/ |
| 论文理解 | Paper Note | paper_reading_template | 03_papers/ |

## 快速开始

### 场景 1：开始新项目
1. 在 `04_research_line/` 创建项目文件夹
2. 使用 `project_template.md` 创建 `overview.md`
3. 在 `00_dashboard/index.md` 添加到"活跃项目"

### 场景 2：理解新概念
1. 在 `02_core_concepts/` 对应分类下创建文件
2. 使用 `concept_template.md`
3. 尝试用 `feynman_template.md` 简化讲解

### 场景 3：学习新方法
1. 在 `05_toolbox/` 对应分类下创建文件
2. 使用 `method_template.md`
3. 记录"什么时候用""什么时候不用"

### 场景 4：做重要决策
1. 在 `09_decisions/` 创建文件
2. 使用 `decision_template.md`
3. 记录背景、方案、理由
4. 事后更新结果和反思

## 核心原则

1. **最小单元是"问题"**
   - 不要创建"CKM 矩阵"这样的大主题
   - 而是"为什么 CKM 矩阵是酉矩阵"

2. **记录判断和决策**
   - 不只是"用了 sPlot"
   - 而是"为什么选 sPlot 而不是 Fit"

3. **使用统一模板**
   - 保持结构一致
   - 便于查找和维护

4. **持续迭代**
   - 允许 draft 状态
   - 渐进式完善

## 常见问题

**Q: 什么内容值得提炼？**
A: 符合以下任一条件：
- 花了很多时间理解的
- 做了重要决策的
- 失败了但有教训的
- 未来可能复用的

**Q: 提炼要多详细？**
A: 遵循"6 个月后的自己能看懂"原则

**Q: 如何避免知识库失控？**
A:
- 严格使用模板
- 定期清理 draft
- 合并重复内容

**Q: Private 和 Public 如何选择？**
A: 参考 `private_to_public.md`

## 相关文档

- [提炼工作流](refinement_workflow.md)
- [Private to Public 转换](private_to_public.md)
- [知识库哲学](knowledge_philosophy.md)
