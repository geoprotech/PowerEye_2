from pathlib import Path


def stylesheet(file):
    CUR_PATH = Path(file).parent
    with open(CUR_PATH / Path("style.css")) as f:
        data = f.read()
    return data
