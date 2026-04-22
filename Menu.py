import pygame
from pygame import Surface
import util


BACKGROUNDASSET = util.image_asset("Starbasesnow.png")
with BACKGROUNDASSET.open() as img:
    BACKGROUNDIMG = pygame.image.load(img)


class Menu:
    def __init__(self, screen: Surface):
        width = screen.get_width()
        height = screen.get_height()
        self.screen = screen.subsurface(0, 0, width, height)
        self.background = BACKGROUNDIMG.copy()
