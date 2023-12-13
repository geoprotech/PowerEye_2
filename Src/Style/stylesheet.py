class Stylesheet:
    """
    Base class for all stylesheets. Based on Template. Used for qt elements stylesheet.
    """

    def __init__(self, template):
        assert type(template) is dict
        self._template = template

    def __str__(self):
        string_representation = ""
        for key, val in self._template.items():
            string_representation += key + ":" + val + ";\n"
        return string_representation

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        return self._template[item]

    def geometry(self):
        """
        Returns the geometry of the stylesheet for proper usage in qt widgets and windows.
        :return list[int]:
        """
        assert "geometry" in self._template.keys(), "No geometry in template."
        return [
            int(self._template["geometry"].split("x")[0]),
            int(self._template["geometry"].split("x")[1]),
            int(self._template["geometry"].split("x")[2]),
            int(self._template["geometry"].split("x")[3]),
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

MAIN_WINDOW_HEADER_STYLESHEET = Stylesheet(
    MAIN_WINDOW_HEADER_STYLESHEET_TEMPLATE
)
