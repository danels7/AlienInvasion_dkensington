from pathlib import Path


CWD = Path.cwd()
ASSETS = Path.joinpath(CWD, "Assets")


def asset_path(subDir: str, fileName: str) -> Path:
    return Path.joinpath(ASSETS, subDir, fileName)