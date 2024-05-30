# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
import argparse
import re
import subprocess
from pathlib import Path
from typing import List, Sequence, Union


class NormalizeFormula:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parent

    def __call__(
        self,
        input_content: Union[str, Path, Sequence[Union[str, Path]]],
        out_path: Union[str, Path, None] = None,
        mode: str = "normalize",
    ) -> List[str]:
        input_data = self.load_data(input_content)

        # 将hskip 替换为hspace{}
        after_content = [
            self.replace_hskip_to_hspace(str(v)).replace("\r", " ").strip()
            for v in input_data
        ]

        if not self.check_node():
            raise NormalizeFormulaError("Node.js was not installed correctly!")

        # 借助KaTeX获得规范化后的公式
        normalized_formulas = self.get_normalize_formulas(after_content, mode)

        # 去除非ascii得字符
        final_content = self.remove_invalid_symbols(normalized_formulas)

        if out_path is not None:
            self.write_txt(out_path, final_content)
        return final_content

    def load_data(
        self, input_content: Union[str, Path, Sequence[Union[str, Path]]]
    ) -> Sequence[Union[str, Path]]:
        if isinstance(input_content, list):
            return input_content

        if isinstance(input_content, (str, Path)):
            if len(str(input_content)) > 255:
                return [input_content]

            if Path(input_content).is_file():
                return self.read_txt(input_content)
            return [input_content]

        raise NormalizeFormulaError("The format of input content is not supported!")

    def check_node(self) -> bool:
        if self.run_cmd("node -v"):
            return True
        return False

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
        latex_js_path = self.root_dir / "preprocess_latex.js"
        cmd = ["node", latex_js_path, mode]

        try:
            result = subprocess.run(
                cmd,
                input="\n".join(after_content),
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.splitlines()
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e.stderr}")
            raise NormalizeFormulaError(
                "Error occurred while normalizing formulas."
            ) from e

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
    def run_cmd(cmd: str) -> bool:
        try:
            ret = subprocess.run(
                cmd,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"Run {cmd} meets error. \n{e.stderr}")
            return False
        return True


class NormalizeFormulaError(Exception):
    pass


def main():
    parser = argparse.ArgumentParser(
        description="Preprocess (tokenize or normalize) latex formulas"
    )
    parser.add_argument(
        "--input_content",
        dest="input_content",
        type=str,
        required=True,
        help="Str / List / file path which contains multi-lines formulas.",
    )
    parser.add_argument(
        "--out_path",
        dest="out_path",
        type=str,
        default=None,
        help="Output file. Default is None",
    )
    parser.add_argument(
        "--mode",
        dest="mode",
        choices=["tokenize", "normalize"],
        default="normalize",
        help=(
            "Tokenize (split to tokens separated by space) or normalize (further translate to an equivalent standard form)."
        ),
    )
    args = parser.parse_args()

    processor = NormalizeFormula()
    result = processor(
        input_content=args.input_content,
        out_path=args.out_path,
        mode=args.mode,
    )
    print(result)


if __name__ == "__main__":
    main()
