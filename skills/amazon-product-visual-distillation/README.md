# FormaMark · 形符引擎

技术标识：`amazon-product-visual-distillation`

这是一个 Codex Skill。请将整个 `amazon-product-visual-distillation` 文件夹安装到当前用户的 `.agents/skills` 下，使 `SKILL.md`、`references/`、`scripts/` 位于同一层级。不要只复制 `SKILL.md`。

可直接把本 RAR 交给本地 Codex，并说：

> 请安装压缩包中的 amazon-product-visual-distillation Skill 到我当前用户的 .agents/skills 目录，核对 SKILL.md、references/ 和 scripts/ 都存在，然后告诉我安装结果。

使用示例：

> 使用 $amazon-product-visual-distillation，蒸馏我的自有商品 ASIN：<填写 ASIN>。
>
> 基于刚才确认的版型，把新款改成：<主题描述或附图>。先出主图给我确认，确认后再做副图。

本包为独立 Skill，不含案例产品的源图或已生成图片。实际生图需要 Codex 环境提供图片生成能力；A+ 新页面创作尚未实现。发布版的复现交付线为硬门槛通过且人工视觉量表 **>90/100**。
