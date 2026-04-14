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
import util


LASERASSET = util.image_asset("laserBlast.png")
with LASERASSET.open() as img:
    LASERIMG = pygame.image.load(img)


MOVESPEED = 576


class Laser(VisualAsset):
    """This class represents the lasers fired by the player's ship"""

    def __init__(self, screen: Surface, shipRect: Rect):
        super().__init__(screen, LASERIMG, shipRect.height / LASERIMG.get_height())

        self.rect = self.img.get_rect()

        self.x = shipRect.x + (shipRect.width/2) - (self.rect.width/2)
        self.y = shipRect.y - self.rect.height
        
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

        self.yMin = -self.rect.height
        self.yMax = self.parent.get_height()
        self.xMin = -self.rect.width
        self.xMax = self.parent.get_width()
        self.toppedOut = False

    def move_up(self, dt: float) -> None:
        """Move the laser up"""
        self.y -= MOVESPEED * dt
        self.rect.y = round(self.y)
        if self.rect.y == self.yMin:
            self.toppedOut = True

    def is_off_screen(self) -> bool:
        """Returns True if the laser has moved up off the screen, False otherwise"""
        return self.toppedOut