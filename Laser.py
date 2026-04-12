import pygame
from pygame import Rect
import util


LASERASSET = util.image_asset("laserBlast.png")
with LASERASSET.open() as img:
    LASERIMG = pygame.image.load(img)


class Laser:
    def __init__(self, shipRect: Rect):
        self.laserImg = pygame.transform.scale(LASERIMG, (shipRect.width, shipRect.height))

        self.rect = self.laserImg.get_rect()

        self.x = shipRect.x + (shipRect.width/2) - (self.rect.width/2)
        self.y = shipRect.y + self.rect.height
        
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)