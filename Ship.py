import pygame
from pygame import Surface
import util


SHIPASSET = util.image_asset("ship2.png")

MOVESPEED = 512 # ship speed in px/sec


class Ship:
    def __init__(self, screen: Surface, height: int):
        with SHIPASSET.open() as img:
            self.shipImg = pygame.image.load(img)

        self.rect = self.shipImg.get_rect()
        self.rect.height = height
        self.rect.width = round((height/self.shipImg.get_height()) * self.shipImg.get_width())

        self.screen = screen

        self.x = (self.screen.get_width() / 2) - (self.rect.width / 2)
        self.y = self.screen.get_height() - self.rect.height
        
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        
        self.draw()

    def move_right(self, dt: float) -> None:
        self.x += MOVESPEED * dt
        self.rect.x = round(self.x)

    def move_left(self, dt: float) -> None:
        self.x -= MOVESPEED * dt
        self.rect.x = round(self.x)

    def draw(self) -> None:
        self.screen.blit(self.shipImg, self.rect)
