"""
Alien Invasion - Laser Class
Daniel Kensington
This file defines the class Laser. It represents the lasers fired by the player's ship
This class inherits from VisualAsset.
4/12/2026
"""


import pygame
from pygame import Surface, Rect
from VisualAsset import VisualAsset
from Ship import SHIPIMG
import util


LASERASSET = util.image_asset("laserBlast.png")
with LASERASSET.open() as img:
    _img = pygame.image.load(img)
    _multi = SHIPIMG.get_height() / _img.get_height()
    LASERIMG = pygame.image.load(img)


MOVESPEED = 576


class Laser(VisualAsset):
    """This class represents the lasers fired by the player's ship"""

    def __init__(self, screen: Surface, shipRect: Rect, rotState: int):
        if rotState % 2 == 0: # 0 or 2 (up or down)
            super().__init__(screen, LASERIMG)
        else: # 1 or 3 (left or right)
            img = pygame.transform.rotate(LASERIMG, 90)
            super().__init__(screen, img)

        self.rect = self.img.get_rect()

        placeX = shipRect.centerx
        placeY = shipRect.centery

        halfWidth = shipRect.width / 2
        halfHeight = shipRect.height / 2

        self.dx = 0
        self.dy = 0

        if rotState == 0: # up
            placeY -= halfHeight + self.rect.height
            placeX -= halfWidth
            self.dy = -MOVESPEED
        elif rotState == 1: # left
            placeX -= halfWidth + self.rect.width
            placeY -= halfHeight
            self.dx = -MOVESPEED
        elif rotState == 2: # down
            placeY += halfHeight
            placeX -= halfWidth
            self.dy = MOVESPEED
        else: # right (3)
            placeX += halfWidth
            placeY -= halfHeight
            self.dx = MOVESPEED 

        self.x = placeX
        self.y = placeY

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

        self.yMin = -self.rect.height
        self.yMax = self.parent.get_height()
        self.xMin = -self.rect.width
        self.xMax = self.parent.get_width()
        self.offScreen = False

    def move(self, dt: float) -> None:
        """Move the laser"""
        self.x += self.dx * dt
        self.y += self.dy * dt
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        if self.rect.x <= self.xMin or self.rect.x >= self.xMax or self.rect.y <= self.yMin or self.rect.y >= self.yMax:
            self.offScreen = True

    def is_off_screen(self) -> bool:
        """Returns True if the laser has moved up off the screen, False otherwise"""
        return self.offScreen
    
    def is_overlapping(self, rect: Rect) -> bool:
        return self.rect.colliderect(rect)