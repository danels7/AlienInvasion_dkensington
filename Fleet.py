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

        self.aliens: list[list[Alien]] = []

        self.width = fleetWidth

        alienId = 0
        for y in range(fleetHeight):
            row: list[Alien] = []
            for x in range(fleetWidth):
                row.append(Alien(screen, alienId, alienSpeed, (x*dx)+offset, (y*dy)+offset, alienHeightDivisor))
                alienId += 1
            self.aliens.append(row)

    def draw_fleet(self) -> None:
        for row in self.aliens:
            for alien in row:
                alien.draw()

    def remove_alien(self, id: int):
        expectedRow = id // self.width
        for index, alien in enumerate(self.aliens[expectedRow]):
            if alien.get_id() == id:
                self.aliens[expectedRow].pop(index)
                return