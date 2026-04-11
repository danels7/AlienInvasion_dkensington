import pygame
from pygame import Surface
from pygame.event import Event
from Ship import Ship
import util


BACKGROUNDASSET = util.image_asset("Starbasesnow.png")


class Game:
    def __init__(self, screen: Surface):
        self.screen = screen.subsurface(0, 0, screen.get_width(), screen.get_height())
        self.ship = Ship(self.screen)

        with BACKGROUNDASSET.open() as bg:
            self.background = pygame.image.load(bg)
        self.screen.blit(self.background, self.screen.get_rect())

        # this is probably gonne be temporary
        # True = key is being held
        self.controls = {
            pygame.K_RIGHT: False,
            pygame.K_LEFT: False
        }

    def process_event(self, event: Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key in self.controls.keys():
                self.controls[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in self.controls.keys():
                self.controls[event.key] = False