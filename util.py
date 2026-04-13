"""
AlienInvasion - Utility File
Daniel Kensington
This file if for supplemental functions to be used by the program
4/12/2026
"""


from pathlib import Path


CWD = Path.cwd()
ASSETS = Path.joinpath(CWD, "Assets")

FILE = Path.joinpath(ASSETS, "file")
FONTS = Path.joinpath(ASSETS, "Fonts")
IMAGES = Path.joinpath(ASSETS, "images")
SOUND = Path.joinpath(ASSETS, "sound")


def asset_path(subDir: str, fileName: str) -> Path:
    return Path.joinpath(ASSETS, subDir, fileName)

def file_asset(fileName: str) -> Path:
    return Path.joinpath(FILE, fileName)

def font_asset(fileName: str) -> Path:
    return Path.joinpath(FONTS, fileName)

def image_asset(fileName: str) -> Path:
    return Path.joinpath(IMAGES, fileName)

def sound_asset(fileName: str) -> Path:
    return Path.joinpath(SOUND, fileName)