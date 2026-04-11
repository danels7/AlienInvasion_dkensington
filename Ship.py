import pygame
import util


SHIPASSET = util.image_asset("ship2.png")

MOVESPEED = 512 # ship speed in px/sec


class Ship:
    def __init__(self):
        with SHIPASSET.open() as img:
            self.shipImg = pygame.image.load(img)

        self.x: float
        self.y: float

    def move_right(self, dt: float):
        self.x += MOVESPEED * dt

    def move_left(self, dt: float):
        self.x -= MOVESPEED * dt