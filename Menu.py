import pygame
from pygame import Surface
from Stage import Stage
from AlienInvasion import WINDOWWIDTH, WINDOWHEIGHT
from typing import override
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
    def __init__(self, screen: Surface):
        width = screen.get_width()
        height = screen.get_height()
        self.screen = screen.subsurface(0, 0, width, height)
        self.background = BACKGROUNDIMG.copy()
        self.playButton = PLAYBUTTON.copy()
