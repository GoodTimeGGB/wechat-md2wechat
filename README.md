# 公众号 Markdown 排版工具 (wechat-md2wechat)

WorkBuddy 技能（skill），把 Markdown 文章一键转换为可直接粘贴到微信公众号编辑器的**内联样式 HTML**。零外部依赖、单文件离线可用，内置 11 套主题。

## 功能
- 11 套主题：手绘笔记风、活力卡通风、水墨书法风、极简留白风、代码极客风、杂志编辑风、柔光幻境风、暗夜棱镜风、青绿山水风、枕边故事风、活动宣发风
- 自动识别并保留可点击链接
- 代码块一键复制
- 内联样式，粘贴公众号不丢格式
- 纯前端单文件，离线可用，无需联网 / API key

## 使用方式
1. 安装技能后，对 WorkBuddy 说「公众号排版 / md2wechat / 把这篇 Markdown 排成公众号」；
2. 或浏览器直接打开 `assets/index.html`，粘贴 Markdown → 选主题 → 复制 HTML → 粘贴进公众号编辑器。

## 仓库结构
- `SKILL.md` / `manifest.yaml` — 技能元信息与发布元数据
- `assets/index.html` — 去品牌化的单文件排版工具（**由脚本生成，勿手改**）
- `tools/sync_from_tool.py` — 从源头同步生成 `assets/index.html`

## 维护 / 更新（避免两份 index.html 分叉）
本仓库的 `assets/index.html` 不是手写的，而是从个人品牌版工具
`GoodTimeGGB/ning-md2wechat/index.html` 经 `tools/sync_from_tool.py` 去品牌化生成：

```bash
python tools/sync_from_tool.py --source /path/to/ning-md2wechat/index.html
git add assets/index.html && git commit -m "sync: 从工具源同步" && git push
```

品牌版工具更新后，跑一次脚本即可让 skill 资源同步，杜绝两份 `index.html` 长期分叉。

## SkillHub 导入
在 SkillHub / WorkBuddy 技能市场选择「GitHub 导入」，绑定本仓库（分支 `main`，路径留空＝仓库根），
读取到 `SKILL.md` + `manifest.yaml` 后提交即可。后续本仓库 push，SkillHub 自动同步。

## License
MIT — author: GoodTime
