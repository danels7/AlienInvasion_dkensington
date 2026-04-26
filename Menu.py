"""
Alien Invasion - Menu Class
Daniel Kensington
This file defines the class Menu. It represents the menu that is displayed before the main game
4/26/2026
"""


import pygame
from pygame import Surface
from pygame.event import Event
from Stage import Stage
from AlienInvasion import WINDOWWIDTH, WINDOWHEIGHT
from typing import override
from collections.abc import Callable
import util


BACKGROUNDASSET = util.image_asset("Starbasesnow.png")
with BACKGROUNDASSET.open() as img:
    BACKGROUNDIMG = pygame.image.load(img)


pygame.font.init()
FONTASSET = util.font_asset("Silkscreen-Regular.ttf")
FONT = pygame.font.Font(FONTASSET, 50)

PLAYBUTTON = FONT.render("PLAY", False, pygame.Color(0xff, 0xff, 0xff), pygame.Color(0x00, 0xff, 0x00))
PLAYBUTTONRECT = PLAYBUTTON.get_rect()
PLAYBUTTONRECT.x = round((WINDOWWIDTH/2) - (PLAYBUTTONRECT.width/2))
PLAYBUTTONRECT.y = round((WINDOWHEIGHT/2) - (PLAYBUTTONRECT.height/2))


class Menu(Stage):
    """This class represents the menu that is displayed before the main game"""

    def __init__(self, screen: Surface, startGame: Callable[[], None]):
        self.screen = screen.subsurface(0, 0, WINDOWWIDTH, WINDOWHEIGHT)
        self.background = BACKGROUNDIMG.copy()
        self.playButton = PLAYBUTTON.copy()
        self.startCallback = startGame

    @override
    def process_event(self, event: Event) -> None:
        """Processes events. Only checks if the play button has been clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left mouse button
                if PLAYBUTTONRECT.collidepoint(event.pos):
                    self.startCallback()

    @override
    def update(self, dt: float) -> None:
        """Draws the necessary elements"""
        self.screen.blit(self.background, self.screen.get_rect())
        self.screen.blit(self.playButton, PLAYBUTTONRECT)