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
