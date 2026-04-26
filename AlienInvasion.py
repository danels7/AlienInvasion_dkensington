"""
Alien Invasion - Alien Invasion Class
Daniel Kensington
This file defines the class AlienInvasion. This class serves as the "starting point" for pygame, as well as the "manager" for the program
4/12/2026
"""



WINDOWWIDTH = 1280
WINDOWHEIGHT = 720

import pygame
from Stage import Stage
from Game import Game
from Menu import Menu


class AlienInvasion:
    """This class represents the core of the program. It creates the pygame instance and handles the core loop of the program"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption("Alien Invasion")
        self.running = False
        self.clock = pygame.time.Clock()
        self.game = Game(self.screen, self.switchToMenu)
        self.menu = Menu(self.screen, self.switchToGame)
        self.currentStage: Stage = self.menu

    def switchToGame(self):
        self.currentStage = self.game
        self.game.new_game()

    def switchToMenu(self):
        self.currentStage = self.menu

    def run(self):
        """Runs the game"""
        self.running = True
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                else:
                    self.currentStage.process_event(event)

            self.currentStage.update(self.clock.tick() / 1000)