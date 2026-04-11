import pygame
from pygame import Surface
from pygame.event import Event
from Ship import Ship


class Game:
    def __init__(self, screen: Surface):
        self.screen = screen.subsurface(0, 0, screen.get_width(), screen.get_height())
        self.ship = Ship()

    def process_event(self, event: Event, dt: float) -> None:
        pass