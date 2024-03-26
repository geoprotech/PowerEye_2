import re
import sys
import logging
import warnings
from pathlib import Path

import cssutils
from style_constants import GLOBAL_STYLE_CONSTANTS

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

RE_STRIP_DIGITS = re.compile(r"\d+")


class Stylesheet(str):
    """
    Class representing a framework allowing to convert .css files to .qss stylesheets, that can be used in Qt widgets
    and windows.

    Stylesheet inherent from base python str class. Thus, you can work with this class instances like you work with
    strings.

    Every Stylesheet instance consist of at least one StylesheetBlock(For example: QWidget {...})

    Stylesheet instance can be defined directly from string or from a .css file(see 'read' method below).
    """

    def __init__(self, template: str):
        self.template = template
        self._blocks: dict[str, StylesheetBlock] = {}
        self._parse_template()

    def _parse_template(self):
        sheet = cssutils.parseString(self.template)

        for rule in sheet:
            block_header = rule.selectorText

            current_block_name = (
                block_header.split()[0].split("::")[0] if len(block_header.split()) > 0 else DEFAULT_BLOCK_NAME
            )

            self.add_block(current_block_name, rule.style.cssText)

            if len(block_header.split()) > 1:
                if not hasattr(self._blocks[current_block_name], block_header.split()[-1].replace("#", "")):
                    ineffective_header = block_header.split()[0].split("::")[0] + " " + block_header.split()[-1]
                    self._blocks[current_block_name].add_sub_block(
                        block_header.split()[-1].replace("#", ""),
                        ineffective_header + " {\n" + rule.style.cssText + ";\n} \n",
                    )

            if len(block_header.split()[0].split("::")) > 1:
                try:
                    self._blocks[current_block_name].__dict__[block_header.split()[-1].replace("#", "")].add_sub_block(
                        block_header.split()[0].split("::")[-1].replace("-", "_"),
                        block_header + " {\n" + rule.style.cssText + ";\n} \n",
                    )
                except KeyError:
                    self._blocks[current_block_name].add_sub_block(
                        block_header.split()[0].split("::")[-1].replace("-", "_"),
                        block_header + " {\n" + rule.style.cssText + ";\n} \n",
                    )

    def add_block(self, block_name: str, block_content: str) -> None:
        if block_name not in self._blocks:
            self._blocks[block_name] = StylesheetBlock(block_name + " {\n" + block_content + ";\n} \n")

            setattr(self, block_name, self._blocks[block_name])

    @staticmethod
    def replace_constants(data: str):
        for key, value in GLOBAL_STYLE_CONSTANTS.items():
            data = data.replace(key, str(value))

        return data

    @classmethod
    def read(cls, file: Path):
        dir_path = file.parent
        with open(dir_path / Path("style.css")) as f:
            data = f.read()
        data = Stylesheet.replace_constants(data)
        return cls(data)


class StylesheetBlock(str):
    """
    As mentioned in Stylesheet docstring, every Stylesheet instance consist of at least one StylesheetBlock.

    If there are more than one block with same name, and they have different ids corresponded StylesheetBlock instances
    will be created and contained into main StylesheetBlock attributes. If ids are the same or None last definition
    will be taken.

    You can access every sub block by id and every css property by name.
    For example:

    STYLESHEET_NAME.QWidget
    STYLESHEET_NAME.QWidget.PROPERTY_NAME
    STYLESHEET_NAME.QWidget.SUB_BLOCK_ID.PROPERTY_NAME
    """

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
            warnings.warn(
                f"Warning! Duplicate id '{sub_block_name}' for stylesheet in directory: "
                f"{Path(__file__).parent}, first definition will be used."
            )
            return

        self._sub_blocks[sub_block_name] = StylesheetBlock(template)
        setattr(self, sub_block_name.replace("-", "_"), StylesheetBlock(template))

    @staticmethod
    def strip_units(string: str) -> int | str | list[int | str]:
        string_result = RE_STRIP_DIGITS.findall(string)
        final_result = []

        if len(string_result) > 1:
            for el in string_result:
                try:
                    final_result.append(int(el))
                except ValueError:
                    final_result.append(el)

            return final_result

        else:
            try:
                return int(string_result[0])
            except ValueError:
                return string_result[0]
            except IndexError:
                return string


if __name__ == "__main__":
    filename = Path("./style.css")  # noqa
    TEST_STYLESHEET = Stylesheet.read(filename)
    # tests
    print(TEST_STYLESHEET.QWidget.__dict__.keys())
    print(TEST_STYLESHEET.QWidget.header.__dict__.keys())
    print(TEST_STYLESHEET.QWidget.header.hover.__dict__.keys())
    print(TEST_STYLESHEET.QWidget.__dict__.keys())
    print("-" * 100)
    print(TEST_STYLESHEET.QDialog.__dict__.keys())
    print(TEST_STYLESHEET.QDialog.hover.__dict__.keys())
    print("-" * 100)
    print(TEST_STYLESHEET)
