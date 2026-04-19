"""
Alien Invastion - Visual Asset Class
Daniel Kensington
This file defines the abstract base class VisualAsset, used for classes that represent visual assets
4/12/2026
"""


from pygame import Surface
from abc import ABC


class VisualAsset(ABC):
    """This is an abstract base class for classes that represent visual assets"""

    def __init__(self, parentScreen: Surface, img: Surface):
        self.img = img.copy()
        self.rect = self.img.get_rect()
        self.parent = parentScreen

    def draw(self) -> None:
        """Draws the asset image on the parent screen"""
        self.parent.blit(self.img, self.rect)