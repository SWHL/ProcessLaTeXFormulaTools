# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import sys
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
root_dir = cur_dir.parent
sys.path.append(str(root_dir))

from preprocess_formular import NormalizeFormular

test_file_dir = cur_dir / "test_files"
mode = "normalize"
normlizer = NormalizeFormular()


def test_input_normal():
    input_path = test_file_dir / "formulas.lst"
    out_path = test_file_dir / "formulas.norm.lst"

    normlizer(mode=mode, input_path=input_path, out_path=out_path)

    content = normlizer.read_txt(out_path)
    assert len(content) == 1200
    assert len(content[1149]) == 0
