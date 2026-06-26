#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""find_examples.py — 为每种写作模式从 /tmp/pairs.jsonl 捞候选案例，便于人工挑选。"""
import json

pairs = [json.loads(l) for l in open("/tmp/pairs.jsonl", encoding="utf-8")]


def show(title, items, n=6):
    print("\n" + "=" * 70)
    print("【%s】 命中 %d" % (title, len(items)))
    print("=" * 70)
    for p in items[:n]:
        print("- [%s/%s] %s" % (p["spec"], p["loc"], p["name"]))
        print("    NATIVE: %r" % (p["native"][:160] or "(空)"))
        print("    ENH   : %r" % p["enh"][:220])


def words(s):
    return len(s.split())


# 模式1：从无到有（native 空，enh 有内容）
p1 = [p for p in pairs if not p["native"] and p["loc"] == "field" and 8 <= words(p["enh"]) <= 30]
show("模式1 从无到有（源空白→一句人话）", p1)

# 模式2：短标签→完整句（native 是 1-3 词标签，enh 扩成句）
p2 = [p for p in pairs if p["native"] and words(p["native"]) <= 3
      and words(p["enh"]) >= 10 and p["loc"] == "field"]
show("模式2 标签扩写（'Category'→完整释义）", p2)

# 模式3：补默认/省略后果（enh 含 omit/default/fall back/if not）
kw3 = ("omit", "default", "fall back", "falls back", "if not", "when omitted", "leave it", "absent")
p3 = [p for p in pairs if p["loc"] == "field" and any(k in p["enh"].lower() for k in kw3)
      and words(p["native"]) < words(p["enh"])]
show("模式3 补默认行为/省略后果", p3)

# 模式4：补用途/下游（enh 含 use it / use to / downstream / pass it / build）
kw4 = ("use it", "use to", "used to", "downstream", "pass it", "build a", "as the input", "to page", "feed")
p4 = [p for p in pairs if p["loc"] == "field" and any(k in p["enh"].lower() for k in kw4)]
show("模式4 补用途与下游用法（不止说是什么）", p4)

# 模式5：枚举业务含义（enh 含 such as / e.g. 解释取值含义，native 短）
p5 = [p for p in pairs if p["loc"] == "field" and ("such as" in p["enh"].lower() or "e.g." in p["enh"].lower())
      and words(p["native"]) <= 6]
show("模式5 枚举的业务含义（写含义不抄字面）", p5)

# 模式6：operation 级——summary 短，desc_en 给能力+场景
p6 = [p for p in pairs if p["loc"] == "operation" and p["native"] and words(p["enh"]) >= 25]
show("模式6 接口定位（能力+场景+组合价值）", p6)

# 模式7：跨字段依赖（enh 含 alongside / together with / paired / combined / relative to）
kw7 = ("alongside", "together with", "paired", "combined with", "relative to", "in combination", "must match")
p7 = [p for p in pairs if p["loc"] == "field" and any(k in p["enh"].lower() for k in kw7)]
show("模式7 跨字段关系/依赖", p7)

# 模式8：自适应深度——自解释字段保持一句话（enh 很短）
p8 = [p for p in pairs if p["loc"] == "field" and words(p["enh"]) <= 8 and not p["native"]]
show("模式8 自适应深度（自解释字段不注水）", p8)
