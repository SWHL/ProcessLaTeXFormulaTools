# -*- encoding: utf-8 -*-
import argparse
import re
import subprocess
from pathlib import Path
from typing import List, Union


class NormalizeFormula:
    def __init__(
        self,
    ):
        self.root_dir = Path(__file__).resolve().parent

    def __call__(
        self, mode: str, input_path: Union[str, Path], out_path: Union[str, Path]
    ):
        # 将hskip 替换为hspace{}
        input_content = self.read_txt(input_path)
        after_content = [
            self.replace_hskip_to_hspace(v).replace("\r", " ").strip()
            for v in input_content
        ]

        # 借助KaTeX获得规范化后的公式
        normalized_formulas = self.get_normalize_formulas(after_content, mode)

        # 去除非ascii得字符
        final_content = self.remove_invalid_symbols(normalized_formulas)

        self.write_txt(out_path, final_content)

    def replace_hskip_to_hspace(self, input_string: str) -> str:
        pattern = r"hskip(.*?)(cm|in|pt|mm|em)"
        replacement = r"hspace{\1\2}"
        output_string = re.sub(pattern, replacement, input_string)
        return output_string

    @staticmethod
    def read_txt(txt_path: Union[Path, str]) -> List[str]:
        with open(txt_path, "r", encoding="utf-8") as f:
            data = [v.rstrip("\n") for v in f]
        return data

    @staticmethod
    def write_txt(
        save_path: Union[str, Path], content: Union[List[str], str], mode: str = "w"
    ) -> None:
        if not isinstance(content, list):
            content = [content]

        with open(save_path, mode, encoding="utf-8") as f:
            for value in content:
                f.write(f"{value}\n")

    def get_normalize_formulas(self, after_content, mode) -> List[str]:
        temp_file = self.root_dir / "tmp"
        self.write_txt(temp_file, after_content)

        out_path = Path(temp_file).with_suffix(".temp.out")
        cmd = "cat %s | node preprocess_formula/preprocess_latex.js %s > %s " % (
            temp_file,
            mode,
            out_path,
        )
        self.run_cmd(cmd)
        self.del_file(temp_file)

        out_content = self.read_txt(out_path)
        self.del_file(out_path)
        return out_content

    def remove_invalid_symbols(self, normalized_formulas: List[str]) -> List[str]:
        final_content = []
        for content in normalized_formulas:
            tokens = content.strip().split()
            tokens_out = [t for t in tokens if self.is_ascii(t)]
            tokens_str = " ".join(tokens_out)

            final_content.append(tokens_str)
        return final_content

    @staticmethod
    def is_ascii(txt: str) -> bool:
        try:
            txt.encode("ascii").decode("ascii")
            return True
        except UnicodeError:
            return False

    @staticmethod
    def run_cmd(cmd: str):
        ret = subprocess.call(cmd, shell=True)
        if ret != 0:
            print(f"FAILED: {cmd}")

    @staticmethod
    def del_file(file_path: Union[str, Path]):
        file_path = Path(file_path)
        if file_path.exists() and file_path.is_file():
            file_path.unlink()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Preprocess (tokenize or normalize) latex formulas"
    )
    parser.add_argument(
        "--mode",
        dest="mode",
        choices=["tokenize", "normalize"],
        required=True,
        help=(
            "Tokenize (split to tokens seperated by space) or normalize (further translate to an equivalent standard form)."
        ),
    )
    parser.add_argument(
        "--input_path",
        dest="input_path",
        type=str,
        required=True,
        help=("Input file containing latex formulas. One formula per line."),
    )
    parser.add_argument(
        "--out_path",
        dest="out_path",
        type=str,
        required=True,
        help=("Output file."),
    )

    args = parser.parse_args()

    processor = NormalizeFormula()

    processor(mode=args.mode, input_path=args.input_path, out_path=args.out_path)

    print("Jobs finished")
