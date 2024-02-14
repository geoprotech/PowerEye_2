from pathlib import Path


CUR_PATH = Path(__file__).parent

close_button_css: str

with open(CUR_PATH / Path("style.css")) as f:
    data = f.read()
LEFT_MENU_BUTTON_STYLESHEET = data

# LEFT_MENU_BUTTON_STYLESHEET = Stylesheet(LEFT_MENU_BUTTON_STYLESHEET_TEMPLATE)
# LEFT_MENU_BUTTON_STYLESHEET_HOVER = Stylesheet(LEFT_MENU_BUTTON_STYLESHEET_TEMPLATE_HOVER)
