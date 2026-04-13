import pygame
from pygame import Surface, Rect
from VisualAsset import VisualAsset
import util


LASERASSET = util.image_asset("laserBlast.png")
with LASERASSET.open() as img:
    LASERIMG = pygame.image.load(img)


MOVESPEED = 576


class Laser(VisualAsset):
    def __init__(self, screen: Surface, shipRect: Rect):
        super().__init__(screen, LASERIMG, shipRect.height / LASERIMG.get_height())

        self.rect = self.img.get_rect()

        self.x = shipRect.x + (shipRect.width/2) - (self.rect.width/2)
        self.y = shipRect.y + self.rect.height
        
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def move_up(self, dt: float) -> None:
        self.y -= MOVESPEED * dt
        self.rect.y = round(self.y)