import pygame
import util


SHIPASSET = util.image_asset("ship2.png")


class Ship:
    def __init__(self):
        with SHIPASSET.open() as img:
            self.shipImg = pygame.image.load(img)

        self.x: int
        self.y: int
        