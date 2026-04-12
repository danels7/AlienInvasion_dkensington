import pygame
from pygame import Surface


class VisualAsset:
    def __init__(self, parentScreen: Surface, img: Surface, imgScale: float | None = None):
        if imgScale is None:
            self.img = img.copy()
        else:
            width = img.get_width() * imgScale
            height = img.get_height() * imgScale
            self.img = pygame.transform.scale(img, (width, height))
        self.rect = img.get_rect()
        self.parent = parentScreen

    def draw(self) -> None:
        self.parent.blit(self.img, self.rect)