"""
Alien Invasion - Game Class
Daniel Kensington
This file defines the class Game. It is responsible for managing the game itself
4/12/2026
"""


import pygame
from pygame import Surface
from pygame.event import Event
from Ship import Ship
from Laser import Laser
from Fleet import Fleet
import time
import util


BACKGROUNDASSET = util.image_asset("Starbasesnow.png")
with BACKGROUNDASSET.open() as img:
    BACKGROUNDIMG = pygame.image.load(img)

MAXLASERS = 5 # maximum lasers on screen

class Game:
    """This class manages the game itself. It handles controls, events, assets, etc."""

    def __init__(self, screen: Surface):
        width = screen.get_width()
        height = screen.get_height()
        self.screen = screen.subsurface(0, 0, width, height)
        self.ship = Ship(self.screen)
        self.fleet = Fleet(self.screen, 15, 5, 30)

        self.background = BACKGROUNDIMG.copy()

        self.screen.blit(self.background, self.screen.get_rect())

        self.lasers: list[Laser] = []

        self.respawning = False
        self.lastDeathTime = 0

        self.controls = {
            pygame.K_RIGHT: False,
            pygame.K_LEFT: False,
            pygame.K_UP: False,
            pygame.K_DOWN: False
        }

    def process_event(self, event: Event) -> None:
        """Takes an event and determines what, if anything, to do with it"""

        if event.type == pygame.KEYDOWN:
            if event.key in self.controls.keys():
                self.controls[event.key] = True
            elif event.key == pygame.K_c:
                if len(self.lasers) < MAXLASERS:
                    self.lasers.append(self.ship.fire_laser())
            elif event.key == pygame.K_z:
                self.ship.turn_left()
            elif event.key == pygame.K_x:
                self.ship.turn_right()
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

        elif event.type == pygame.KEYUP:
            if event.key in self.controls.keys():
                self.controls[event.key] = False

    def draw(self):
        self.screen.blit(self.background, self.screen.get_rect())
        for laser in self.lasers:
            if laser.is_off_screen():
                self.lasers.remove(laser)
            else:
                laser.draw()
        self.ship.draw()
        self.fleet.draw_fleet()
        pygame.display.flip()

    def update(self, dt: float) -> None:
        """Does what is necessary to update the state of assets, then redraws them"""

        if self.respawning:
            if self.lastDeathTime + 2 <= time.time():
                self.respawning = False
                self.draw()
            else:
                if self.lastDeathTime + 1 <= time.time():
                    self.ship = Ship(self.screen)
                    self.fleet.reset_fleet_pos()
                self.draw()
                return
        
        if self.controls[pygame.K_RIGHT] and not self.controls[pygame.K_LEFT]:
            self.ship.move_right(dt)
        elif self.controls[pygame.K_LEFT] and not self.controls[pygame.K_RIGHT]:
            self.ship.move_left(dt)

        if self.controls[pygame.K_DOWN] and not self.controls[pygame.K_UP]:
            self.ship.move_down(dt)
        elif self.controls[pygame.K_UP] and not self.controls[pygame.K_DOWN]:
            self.ship.move_up(dt)

        for laser in self.lasers:
            laser.move(dt)

        lasersToRemove = sorted(self.fleet.process_lasers(self.lasers), reverse=True)
        for index in lasersToRemove:
            self.lasers.pop(index)

        self.draw()

        if self.fleet.check_ship_collision(self.ship):
            self.respawning = True
            self.lastDeathTime = time.time()