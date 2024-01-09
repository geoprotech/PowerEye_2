from bin.exceptions import StylesheetException


class Stylesheet:
    """
    Base class for all stylesheets. Based on Template. Used for qt elements stylesheet.
    """

    def __init__(self, template: dict[str, str]) -> None:
        if not isinstance(template, dict):
            raise StylesheetException("Wrong type for template", "DEBUG")
        self._template = template

    def __str__(self) -> str:
        string_representation = ""
        for key, val in self._template.items():
            if key != "geometry":
                string_representation += key + ":" + val + ";\n"
        return string_representation

    def __repr__(self) -> str:
        return str(self)

    def __getitem__(self, item: str) -> str:
        return self._template[item]

    def geometry(self) -> list[int]:
        """
        Returns the geometry of the stylesheet for proper usage in qt widgets and windows.
        :return list[int]:
        """
        if "geometry" not in self._template.keys():
            raise StylesheetException("No geometry in template", "DEBUG")
        geometry_list = self._template["geometry"].split("x")

        return [
            int(geometry_list[0]),
            int(geometry_list[1]),
            int(geometry_list[2]),
            int(geometry_list[3]),
        ]


BASE_STYLESHEET_TEMPLATE = {
    "geometry": "150x50x1298x730",
    "font-family": "Oxanium",
    "font": "10px",
    "background-color": "#F9F9F9",
}

BASE_STYLESHEET = Stylesheet(BASE_STYLESHEET_TEMPLATE)

MAIN_WINDOW_HEADER_STYLESHEET_TEMPLATE = {
    "font": "20px",
    "font-weight": "600",
    "background-color": "#28BFC9",
    "height": "68",
}

MAIN_WINDOW_HEADER_STYLESHEET = Stylesheet(MAIN_WINDOW_HEADER_STYLESHEET_TEMPLATE)

CLOSE_BUTTON_STYLESHEET_TEMPLATE = {
    "height": "20",
    "border": "None",
    "border-radius": "5",
    "margin-right": "15",
}

CLOSE_BUTTON_STYLESHEET_TEMPLATE_HOVER = {
    "height": "20",
    "border": "None",
    "border-radius": "5",
    "margin-right": "15",
    "background-color": "#28b3bd",
}

CLOSE_BUTTON_STYLESHEET = Stylesheet(CLOSE_BUTTON_STYLESHEET_TEMPLATE)
CLOSE_BUTTON_STYLESHEET_HOVER = Stylesheet(CLOSE_BUTTON_STYLESHEET_TEMPLATE_HOVER)
