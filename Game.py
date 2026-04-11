import pygame
from pygame import Surface
from pygame.event import Event
from Ship import Ship


class Game:
    def __init__(self, screen: Surface):
        self.screen = screen.subsurface(0, 0, screen.get_width(), screen.get_height())
        self.ship = Ship(self.screen)

    def process_event(self, event: Event, dt: float) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.move_right(dt)
            elif event.key == pygame.K_LEFT:
                self.ship.move_left(dt)