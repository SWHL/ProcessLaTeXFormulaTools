# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from process_formula_t import NormalizeFormula

normlizer = NormalizeFormula()

math_str = [
    r"\,^{*}d\,^{*}H=\kappa \,^{*}d\phi = J_B  . \label{bfm19}",
    r"\label{A0}A_0 = \pm\sqrt{{4\over 3(1-\alpha)}}e^{(\alpha-1)\phi}\ .",
]

result = normlizer(math_str)
print(result)
