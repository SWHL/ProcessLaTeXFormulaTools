# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from process_formula import NormalizeFormula

normlizer = NormalizeFormula()

# mode = "normalize"
# input_path = "tests/test_files/formulas.lst"
# out_path = "tests/test_files/formulas.norm.lst"

# normlizer(mode=mode, input_content=input_path, out_path=out_path)


math_str = [
    r"\,^{*}d\,^{*}H=\kappa \,^{*}d\phi = J_B  . \label{bfm19}",
    r"\label{A0}A_0 = \pm\sqrt{{4\over 3(1-\alpha)}}e^{(\alpha-1)\phi}\ .",
]

result = normlizer(math_str)
print("ok")
