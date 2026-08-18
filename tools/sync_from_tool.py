#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_from_tool.py — 从「品牌版」工具源文件生成「去品牌化」skill 资源。

维护约定（解决两份 index.html 长期分叉问题）：
- 唯一源头 = 个人品牌版工具  GoodTimeGGB/ning-md2wechat/index.html
  （在线版 https://goodtimeggb.github.io/ning-md2wechat/ 即此文件）
- 本仓库的 index.html（仓库根）由本脚本生成，禁止手动改它，
  否则下次同步会覆盖。

用法：
  python tools/sync_from_tool.py
  python tools/sync_from_tool.py --source /path/to/ning-md2wechat/index.html
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SOURCE = (
    r"C:\Users\Administrator\WorkBuddy\2026-07-28-14-09-25"
    r"\ning-md2wechat\index.html"
)
DEFAULT_OUTPUT = os.path.normpath(os.path.join(HERE, "..", "index.html"))

# 署名块：各主题 style 颜色不同，用 [^>]* 匹配任意属性后统一替换
SIG_RE = re.compile(
    r"我是 <strong[^>]*>GoodTime</strong>，｜全栈·AI讲师·社区主理人｜"
    r"公众号<strong[^>]*>【宁的AI小站】</strong>——用技术让AI更实用。"
)

# 顺序：更具体的先替换，避免「宁的AI小站 · 公众号」误伤「宁的AI小站 · 公众号排版工具」
REPLACEMENTS = [
    ('<title>宁的AI小站 · 公众号排版工具</title>', '<title>公众号 Markdown 排版工具</title>'),
    ('宁的AI小站 · 公众号排版工具', '公众号 Markdown 排版工具'),
    ('宁的AI小站 · AI SERIES', 'AI SERIES · 公众号'),
    ('宁的AI小站 · 公众号', '公众号 · 系列'),
    ('文 / GoodTime', '文 / 作者'),
    ('GoodTime 记', '手记'),
    ('宁的AI小站', '公众号排版工具'),
    ('10 套主题', '11 套主题'),
]


def sync(source, output):
    if not os.path.isfile(source):
        sys.exit(
            "[ERROR] 源头文件不存在: %s\n"
            "请通过 --source 指定 ning-md2wechat/index.html 路径" % source
        )
    with open(source, "r", encoding="utf-8") as f:
        text = f.read()

    text, n_sig = SIG_RE.subn("感谢阅读 · 欢迎关注并转发", text)
    for a, b in REPLACEMENTS:
        text = text.replace(a, b)

    leftover = re.findall(r"宁的AI小站|GoodTime|ning-md2wechat", text)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    print("源: %s" % source)
    print("出: %s" % os.path.abspath(output))
    print("替换署名块: %d 处" % n_sig)
    if leftover:
        print("[WARN] 仍有 %d 处品牌残留: %s" % (len(leftover), set(leftover)))
    else:
        print("品牌字样已清零 ✓")
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=DEFAULT_SOURCE)
    ap.add_argument("--output", default=DEFAULT_OUTPUT)
    args = ap.parse_args()
    sync(args.source, args.output)
    print("完成。如需更新 skill 仓库：")
    print('  git add assets/index.html && git commit -m "sync: 从工具源同步" && git push')


if __name__ == "__main__":
    main()
