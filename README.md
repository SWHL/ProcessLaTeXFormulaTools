<div align="center">
  <div align="center">
    <h1><b>🛠️ Process LaTeX formula Tools</b></h1>
  </div>
  <a href=""><img src="https://img.shields.io/badge/Python->=3.6,<3.12-aff.svg"></a>
  <a href=""><img src="https://img.shields.io/badge/OS-Linux%2C%20Mac-pink.svg"></a>
  <a href="https://semver.org/"><img alt="SemVer2.0" src="https://img.shields.io/badge/SemVer-2.0-brightgreen"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
  <a href="https://github.com/SWHL/ProcessLaTeXFormulaTools/blob/fee132e672e22ea417e34050b9a3e9df825ab36c/LICENSE"><img alt="GitHub" src="https://img.shields.io/badge/license-MIT-blue"></a>
  <a href="https://pepy.tech/project/process_formula"><img src="https://static.pepy.tech/personalized-badge/process_formula?period=total&units=abbreviation&left_color=grey&right_color=blue&left_text=Downloads"></a>
  <a href="https://pypi.org/project/process-formula/"><img alt="PyPI" src="https://img.shields.io/pypi/v/process-formula"></a>

  [简体中文](./docs/README_zh.md) | English
</div>

### Introduction
This repository is a library of tools for processing LaTeX formulas. This includes checking existing LaTeX formulas for syntax errors and normalizing existing LaTeX formulas for subsequent use in tasks such as training.


### What are normalized LaTeX formulas?
<div align="center">
    <img src="https://github.com/SWHL/ProcessLaTeXFormulaTools/releases/download/v0.0.0/normalize_demo.jpg" width="70%" height="70%">
</div>

From：[An End-to-End Formula Recognition Method Integrated Attention Mechanism Figure 7.](https://www.mdpi.com/2227-7390/11/1/177)


### Environment
- [Node.js](https://nodejs.org/en/download)
- Python

### Installation
```bash
pip install process_formula
```

### Usage
```bash
$ normalize_formular --input_content tests/test_files/formulas.lst --out_path formulas.norm.lst
```

### Documentation
Full documentation can be found on [docs](https://swhl.github.io/ProcessLaTeXFormulaTools/docs), in Chinese.

### Acknowledgements
Most of the code in this warehouse comes from [harvardnlp/im2markup](https://github.com/harvardnlp/im2markup). Thank you very much.

### Code Contributors
<p align="left">
  <a href="https://github.com/SWHL/ProcessLaTeXFormulaTools/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=SWHL/ProcessLaTeXFormulaTools" width="8%"/>
  </a>
</p>

### Contributing
- Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
- Please make sure to update tests as appropriate.

### [Sponsor](https://rapidai.github.io/Knowledge-QA-LLM/docs/sponsor/)
If you want to sponsor the project, you can directly click the **Buy me a coffee** image, please write a note (e.g. your github account name) to facilitate adding to the sponsorship list below.

<div align="left">
   <a href="https://www.buymeacoffee.com/SWHL"><img src="https://raw.githubusercontent.com/RapidAI/.github/main/assets/buymeacoffe.png" width="30%" height="30%"></a>
</div>


### License
This project is released under the [Apache 2.0 license](https://github.com/SWHL/ProcessLaTeXFormulaTools/blob/fee132e672e22ea417e34050b9a3e9df825ab36c/LICENSE).
