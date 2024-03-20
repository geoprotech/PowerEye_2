import re
import sys
import logging
from pathlib import Path

import cssutils

from bin.exceptions import StylesheetException


cssutils.log.setLevel(logging.CRITICAL)


# temporary
def stylesheet(file):
    CUR_PATH = Path(file).parent
    with open(CUR_PATH / Path("style.css")) as f:
        data = f.read()
    return data


CUSTOM_OPTIONS = [
    "spacing",
    "width",
    "height",
    "margin",
    "geometry",
]

DEFAULT_BLOCK_NAME = "QWidget"


class Stylesheet(str):
    def __init__(self, template: str):
        self.template = template
        self._blocks: dict[str, StylesheetBlock] = {}
        self._parse_template()

    def _parse_template(self):
        sheet = cssutils.parseString(self.template)

        for rule in sheet:
            block_header = rule.selectorText

            current_block_name = block_header.split()[0] if len(block_header.split()) else DEFAULT_BLOCK_NAME

            if current_block_name in self._blocks:
                if len(block_header.split()) > 1:
                    self._blocks[current_block_name].add_sub_block(
                        block_header.split()[-1].replace("#", ""),
                        block_header + " {\n" + rule.style.cssText + ";\n} \n",
                    )
                else:
                    print(
                        f"Warning! Duplicate name '{block_header.split()[0]}' for stylesheet in directory: "
                        f"{Path(__file__).parent}, last definition will be used.",
                        file=sys.stderr,
                    )
            else:
                self._blocks[current_block_name] = StylesheetBlock(
                    block_header + " {\n" + rule.style.cssText + ";\n} \n"
                )
                setattr(self, current_block_name, self._blocks[current_block_name])

    @classmethod
    def read(cls, file: Path):
        dir_path = file.parent
        with open(dir_path / Path("style.css")) as f:
            data = f.read()
        return cls(data)


class StylesheetBlock(str):
    def __init__(self, template: str):
        self.template = template
        self._sub_blocks: dict[str, StylesheetBlock] = {}
        self._parse_template()

    def _parse_template(self):
        sheet = cssutils.parseString(self.template)

        for rule in sheet:
            for option in rule.style:
                if option.name.startswith("custom-"):
                    custom_option_name = option.name.replace("custom-", "")

                    if custom_option_name not in CUSTOM_OPTIONS:
                        raise StylesheetException(f"fWrong custom option name: {custom_option_name}", "info")

                    setattr(self, custom_option_name, self.strip_units(option.value))
                else:
                    setattr(self, option.name.replace("-", "_"), option.value)

    def add_sub_block(self, sub_block_name: str, template: str) -> None:
        if sub_block_name in self._sub_blocks:
            print(
                f"Warning! Duplicate name '{sub_block_name}' for stylesheet in directory: "
                f"{Path(__file__).parent}, last definition will be used.",
                file=sys.stderr,
            )

        self._sub_blocks[sub_block_name] = StylesheetBlock(template)
        setattr(self, sub_block_name.replace("-", "_"), StylesheetBlock(template))

    @staticmethod
    def strip_units(string: str):
        re_digits = re.compile(r"\d+")
        return re_digits.findall(string)


if __name__ == "__main__":
    filename = Path("./style.css")  # noqa
    TEST_STYLESHEET = Stylesheet.read(filename)
    print(TEST_STYLESHEET.__dict__.keys())
    print(TEST_STYLESHEET.QDialog.__dict__.keys())
    print(TEST_STYLESHEET.QDialog.test.__dict__.keys())
