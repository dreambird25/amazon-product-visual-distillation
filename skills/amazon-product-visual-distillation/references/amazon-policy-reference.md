# Amazon 图片规则参考

**核验日期：2026-09-23。** 这是用于起步的官方来源索引，不是永久规则清单。每个实际图片任务都要按目标站点、图片渠道和商品类别打开最新官方规则复核；不要仅凭这份快照标记可上架。

## Listing 商品图片

[Amazon US Seller Central：Product image guide](https://sellercentral.amazon.com/help/hub/reference/external/G1881?locale=en_us) 当前说明适用于美国站。主要规则包括：主图真实展示所售商品、纯白背景（RGB 255,255,255）、商品约占画面 85%、完整入框且只展示一次；全体商品图片要准确匹配商品。页面同时列出 500–10,000 px 长边范围、1,000 px 以上建议，以及针对类别/服饰/鞋类等的特殊要求。该页面还明确列出适用于商品图片的文字、价格、Amazon 标识和徽章限制，不能直接沿用第三方 skill 对副图信息图中文字的假设。

Amazon 同一页面增加了逼真人工智能生成人物的标注说明：完全由 AI 生成且逼真的人物图需要在 XMP `dc:subject` 中加入 `contains-synthetic-performer`。实际提交前复核页面的适用范围和当前元数据步骤。

## A+ Content

A+ 内容不等同于 listing 图片轮播，单独使用其官方模块规范和政策核验。Amazon 的[A+ Content Design Guide](https://sell.amazon.com/blog/a-plus-content-design-guide) 建议提交前用 A+ 预览检查桌面和移动端呈现，并提醒避免未证实的奖项/背书、best-selling/top-rated 等表述、保修承诺、价格促销、站外链接/QR 码/联系方式及竞品比较。具体模块规格和审核规则以 Seller Central 当前 A+ 指南为准：[A+ Content guidelines](https://sellercentral.amazon.com/help/hub/reference/GGW8U76SSNTRTBX7)。

Amazon 的人工智能人物标注指南：[How to tag media that contains an AI-generated person](https://sellercentral.amazon.com/help/hub/reference/GFXHCHYZRGJRBZA5)。A+ 管理器可能提供与普通 listing 文件不同的标注路径，不能据一条渠道推定另一条渠道的上传流程。

## 工作时的处理方式

- marketplace 未知：可以先产出带 `unverified` 状态的视觉方案；不可声称平台合规。
- 同一图集中 listing carousel 与 A+ 模块分开建槽位、分开检查政策和画幅。
- 平台规则与产品事实冲突时，把限制写入对应图片槽位，并说明来源及待确认项。
- 仅使用来源明确、用户有权使用的产品材料；第三方参考图提炼为通用的构图、色彩、光线和模块组织，不复制其商标或独有文案。
