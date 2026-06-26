#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_index.py — 生成 Scalar standalone index.html（阶段五，路线 A 第 4 步）

从 ws-site/<lang>/*.json 派生 source 列表（不手抄），输出 ws-site/<lang>/index.html。
用 Scalar 官方 CDN 的 @scalar/api-reference，多 source 下拉侧边栏，零网络监听。

呈现层规则（不动任何 spec 内容、不改文件）
------------------------------------------
- 显示名：默认取 info.title；泛标题 "AIsa API proxy" 用文件名兜底（A.5.4，不编营销标题）。
- IA 分组：7 份 twitter-* 统一加 "Twitter · " 前缀，使其在下拉里聚成一簇
  （Scalar source 选择器是扁平下拉，原生无嵌套分组；前缀聚簇是最忠实的呈现层近似）。
- slug：用文件名，稳定、可深链。
- 默认档：openai-chat（OpenAI 兼容网关的代表接口）置顶为 default。
- 在线 "Test Request"：默认关闭（hideTestRequestButton=true，连带隐藏鉴权面板），
  servers 指向真网关 api.aisa.one、涉鉴权，开关交负责人决断（A.5.5）。
"""
import argparse
import glob
import html
import json
import os

CDN = "https://cdn.jsdelivr.net/npm/@scalar/api-reference"

TW_PREFIX = "Twitter · "
TWITTER_LABELS = {
    "twitter-actions": "Actions",
    "twitter-communities": "Communities",
    "twitter-list": "Lists",
    "twitter-trend": "Trends",
    "twitter-tweet-batch_01": "Tweets (batch 01)",
    "twitter-tweet-batch_02": "Tweets (batch 02)",
    "twitter-tweet-replies-v2": "Tweet Replies V2",
    "twitter-user-batch_01": "Users (batch 01)",
    "twitter-user-batch_02": "Users (batch 02)",
}
GENERIC_TITLES = {"AIsa API proxy", "", None}
DEFAULT_SLUG = "openai-chat"

PAGE_TITLE = {"en": "AIsa API Reference", "zh": "AIsa API 参考文档"}
LOCALE = {"en": "en", "zh": "zh"}


def display_name(name, title):
    if name in TWITTER_LABELS:
        return TW_PREFIX + TWITTER_LABELS[name]
    if name.startswith("twitter-"):
        return TW_PREFIX + name[len("twitter-"):]
    if title in GENERIC_TITLES:
        return name  # 泛标题用文件名兜底，不编造
    return title


def sort_key(name):
    # twitter-* 连续聚簇排在一起；其余按名字；默认档置顶
    if name == DEFAULT_SLUG:
        return (0, "")
    if name.startswith("twitter-"):
        return (2, name)
    return (1, name)


def build_sources(lang_dir):
    files = sorted(glob.glob(os.path.join(lang_dir, "*.json")))
    items = []
    for f in files:
        name = os.path.basename(f)[:-5]
        d = json.load(open(f, encoding="utf-8"))
        title = (d.get("info") or {}).get("title")
        items.append((name, display_name(name, title)))
    items.sort(key=lambda it: sort_key(it[0]))
    sources = []
    for name, label in items:
        src = {"slug": name, "title": label, "url": "./%s.json" % name}
        if name == DEFAULT_SLUG:
            src["default"] = True
        sources.append(src)
    return sources


def render_html(lang, sources):
    config = {
        "sources": sources,
        "hideTestRequestButton": True,   # 默认关闭在线请求（A.5.5），开关交负责人
        "hideDarkModeToggle": False,
        "darkMode": False,
        "defaultOpenAllTags": False,
        "documentDownloadType": "none",
        "localization": {"locale": LOCALE[lang]},
    }
    cfg_json = json.dumps(config, ensure_ascii=False, indent=2)
    title = html.escape(PAGE_TITLE[lang])
    return """<!doctype html>
<html lang="%(locale)s">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>%(title)s</title>
    <style>
      body { margin: 0; }
    </style>
  </head>
  <body>
    <div id="app"></div>
    <script src="%(cdn)s"></script>
    <script>
      Scalar.createApiReference('#app', %(config)s)
    </script>
  </body>
</html>
""" % {"locale": LOCALE[lang], "title": title, "cdn": CDN, "config": cfg_json}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", required=True, choices=("en", "zh"))
    ap.add_argument("--dir", required=True, help="ws-site/<lang> 目录")
    args = ap.parse_args(argv)
    sources = build_sources(args.dir)
    out = os.path.join(args.dir, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(render_html(args.lang, sources))
    print("build_index[%s]: %d sources -> %s" % (args.lang, len(sources), out))
    for s in sources:
        print("   %-28s %s%s" % (s["slug"], s["title"],
                                  "  [default]" if s.get("default") else ""))


if __name__ == "__main__":
    main()
