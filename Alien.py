import pygame
from pygame import Surface
from VisualAsset import VisualAsset
from Laser import Laser
from Ship import Ship
from AlienInvasion import WINDOWHEIGHT
import util


ALIENASSET = util.image_asset("enemy_4.png")
with ALIENASSET.open() as img:
    _img = pygame.image.load(img)
    _multi = (WINDOWHEIGHT/12) / _img.get_height()
    ALIENIMG = pygame.transform.scale(_img, (_img.get_width() * _multi, _img.get_height() * _multi))


class Alien(VisualAsset):
    def __init__(self, screen: Surface, fleetId: int, movementSpeed: float, spawnX: float, spawnY: float):
        super().__init__(screen, ALIENIMG)

        self.id = fleetId

        self.speed = movementSpeed

        self.spawnX = spawnX
        self.spawnY = spawnY

        self.x = spawnX
        self.y = spawnY

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def is_touching_laser(self, lasers: list[Laser]) -> int | None:
        for index, laser in enumerate(lasers):
            if laser.is_overlapping(self.rect):
                return index
        return None
    
    def is_touching_ship(self, ship: Ship) -> bool:
        return ship.is_overlapping(self.rect)
    
    def get_id(self) -> int:
        return self.id
    
    def reset(self) -> None:
        self.x = self.spawnX
        self.y = self.spawnY
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
