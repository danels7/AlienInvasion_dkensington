import pygame
from pygame import Surface
import util


SHIPASSET = util.image_asset("ship2.png")
with SHIPASSET.open() as img:
    SHIPIMG = pygame.image.load(img)

MOVESPEED = 512 # ship speed in px/sec


class Ship:
    def __init__(self, screen: Surface):
        self.screen = screen

        screenHeight = self.screen.get_height()
        screenWidth = self.screen.get_width()

        self.rect = SHIPIMG.get_rect()
        scale = (screenHeight/15) / self.rect.height
        self.rect.scale_by_ip(scale, scale)
        self.shipImg = pygame.transform.scale(SHIPIMG, (self.rect.width, self.rect.height))

        self.xMin = 0
        self.xMax = screenWidth - self.rect.width
        self.yMin = 0
        self.yMax = screenHeight

        self.x = (screenWidth / 2) - (self.rect.width / 2)
        self.y = screenHeight - self.rect.height
        
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        
        self.draw()

    def move_right(self, dt: float) -> None:
        self.x = pygame.math.clamp(self.x + (MOVESPEED * dt), self.xMin, self.xMax)
        self.rect.x = round(self.x)
        

    def move_left(self, dt: float) -> None:
        self.x = pygame.math.clamp(self.x - (MOVESPEED * dt), self.xMin, self.xMax)
        self.rect.x = round(self.x)

    def draw(self) -> None:
        self.screen.blit(self.shipImg, self.rect)
