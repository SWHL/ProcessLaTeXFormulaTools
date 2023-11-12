# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from preprocess_formula import NormalizeFormula

normlizer = NormalizeFormula()

mode = "normalize"
input_path = "tests/test_files/formulas.lst"
out_path = "tests/test_files/formulas.norm.lst"

normlizer(mode=mode, input_path=input_path, out_path=out_path)
