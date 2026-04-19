"""
Alien Invasion - Ship Class
Daniel Kensington
The file defines the class Ship. It represents the ship that the player controls
This class inherits from VisualAsset. 
4/12/2026
"""


import pygame
from pygame import Surface
from VisualAsset import VisualAsset
from Laser import Laser
from AlienInvasion import WINDOWWIDTH, WINDOWHEIGHT
import util


SHIPASSET = util.image_asset("ship2.png")
with SHIPASSET.open() as img:
    _img = pygame.image.load(img)
    _multi = (WINDOWHEIGHT/15) / _img.get_height()
    SHIPIMG = pygame.transform.scale(_img, (_img.get_width() * _multi, _img.get_height() * _multi))
    del _img, _multi

MOVESPEED = 512 # ship speed in px/sec


class Ship(VisualAsset):
    """This class represents the ship that the player controls"""

    def __init__(self, screen: Surface):
        screenHeight = screen.get_height()
        screenWidth = screen.get_width()

        super().__init__(screen, SHIPIMG)

        self.xMin = 0
        self.xMax = screenWidth - self.rect.width
        self.yMin = 0
        self.yMax = screenHeight - self.rect.height

        self.x = (screenWidth / 2) - (self.rect.width / 2)
        self.y = screenHeight - self.rect.height
        
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

        self.rotState = 0  #  0 = up, 1 = left, 2 = down, 3 = right

    def move_right(self, dt: float) -> None:
        """Move the ship right"""
        self.x = pygame.math.clamp(self.x + (MOVESPEED * dt), self.xMin, self.xMax)
        self.rect.x = round(self.x)

    def move_left(self, dt: float) -> None:
        """Move the ship left"""
        self.x = pygame.math.clamp(self.x - (MOVESPEED * dt), self.xMin, self.xMax)
        self.rect.x = round(self.x)

    def move_up(self, dt: float) -> None:
        """Move the ship up"""
        self.y = pygame.math.clamp(self.y - (MOVESPEED * dt), self.yMin, self.yMax)
        self.rect.y = round(self.y)

    def move_down(self, dt: float) -> None:
        """Move the ship down"""
        self.y = pygame.math.clamp(self.y + (MOVESPEED * dt), self.yMin, self.yMax)
        self.rect.y = round(self.y)

    def turn_left(self) -> None:
        """Turn the ship left (counter-clockwise)"""
        self.img = pygame.transform.rotate(self.img, 90)
        self.rect = self.img.get_rect(center=self.rect.center)
        self.rotState = (self.rotState + 1) % 4

    def turn_right(self) -> None:
        """Turn the ship right (clockwise)"""
        self.img = pygame.transform.rotate(self.img, -90)
        self.rect = self.img.get_rect(center=self.rect.center)
        self.rotState = (self.rotState - 1) % 4

    def fire_laser(self) -> Laser:
        """Fire a laser. Returns the Laser instance that was created"""
        return Laser(self.parent, self.rect, self.rotState)