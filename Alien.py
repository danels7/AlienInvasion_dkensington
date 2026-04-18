import pygame
from VisualAsset import VisualAsset
import util


ALIENASSET = util.image_asset("enemy_4.png")
with ALIENASSET.open() as img:
    ALIENIMG = pygame.image.load(img)


class Alien(VisualAsset):
    def __init__(self):
        pass