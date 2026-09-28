# FormaMark · 形符引擎

将自有亚马逊商品的视觉拆成可复用的**版型 + 符号**，再基于新主题、文字或参考图片设计新主图和副图。

## 能做什么

- **视觉蒸馏**：查看可访问的商品主副图、A+ 与用户素材，生成版型文字/图片、符号文字/图片、可复用提示词和独立复现记录。
- **主题再创作**：保留已核对的产品结构，替换图案与文案；先交新主图供用户确认，再规划并生成副图。
- **质量门槛**：独立复现需通过事先确定的硬门槛，且人工视觉量表评分严格 **≥90/100**；达不到时保留草稿和偏差记录。

当前不包含 A+ 新页面创作。实际生图需要 Codex 环境提供图片生成及独立子代理能力。

## 安装

在 Codex 中输入：

```text
使用 $skill-installer，从 https://github.com/dreambird25/amazon-product-visual-distillation/tree/main/skills/amazon-product-visual-distillation 安装这个 Skill。
```

Skill 的完整说明见 [SKILL.md](skills/amazon-product-visual-distillation/SKILL.md)。

## 开始使用

```text
使用 $amazon-product-visual-distillation，蒸馏我的自有商品 ASIN：<ASIN>。
```

```text
基于刚才确认的版型，把新款改成：<主题描述或附图>。先出主图给我确认，确认后再做副图。
```

你通常只需提供原商品 ASIN 和新款创意；若前台资料不可访问、相互冲突或缺失关键事实，Codex 会就必要内容提问。
