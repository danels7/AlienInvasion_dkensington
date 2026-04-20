"""
Alien Invasion - Alien Class
Daniel Kensington
This file defines the class Alien. It represents the aliens that the player is fighting
This class inherits from Visual Asset
4/19/2026
"""


import pygame
from pygame import Surface
from math import sin, cos, atan2
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
    """This class represents the aliens that the player is fighting"""

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
        """Check if the alien is touching a laser. Returns the index of the first laser it detects, else None"""
        for index, laser in enumerate(lasers):
            if laser.is_overlapping(self.rect):
                return index
        return None
    
    def is_touching_ship(self, ship: Ship) -> bool:
        """Returns True if the alien is touching ship"""
        return ship.is_overlapping(self.rect)
    
    def get_id(self) -> int:
        """Returns the alien's unique fleet id"""
        return self.id
    
    def reset(self) -> None:
        """Resets the alien to its original starting position"""
        self.x = self.spawnX
        self.y = self.spawnY
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def move_toward_ship(self, shipCenter: tuple[int, int], dt: float) -> None:
        """Moves the alien toward the ship"""
        shipX = shipCenter[0]
        shipY = shipCenter[1]

        x = shipX - self.x
        y = shipY - self.y

        angle = atan2(y, x)

        dx = cos(angle) * self.speed * dt
        dy = sin(angle) * self.speed * dt

        self.x += dx
        self.y += dy

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)