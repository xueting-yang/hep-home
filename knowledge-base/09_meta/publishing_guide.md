# 从 Knowledge Base 发布到 Public Page

## 发布流程

1. **标记内容为 stable**
   在 knowledge-base 中，将要发布的内容状态改为 `status: stable`

2. **运行发布脚本**
   ```bash
   python scripts/publish.py
   ```

3. **推送到 GitHub**
   ```bash
   git add .
   git commit -m "Update public content"
   git push
   ```

## 发布标准

### 可发布内容
- `status: stable` 的 Concept Notes
- `status: stable` 的 Feynman Notes
- `status: stable` 的 Method Notes
- 完成的 Project Dossiers

### 不发布内容
- `status: draft` 或 `status: refining`
- Decisions（决策记录保持私有）
- 包含敏感信息的内容
- 未成熟的想法

## 发布前检查

- [ ] 移除敏感信息
- [ ] 调整语气为客观教学性
- [ ] 补充必要背景
- [ ] 确保内容完整
- [ ] 标记 `status: stable`

## 自动化

发布脚本会：
1. 扫描 knowledge-base 中 `status: stable` 的内容
2. 生成 `data/knowledge.json` 索引
3. 复制文件到 public page

## 维护

- Private 版本标注：`public_version: /knowledge/xxx`
- Public 版本标注：`private_source: /knowledge-base/xxx`
- 定期同步更新
