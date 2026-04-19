import pygame
from pygame import Surface
from VisualAsset import VisualAsset
from Laser import Laser
import util


ALIENASSET = util.image_asset("enemy_4.png")
with ALIENASSET.open() as img:
    ALIENIMG = pygame.image.load(img)


class Alien(VisualAsset):
    def __init__(self, screen: Surface, movementSpeed: float, spawnX: float, spawnY: float, sizeDivisorHeight: float = 1):
        super().__init__(screen, ALIENIMG, (screen.get_height() / sizeDivisorHeight) / ALIENIMG.get_height())

        self.speed = movementSpeed

        self.x = spawnX
        self.y = spawnY

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def is_touching_laser(self, lasers: list[Laser]) -> int | None:
        for index, laser in enumerate(lasers):
            if laser.is_overlapping(self.rect):
                return index
        return None