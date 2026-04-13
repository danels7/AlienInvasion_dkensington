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
import util


SHIPASSET = util.image_asset("ship2.png")
with SHIPASSET.open() as img:
    SHIPIMG = pygame.image.load(img)

MOVESPEED = 512 # ship speed in px/sec


class Ship(VisualAsset):
    def __init__(self, screen: Surface):
        screenHeight = screen.get_height()
        screenWidth = screen.get_width()

        super().__init__(screen, SHIPIMG, (screenHeight/15) / SHIPIMG.get_height())

        self.xMin = 0
        self.xMax = screenWidth - self.rect.width
        self.yMin = 0
        self.yMax = screenHeight - self.rect.height

        self.x = (screenWidth / 2) - (self.rect.width / 2)
        self.y = screenHeight - self.rect.height
        
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def move_right(self, dt: float) -> None:
        self.x = pygame.math.clamp(self.x + (MOVESPEED * dt), self.xMin, self.xMax)
        self.rect.x = round(self.x)

    def move_left(self, dt: float) -> None:
        self.x = pygame.math.clamp(self.x - (MOVESPEED * dt), self.xMin, self.xMax)
        self.rect.x = round(self.x)

    def move_up(self, dt: float) -> None:
        self.y = pygame.math.clamp(self.y - (MOVESPEED * dt), self.yMin, self.yMax)
        self.rect.y = round(self.y)

    def move_down(self, dt: float) -> None:
        self.y = pygame.math.clamp(self.y + (MOVESPEED * dt), self.yMin, self.yMax)
        self.rect.y = round(self.y)

    def fire_laser(self) -> Laser:
        return Laser(self.parent, self.rect)