#!/usr/bin/env python3
"""
从 knowledge-base 发布内容到 hep-home (public page)
"""

import json
import os
import shutil
from pathlib import Path
from datetime import datetime

KB_ROOT = Path(__file__).parent.parent / "knowledge-base"
PUBLIC_ROOT = Path(__file__).parent.parent
PUBLIC_DATA = PUBLIC_ROOT / "data"
PUBLIC_KNOWLEDGE = PUBLIC_ROOT / "knowledge"

def load_frontmatter(file_path):
    """提取 markdown 文件的 frontmatter"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return {}, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content

    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter, parts[2].strip()

def should_publish(file_path):
    """检查文件是否应该发布"""
    meta, _ = load_frontmatter(file_path)
    status = meta.get('status', 'draft')
    return status == 'stable'

def publish_knowledge():
    """发布知识库内容"""
    PUBLIC_KNOWLEDGE.mkdir(exist_ok=True)

    published = []

    # 发布 Concept Notes
    concepts_dir = KB_ROOT / "02_core_concepts"
    if concepts_dir.exists():
        for concept_file in concepts_dir.rglob("*.md"):
            if should_publish(concept_file):
                meta, content = load_frontmatter(concept_file)
                rel_path = concept_file.relative_to(concepts_dir)

                published.append({
                    "type": "concept",
                    "title": meta.get('concept', rel_path.stem),
                    "path": f"knowledge/concepts/{rel_path}",
                    "category": "核心概念"
                })

    # 发布 Feynman Notes
    feynman_dir = KB_ROOT / "06_feynman_lab"
    if feynman_dir.exists():
        for feynman_file in feynman_dir.rglob("*.md"):
            if should_publish(feynman_file):
                meta, content = load_frontmatter(feynman_file)
                rel_path = feynman_file.relative_to(feynman_dir)

                published.append({
                    "type": "feynman",
                    "title": meta.get('topic', rel_path.stem),
                    "path": f"knowledge/feynman/{rel_path}",
                    "category": "费曼讲解"
                })

    # 发布 Method Notes
    methods_dir = KB_ROOT / "05_toolbox"
    if methods_dir.exists():
        for method_file in methods_dir.rglob("*.md"):
            if should_publish(method_file):
                meta, content = load_frontmatter(method_file)
                rel_path = method_file.relative_to(methods_dir)

                published.append({
                    "type": "method",
                    "title": meta.get('method', rel_path.stem),
                    "path": f"knowledge/methods/{rel_path}",
                    "category": "方法工具"
                })

    # 保存索引
    PUBLIC_DATA.mkdir(exist_ok=True)
    with open(PUBLIC_DATA / "knowledge.json", 'w', encoding='utf-8') as f:
        json.dump(published, f, ensure_ascii=False, indent=2)

    print(f"✓ 发布了 {len(published)} 个知识条目")
    return published

def main():
    print("开始发布到 public page...")
    publish_knowledge()
    print("✓ 发布完成")

if __name__ == "__main__":
    main()
