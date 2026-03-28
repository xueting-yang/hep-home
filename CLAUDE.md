# Xueting's HEP HOME

高能物理学习与研究的个人知识库网站。

## 项目概述

这是一个展示高能物理学习历程、研究笔记和 arXiv 论文追踪的个人站点。

**核心功能**：
- 展示个人项目和作业
- 每日推荐 HEP-EX 领域论文
- 论文知识库管理
- 学习笔记整理

## 项目结构

```
.
├── index.html          # 主页
├── style.css           # 样式
├── app.js              # 前端逻辑
├── data/
│   ├── projects.json   # 项目列表
│   └── papers.json     # 论文知识库
├── notes/
│   └── papers/         # 论文学习笔记 (Markdown)
└── .claude/
    └── skills/
        ├── paper-workflow/   # 论文工作流 Skill
        └── pdf-to-video/     # PDF 转视频 Skill
```

## 技术栈

- 纯静态站点 (HTML + CSS + JavaScript)
- arXiv API 集成
- GitHub Pages 部署

## 工作流

### 论文更新流程

使用 `paper-workflow` Skill 自动化处理：

1. **获取论文**: 从 arXiv 获取 hep-ex/hep-ph/hep-th 最近一周的论文
2. **智能筛选**: AI 筛选出 5-10 篇核心文章
3. **提取洞察**: 自动生成物理问题/核心成果/重要意义
4. **生成笔记**: 创建 Markdown 学习笔记模板
5. **更新展示**: 追加到 papers.json，保留历史数据

**触发命令**：
```
更新本周的论文
从 arXiv 获取最新的 hep-ex 论文
```

### 数据结构

**papers.json** 格式：
```json
{
  "title": "论文标题",
  "authors": "作者",
  "arxivId": "YYMM.NNNNN",
  "published": "YYYY-MM-DD",
  "experiment": "实验名称 · 加速器",
  "physics": {
    "question": "物理问题",
    "result": "核心成果",
    "significance": "重要意义",
    "category": "分类标签"
  },
  "summary": "摘要",
  "status": "unread/read/noted",
  "tags": ["标签"],
  "addedDate": "YYYY-MM-DD"
}
```

## 开发指南

### 本地运行

```bash
# 启动本地服务器
python -m http.server 8000
# 访问 http://localhost:8000
```

### 更新论文库

```bash
# 使用 paper-workflow skill
# 在 Claude 中输入：更新本周的论文
```

### 添加新项目

编辑 `data/projects.json`：
```json
{
  "title": "项目名称",
  "description": "项目描述",
  "url": "项目链接",
  "date": "2026-03",
  "status": "done/wip"
}
```

## Skills

### paper-workflow
自动化论文获取、筛选、整理流程。

**功能**：
- 从 arXiv 获取最新论文
- AI 筛选核心文章
- 生成物理洞察和学习笔记
- 更新 papers.json

### pdf-to-video
将 PDF 文档转换为展示视频。

## 研究方向

- CKM 角 gamma 测量
- B 介子物理
- CP 破坏
- LHCb 实验

## 部署

推送到 GitHub 后自动部署到 GitHub Pages。

## 注意事项

- papers.json 采用追加模式，不删除历史数据
- 论文笔记保存在 notes/papers/
- arXiv API 请求需遵守速率限制
- 使用代理解决 CORS 问题
