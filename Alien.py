import pygame
from pygame import Surface
from VisualAsset import VisualAsset
from Laser import Laser
from AlienInvasion import WINDOWWIDTH, WINDOWHEIGHT
import util


ALIENASSET = util.image_asset("enemy_4.png")
with ALIENASSET.open() as img:
    _img = pygame.image.load(img)
    _multi = (WINDOWHEIGHT/12) / _img.get_height()
    ALIENIMG = pygame.image.load(img)


class Alien(VisualAsset):
    def __init__(self, screen: Surface, fleetId: int, movementSpeed: float, spawnX: float, spawnY: float):
        super().__init__(screen, ALIENIMG)

        self.id = fleetId

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
    
    def get_id(self):
        return self.id