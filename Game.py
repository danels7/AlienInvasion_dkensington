import pygame
from pygame import Surface
from pygame.event import Event
from Ship import Ship
import util


BACKGROUNDASSET = util.image_asset("Starbasesnow.png")
with BACKGROUNDASSET.open() as img:
    BACKGROUNDIMG = pygame.image.load(img)


class Game:
    def __init__(self, screen: Surface):
        width = screen.get_width()
        height = screen.get_height()
        self.screen = screen.subsurface(0, 0, width, height)
        self.ship = Ship(self.screen)

        self.background = BACKGROUNDIMG.copy()

        self.screen.blit(self.background, self.screen.get_rect())

        # this is probably gonne be temporary
        # True = key is being held
        self.controls = {
            pygame.K_RIGHT: False,
            pygame.K_LEFT: False,
            pygame.K_UP: False,
            pygame.K_DOWN: False
        }

    def process_event(self, event: Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key in self.controls.keys():
                self.controls[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in self.controls.keys():
                self.controls[event.key] = False

    def update(self, dt: float) -> None:
        if self.controls[pygame.K_RIGHT] and not self.controls[pygame.K_LEFT]:
            self.ship.move_right(dt)
        elif self.controls[pygame.K_LEFT] and not self.controls[pygame.K_RIGHT]:
            self.ship.move_left(dt)

        if self.controls[pygame.K_RIGHT] and not self.controls[pygame.K_UP]:
            self.ship.move_up(dt)
        elif self.controls[pygame.K_LEFT] and not self.controls[pygame.K_DOWN]:
            self.ship.move_down(dt)
        
        self.screen.blit(self.background, self.screen.get_rect())
        self.ship.draw()