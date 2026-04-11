import pygame
from Game import Game


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Alien Invasion")
        self.running = False
        self.game = Game(self.screen)

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.game.handle_events(events)

            pygame.display.flip()