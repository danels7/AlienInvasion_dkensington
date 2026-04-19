import pygame
from pygame import Surface
from Alien import Alien


class Fleet():
    def __init__(self, screen: Surface, fleetWidth: int, fleetHeight: int, alienSpeed: float):
        offset = 20
        spawnAreaWidth = screen.get_width() - (offset * 2)
        spawnAreaHeight = screen.get_height() * 0.45

        dx = spawnAreaWidth / fleetWidth
        dy = spawnAreaHeight / fleetHeight

        alienHeightDivisor = (screen.get_height() / spawnAreaHeight) * fleetHeight

        self.Aliens: list[list[Alien]] = []

        alienId = 1
        for y in range(fleetWidth):
            row: list[Alien] = []
            for x in range(fleetHeight):
                row.append(Alien(screen, alienId, alienSpeed, (x*dx)+offset, (y*dy)+offset, alienHeightDivisor))
                alienId += 1
            self.Aliens.append(row)

    def draw_fleet(self) -> None:
        for row in self.Aliens:
            for alien in row:
                alien.draw()