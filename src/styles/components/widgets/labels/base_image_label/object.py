from pathlib import Path


CUR_PATH = Path(__file__).parent

with open(CUR_PATH / Path("style.css")) as f:
    data = f.read()
IMAGE_LABEL_STYLESHEET = data
