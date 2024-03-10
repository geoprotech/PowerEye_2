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


#


CUSTOM_OPTIONS = [
    "spacing",
    "width",
    "height",
    "margin",
    "geometry",
]

DEFAULT_BLOCK_NAME = "general"


class Stylesheet(str):
    def __init__(self, template: str):
        self.template = template
        self.blocks: dict[str, StylesheetBlock] = {}
        self._parse_template()

    def __add__(self, other):
        if not isinstance(other, Stylesheet):
            raise StylesheetException(f"Not implemented operator '+' for Stylesheet and {type(other)}", "info")

        all_blocks = set(list(self.blocks.keys()) + list(other.blocks.keys()))

        result_template = ""

        for block in list(all_blocks):
            if hasattr(self, block) and hasattr(other, block):
                result_template += self.__dict__[block] + other.__dict__[block]
            else:
                try:
                    result_template += self.__dict__[block]
                except AttributeError:
                    result_template += other.__dict__[block]
        return Stylesheet(result_template)

    def _parse_template(self):
        sheet = cssutils.parseString(self.template)

        for rule in sheet:
            block_header = rule.selectorText

            current_block_name = DEFAULT_BLOCK_NAME
            if "#" in block_header:
                current_block_name = block_header[block_header.find("#") + 1 :]

            self.blocks[current_block_name] = StylesheetBlock(block_header + " {\n" + rule.style.cssText + ";} \n")
            setattr(self, current_block_name, self.blocks[current_block_name])

    @classmethod
    def read(cls, file: Path):
        dir_path = file.parent
        with open(dir_path / Path("style.css")) as f:
            data = f.read()
        return cls(data)


class StylesheetBlock(str):
    def __init__(self, template: str):
        self.template = template
        self._parse_template()

    def __add__(self, other):
        if not isinstance(other, StylesheetBlock):
            raise StylesheetException(f"Not implemented operator '+' for StylesheetBlock and {type(other)}", "info")
        self_sheet = cssutils.parseString(self.template)
        other_sheet = cssutils.parseString(other.template)
        header = ""
        self_body = ""
        other_body = ""
        for rule in self_sheet:
            header = rule.selectorText
            self_body = rule.style.cssText

        for rule in other_sheet:
            header = rule.selectorText
            other_body = rule.style.cssText

        return StylesheetBlock(header + " {\n" + self_body + ";\n" + other_body + ";} \n")

    def _parse_template(self):
        correspondences = {key: self.strip_units for key in CUSTOM_OPTIONS}
        correspondences.update({"geometry": self.strip_geometry})  # noqa
        correspondences.update({"margin": self.strip_margin})  # noqa

        sheet = cssutils.parseString(self.template)

        for rule in sheet:
            for option in rule.style:
                if "custom-" in option.name:
                    custom_option_name = option.name[option.name.find("custom-") + 7 :]

                    if custom_option_name not in CUSTOM_OPTIONS:
                        raise StylesheetException(f"fWrong custom option name: {custom_option_name}", "info")

                    setattr(self, custom_option_name, correspondences[custom_option_name](option.value))

    @staticmethod
    def strip_units(string: str):
        idx = 0
        for symbol in string:
            if symbol.isdigit():
                digit_string = symbol
                digit_idx = idx + 1
                while digit_idx < len(string):
                    if string[digit_idx].isdigit():
                        digit_string += string[digit_idx]

                    else:
                        return int(digit_string)
                    digit_idx += 1

                return int(digit_string)

            idx += 1

    @staticmethod
    def strip_margin(string: str):
        result = []
        for margin_part in string.split():
            if margin_part != " ":
                result.append(StylesheetBlock.strip_units(margin_part))

        return result

    @staticmethod
    def strip_geometry(string: str):
        result = []
        temp = string.replace("x", " ").replace("+", " ").replace(",", " ")
        for geometry_part in temp.split():
            if geometry_part != " ":
                result.append(StylesheetBlock.strip_units(geometry_part))

        return result


if __name__ == "__main__":
    filename = Path("./style.css")  # noqa
    TEST_STYLESHEET = Stylesheet.read(filename)
    print(TEST_STYLESHEET)
    TEST_STYLESHEET2 = Stylesheet.read(filename)
    test_sum = TEST_STYLESHEET + TEST_STYLESHEET2
    print(test_sum.test)
    #
