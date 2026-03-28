# Private to Public 转换指南

## 边界原则

### 保留 Private

**失败与教训**
- 分析中的错误尝试
- 未成功的方法
- 个人判断失误

**未成熟想法**
- 正在探索的方向
- 不确定的猜测
- 需要验证的假设

**敏感信息**
- 导师/合作者的私人讨论
- 竞争敏感的研究方向
- 未发表的实验结果

**个人性内容**
- 情绪化的记录
- 纯个人的反思
- 学习过程中的困惑

### 可转 Public

**成熟的理解**
- 经过验证的概念理解
- 完整的 Feynman Note
- 清晰的物理图像

**通用工具**
- 可复用的分析方法
- 有价值的代码工具
- 实用的工作流程

**完成的项目**
- 已发表的工作
- 完整的项目档案
- 可展示的成果

**教学价值**
- 精炼的 Knowledge Map
- 系统的概念讲解
- 有启发的思考框架

## 转换流程

### 1. 评估成熟度

**内容完整性**
- [ ] 逻辑完整，无明显漏洞
- [ ] 经过验证，不是猜测
- [ ] 有足够的背景说明

**表达清晰度**
- [ ] 语言清晰，易于理解
- [ ] 结构合理，便于阅读
- [ ] 无需过多前置知识

**价值判断**
- [ ] 对他人有参考价值
- [ ] 不是纯个人化的内容
- [ ] 愿意公开讨论

### 2. 内容改写

**去除敏感信息**
- 删除私人讨论
- 模糊化具体时间/人物
- 移除未发表数据

**调整语气**
- 从"我的困惑"改为"常见困惑"
- 从"我的理解"改为"一种理解"
- 保持客观和教学性

**补充背景**
- 添加必要的前置知识
- 解释专业术语
- 提供参考资料

### 3. 格式转换

**Private 格式**（knowledge-base）
- 个人化的记录
- 详细的思考过程
- 包含失败和困惑

**Public 格式**（hep-home）
- 精炼的展示
- 核心的洞察
- 突出价值和成果

## 转换示例

### Concept Note: Private → Public

**Private 版本**：
```markdown
# Direct CP Violation

## 我的理解
一开始我以为 direct CPV 就是衰变振幅不同，
后来发现还要考虑 strong phase...

## 理解盲点
- 为什么需要 strong phase？
- 和 mixing 的区别在哪？
```

**Public 版本**：
```markdown
# Direct CP Violation

## 核心概念
Direct CPV 发生在衰变过程本身，
表现为粒子和反粒子的衰变振幅不同。

## 物理图像
需要两个条件：
1. Weak phase（来自 CKM 矩阵）
2. Strong phase（来自末态相互作用）

## 常见困惑
Q: 为什么需要 strong phase？
A: 只有 weak phase 会被复共轭抵消...
```

### Project Dossier: Private → Public

**Private 版本**：
```markdown
# Gamma 测量项目

## 失败尝试
- 试过用 method A，systematic 太大放弃了
- 和导师讨论后决定换 method B
- 第一版代码有 bug，浪费了两周...
```

**Public 版本**：
```markdown
# Gamma 测量项目

## 项目概述
使用 B → DK 衰变测量 CKM 角 gamma

## 方法选择
采用 GLW 方法，因为：
- 理论清晰
- 系统误差可控
- 适合当前数据量
```

## 转换 Checklist

- [ ] 评估内容成熟度
- [ ] 移除敏感信息
- [ ] 调整语气和表达
- [ ] 补充必要背景
- [ ] 格式转换
- [ ] 在 hep-home 创建对应文件
- [ ] 在 private 版本中标注"已公开"
- [ ] 保持两个版本的链接

## 维护策略

**双向链接**
- Private 版本标注：`public_version: /hep-home/xxx`
- Public 版本标注：`private_source: /knowledge-base/xxx`

**更新同步**
- Private 版本更新后，评估是否需要同步到 Public
- Public 版本收到反馈后，补充到 Private

**版本控制**
- Private 版本可以持续迭代
- Public 版本保持稳定，重大更新时标注版本号
