import pygame
from pygame import Surface
from pygame.event import Event


class Game:
    def __init__(self, screen: Surface):
        self.screen = screen.subsurface(0, 0, screen.get_width(), screen.get_height())

    def handle_events(self, events: list[Event]) -> None:
        for event in events:
            pass