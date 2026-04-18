import pygame
from pygame import Surface
from VisualAsset import VisualAsset
import util


ALIENASSET = util.image_asset("enemy_4.png")
with ALIENASSET.open() as img:
    ALIENIMG = pygame.image.load(img)


class Alien(VisualAsset):
    def __init__(self, screen: Surface, spawnX: float, spawnY: float):
        super().__init__(screen, ALIENIMG, (screen.get_height() / 12) / ALIENIMG.get_height())

        self.x = spawnX
        self.y = spawnY

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)