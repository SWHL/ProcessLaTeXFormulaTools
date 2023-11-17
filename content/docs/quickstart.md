---
weight: 2000
lastmod: "2022-08-10"
draft: false
author: "SWHL"
title: "快速开始"
icon: "rocket_launch"
description: "故事的开始，只需3步。"
toc: true
---


### 1. 安装
```bash {linenos=table}
pip install process_formula
```

### 2. 使用
{{< tabs tabTotal="2">}}
{{% tab tabName="终端使用" %}}

```bash {linenos=table}
normalize_formular --input_content tests/test_files/formulas.lst --out_path formulas.norm.lst
```

{{% /tab %}}
{{% tab tabName="Python使用" %}}

```python {linenos=table}
from process_formula import NormalizeFormula

normlizer = NormalizeFormula()

math_str = [
    r"\,^{*}d\,^{*}H=\kappa \,^{*}d\phi = J_B  . \label{bfm19}",
    r"\label{A0}A_0 = \pm\sqrt{{4\over 3(1-\alpha)}}e^{(\alpha-1)\phi}\ .",
]

result = normlizer(math_str)
print(result)

# 输出示例：
[
    '\\, ^ { * } d \\, ^ { * } H = \\kappa \\, ^ { * } d \\phi = J _ { B } .',
    'A _ { 0 } = \\pm \\sqrt { { \\frac { 4 } { 3 ( 1 - \\alpha ) } } } e ^ { ( \\alpha - 1 ) \\phi } \\ .'
]
```
{{% /tab %}}
{{< /tabs >}}
