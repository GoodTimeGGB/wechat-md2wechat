# 公众号 Markdown 排版工具（wechat-md2wechat）

> 一套**不绑定任何个人品牌**的通用排版方案：把 Markdown 文章一键转成可直接粘贴到微信公众号编辑器的**内联样式 HTML**。零依赖、单文件离线可用、内置 11 套主题。
>
> 它**不是某个 Agent 的私有插件**，而是一份**任何桌面 AI Agent 都能用**的「技能包」。本文给出 WorkBuddy、Claude Code / Cowork、OpenAI Codex、Trae（TraeWork）、千问办公、百度 Dumate 等的具体接入方法——你用哪个，翻到对应小节即可。

---

## 它能做什么

- **Markdown → 公众号内联样式 HTML**：粘贴不丢格式，直接进公众号编辑器
- **11 套主题皮肤**任选（手绘 / 卡通 / 书法 / 极简 / 极客 / 杂志 / 柔光 / 棱镜 / 山水 / 故事 / 宣发）
- **链接自动可点击**、**代码块一键复制**
- **单文件 HTML**，离线可用，无需 API key / 联网 / 后端
- 既可**人工**使用，也可**交给 AI Agent 自动排版**

---

## 两种使用方式

### 方式 A：直接用工具（无需 AI，任何浏览器）

适合只想快速排好一篇文章的你，全程不依赖任何 Agent。

1. 获取 `assets/index.html`（见下方「第 0 步：获取仓库」）
2. 用浏览器打开（双击即可，**离线可用**）
3. 左侧粘贴 / 写 Markdown，顶部选主题，右侧实时预览
4. 点「复制」，回到公众号编辑器 `Ctrl / Cmd + V` 粘贴，排版即生效

### 方式 B：交给桌面 Agent 帮你排（AI 自动）

适合你把文章丢给 Agent，让它按规范产出公众号 HTML，或让它帮你打开工具、批量处理。

- **AI 直接产出 HTML**：Agent 读取 `SKILL.md` 后，按规范把你的 Markdown 转成公众号 HTML
- **AI 代操作工具**：让 Agent 打开 `assets/index.html`，按你的要求选主题、复制结果

> 方式 B 的前提是让 Agent「认识」这个技能包——下面按不同 Agent 给出接入方法。

---

## 📋 一键安装：复制这句话，直接发给你的 AI

无论你用哪个桌面 Agent，**最省事的方式就是直接把这句话发给它**：

```
帮我安装这个公众号排版技能：https://github.com/GoodTimeGGB/wechat-md2wechat
```

大多数能联网的桌面 Agent（WorkBuddy、Claude Code / Cowork、Codex、Trae、千问办公、百度 Dumate 等）看到这个 GitHub 链接 +「安装 / 技能」关键词，会**自动把仓库 clone 下来、读取 `SKILL.md` 并加载为可用技能**。发完这句话，再发文章就能直接排版。

如果某个 Agent 不支持「从链接自动安装」，翻到下方对应小节，用那个 Agent 专属的指令块即可。

---

## 支持的桌面 Agent 与接入方法

### 第 0 步：先获取本仓库

无论用哪个 Agent，先拿到文件：

```bash
git clone https://github.com/GoodTimeGGB/wechat-md2wechat.git
```

或在 GitHub 页面 `Code → Download ZIP`。技能包核心是两份文件：

- `assets/index.html` —— 排版工具本体（离线单文件）
- `SKILL.md` —— 给 AI Agent 看的「使用说明书」

---

### 1. WorkBuddy

- **方式一（推荐）· 技能市场导入**：SkillHub / WorkBuddy 技能市场 → 「GitHub 导入」→ 绑定本仓库（分支 `main`，路径留空＝仓库根）→ 读取到 `SKILL.md` + `manifest.yaml` 后提交。后续本仓库 push，SkillHub 自动同步。
- **方式二（本地）· 放技能目录**：把仓库复制到 `~/.workbuddy/skills/wechat-md2wechat/`，重启 WorkBuddy 即识别。

👉 **发给 WorkBuddy 的指令（复制即可）**

```
帮我从 GitHub 安装公众号排版技能，仓库地址：https://github.com/GoodTimeGGB/wechat-md2wechat（分支 main，根目录）
```

---

### 2. Claude Code / Claude Cowork（桌面版）

Claude Code / Cowork 支持 **skills 目录**，会自动识别其中的 `SKILL.md`。

```bash
# 全局（所有项目可用）
cp -r wechat-md2wechat ~/.claude/skills/wechat-md2wechat

# 或仅当前项目
cp -r wechat-md2wechat .claude/skills/wechat-md2wechat
```

👉 **发给 Claude Code / Cowork 的指令（复制即可）**

```
请执行：git clone https://github.com/GoodTimeGGB/wechat-md2wechat.git ~/.claude/skills/wechat-md2wechat
安装完成后，之后我用“wechat-md2wechat”这个技能把文章排成公众号。
```

- 不同 Claude 版本入口名称可能略有差异，认准「能放一个技能 / 指令文件夹」的位置即可。

---

### 3. OpenAI Codex（CLI）

Codex 没有独立 skills 目录，但可以把技能说明作为**指令 / 上下文**注入。

- **方法一 · 指令注入**：把 `SKILL.md` 全文贴进你的提示词，或存进项目 `AGENTS.md` / `codex.md` 作为长期上下文。
- **方法二 · 直接驱动**：让 Codex 读取仓库并用工具：

  ```
  codex exec "读取 SKILL.md，把 article.md 按规范转成公众号 HTML（参考 assets/index.html 的主题样式）"
  ```

- 也可在 Codex 会话里直接说「打开 assets/index.html 帮我排版」。

👉 **发给 Codex 的指令（复制即可）**

```
请阅读 https://raw.githubusercontent.com/GoodTimeGGB/wechat-md2wechat/main/SKILL.md ，把它作为你的长期排版规范。以后我把 Markdown 发给你时，按里面的规范转成公众号内联样式 HTML。
```

---

### 4. Trae（TraeWork，字节）

Trae 支持**项目级 Rules / 自定义 AI 指令**：

- 把 `SKILL.md` 内容写入项目 `.trae/rules/wechat-md2wechat.md`（或在 Trae 设置里的「Rules for AI」粘贴）。
- 或在对话开头贴一句：「请先阅读 `./SKILL.md`，之后按它的规范把我的文章排成公众号 HTML」。

👉 **发给 Trae 的指令（复制即可）**

```
把 https://raw.githubusercontent.com/GoodTimeGGB/wechat-md2wechat/main/SKILL.md 的内容加入本项目的 Rules（Rules for AI）。之后帮我把文章排成公众号。
```

---

### 5. 千问办公 / 通义（Qwen）

- **自建智能体**：在千问办公（或通义千问智能体平台）新建智能体，把 `SKILL.md` 全文粘贴进「智能体指令 / 角色设定」。
- **附参考文件**：把 `assets/index.html` 与 `SKILL.md` 作为知识库 / 附件上传，让智能体读取后按规范排版。

👉 **发给千问办公 / 通义的指令（复制即可）**

```
请阅读这个技能说明：https://raw.githubusercontent.com/GoodTimeGGB/wechat-md2wechat/main/SKILL.md ，并把它设为你的智能体指令。以后我发文章时，按它的规范排成公众号 HTML。
```

---

### 6. 百度 Dumate

- 在 Dumate 的**自定义 Agent / 智能体设定**里，把 `SKILL.md` 作为「系统指令 / 提示词」粘贴。
- 或上传 `SKILL.md` + `assets/index.html` 作为参考文件，让 Agent 读取后排版。

👉 **发给百度 Dumate 的指令（复制即可）**

```
把 https://raw.githubusercontent.com/GoodTimeGGB/wechat-md2wechat/main/SKILL.md 设为你的系统指令。以后我发 Markdown，按它的规范排成公众号 HTML。
```

---

### 7. 通用方法（任何支持「自定义指令 / 系统提示词」的 Agent）

只要你的 Agent 能设置系统指令或读取文件，就能用：

1. 下载本仓库（见第 0 步）
2. 把 `SKILL.md` 内容设为 Agent 的「系统指令 / 自定义提示词」
3. 把 `assets/index.html` 作为参考文件 / 附件交给 Agent
4. 对话里说「按 SKILL.md 把这篇 Markdown 排成公众号」，或直接打开工具自己用

👉 **发给任意 Agent 的通用指令（复制即可）**

```
阅读这个技能包：https://github.com/GoodTimeGGB/wechat-md2wechat ，把 SKILL.md 设为你的系统指令，并把 assets/index.html 作为参考工具。之后按规范把我的文章排成公众号。
```

> 各平台菜单名称（如「智能体指令」「Rules」「系统提示词」）可能随版本变化，认准「能粘贴一段长期生效的指令」的入口即可。

---

## 🚀 日常使用：把文章交给 Agent 排版

装好技能后，每次排版直接发这句话 + 你的文章（把 `<粘贴文章>` 换成你的 Markdown）：

```
用 wechat-md2wechat 把下面这篇 Markdown 排成公众号（手绘笔记风），输出可直接粘贴到公众号编辑器的内联样式 HTML：

<粘贴你的 Markdown 文章>
```

**主题关键词**（替换上面括号里的风格即可）：

| 想要的效果 | 关键词 |
|------------|--------|
| 手作编辑感、便签涂鸦 | 手绘笔记 / handdrawn（默认） |
| 明快圆润、彩色胶囊 | 卡通 / cartoon |
| 宣纸留白、书法标题 | 书法 / ink |
| 大量留白、克制 | 极简 / minimal |
| 等宽字体、终端感 | 极客 / geek |
| 网格、栏目感 | 杂志 / editorial |
| 渐变光晕、梦幻 | 柔光 / aurora |
| 深色玻璃、霓虹 | 棱镜 / prism |
| 青绿设色、山水 | 山水 / landscape |
| 温暖插画、手写 | 故事 / storybook |
| 深蓝+亮黄、海报感 | 宣发 / launch |

如果不指定风格，默认走「手绘笔记风」。

---

## 11 套主题与适用场景

| 主题 | 风格 | 适合 |
|------|------|------|
| 手绘笔记 handdrawn | 手作编辑感、便签涂鸦 | 个人随笔、教程（默认） |
| 活力卡通 cartoon | 明快圆润、彩色胶囊 | 年轻化、轻松内容 |
| 水墨书法 ink | 宣纸留白、书法标题 | 文化、国风内容 |
| 极简留白 minimal | 大量留白、克制 | 专业、干货长文 |
| 代码极客 geek | 等宽字体、终端感 | 技术教程、代码向 |
| 杂志编辑 editorial | 网格、栏目感 | 资讯、深度报道 |
| 柔光幻境 aurora | 渐变光晕、梦幻 | 情感、生活方式 |
| 暗夜棱镜 prism | 深色玻璃、霓虹 | 科技、酷感内容 |
| 青绿山水 landscape | 青绿设色、山水 | 文旅、国风 |
| 枕边故事 storybook | 温暖插画、手写 | 亲子、故事 |
| 活动宣发 launch | 深蓝 + 亮黄、海报感 | 活动预告、Meetup |

---

## 支持的 Markdown 语法

`#` 标题（1–4 级）、`**加粗**`、`*斜体*`、`~~删除线~~`、`> 引用`、`| 表格 |`、```` ``` ```` 代码块、`` `行内代码` ``、`- / 1.` 列表、`---` 分隔线、`![图](url)`、`[链接](url)`、裸网址自动链接。

---

## 仓库结构

```
wechat-md2wechat/
├── SKILL.md                    ← 给 AI Agent 的技能说明（排版规范 + 工作流）
├── manifest.yaml               ← 技能市场元数据（SkillHub / WorkBuddy）
├── assets/
│   └── index.html              ← 去品牌化单文件排版工具（由脚本生成，勿手改）
├── tools/
│   └── sync_from_tool.py       ← 从源头同步生成 assets/index.html
└── README.md
```

---

## 维护 / 更新（避免两份 index.html 分叉）

`assets/index.html` **不是手写的**，而是从品牌版工具源 `GoodTimeGGB/ning-md2wechat/index.html` 经 `tools/sync_from_tool.py` 去品牌化生成：

```bash
python tools/sync_from_tool.py --source /path/to/ning-md2wechat/index.html
git add assets/index.html && git commit -m "sync: 从工具源同步" && git push
```

品牌版工具更新后，跑一次脚本即可让 skill 资源同步，杜绝两份 `index.html` 长期分叉。

---

## 常见问题 FAQ

- **公众号里外部链接点不动？** 微信平台规则：只有 `mp.weixin.qq.com` 域名可点击，外部链接会被转成纯文本——任何工具都无法绕过。
- **需要联网吗？** 不需要。`assets/index.html` 纯前端，离线可用。
- **能商用 / 二次修改吗？** 可以，MIT 许可，工具内不含任何品牌信息。
- **想要更多主题 / 自定义？** 编辑 `assets/index.html` 里的主题对象即可；或参考品牌版 `ning-md2wechat` 仓库的 `references/` 主题库获取更多组件。
- **AI 直排（方式 B）和工具（方式 A）怎么选？** 想反复微调样式、所见即所得 → 用工具（方式 A）；想让 Agent 直接给你成品 HTML、或批量处理 → 用方式 B。

---

## License

[MIT](LICENSE) — author: GoodTime
