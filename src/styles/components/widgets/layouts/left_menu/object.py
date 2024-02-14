from pathlib import Path


CUR_PATH = Path(__file__).parent

close_button_css: str

with open(CUR_PATH / Path("style.css")) as f:
    data = f.read()
LEFT_MENU_STYLESHEET = data
