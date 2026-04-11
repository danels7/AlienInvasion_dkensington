import pygame
from pygame import Surface
import util


SHIPASSET = util.image_asset("ship2.png")

MOVESPEED = 512 # ship speed in px/sec


class Ship:
    def __init__(self, screen: Surface):
        with SHIPASSET.open() as img:
            shipImg = pygame.image.load(img)

        screenHeight = screen.get_height()
        screenWidth = screen.get_width()

        self.rect = shipImg.get_rect()
        scale = (screenHeight/15) / self.rect.height
        self.rect.scale_by_ip(scale, scale)
        self.shipImg = pygame.transform.scale(shipImg, (self.rect.width, self.rect.height))
        del shipImg

        self.screen = screen

        self.x = (screenWidth / 2) - (self.rect.width / 2)
        self.y = screenHeight - self.rect.height
        
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
