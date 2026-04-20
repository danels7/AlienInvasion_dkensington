"""
Alien Invasion - Fleet Class
Daniel Kensington
This file defines the class Fleet. It is responsible for manage all of the aliens within a fleet of aliens
4/19/2026
"""


from pygame import Surface
from Alien import Alien
from AlienInvasion import WINDOWWIDTH, WINDOWHEIGHT
from Laser import Laser
from Ship import Ship
from Alien import ALIENIMG


class Fleet:
    """This class represents and manages a fleet of aliens"""

    def __init__(self, screen: Surface, fleetWidth: int, fleetHeight: int, alienSpeed: float):
        offset = 20
        spawnAreaWidth = WINDOWWIDTH - (offset * 2)
        spawnAreaHeight = WINDOWHEIGHT * 0.45

        dx = spawnAreaWidth / fleetWidth
        dy = spawnAreaHeight / fleetHeight

        self.aliens: list[list[Alien]] = []

        self.width = fleetWidth

        extra = abs(ALIENIMG.get_width() - dx) / fleetWidth

        alienId = 0
        for y in range(fleetHeight):
            row: list[Alien] = []
            for x in range(fleetWidth):
                row.append(Alien(screen, alienId, alienSpeed, (x*dx)+offset+(extra*x), (y*dy)+offset))
                alienId += 1
            self.aliens.append(row)

    def draw_fleet(self) -> None:
        """Calls draw on each alien"""
        for row in self.aliens:
            for alien in row:
                alien.draw()

    def remove_alien(self, id: int) -> None:
        """Removes the alien with the given id, if found"""
        expectedRow = id // self.width
        for index, alien in enumerate(self.aliens[expectedRow]):
            if alien.get_id() == id:
                self.aliens[expectedRow].pop(index)
                return
            
    def reset_fleet_pos(self) -> None:
        """Calls reset on each alien"""
        for row in self.aliens:
            for alien in row:
                alien.reset()

    def process_lasers(self, lasers: list[Laser]) -> list[int]:
        """Calls is_touching_laser on each alien and handles destroying the alien"""
        laserList = [laser for laser in lasers]
        laserIndexes: list[int] = []
        for row in self.aliens:
            for alien in row:
                index = alien.is_touching_laser(laserList)
                if index is not None:
                    laserIndexes.append(index)
                    laserList.pop(index)
                    self.remove_alien(alien.get_id())
        return laserIndexes
    
    def check_ship_collision(self, ship: Ship) -> bool:
        """Call is_touching_ship on each alien, return True if any return True"""
        for row in self.aliens:
            for alien in row:
                if alien.is_touching_ship(ship):
                    return True
        return False
    
    def is_fleet_empty(self) -> bool:
        """Returns True if there are no aliens left"""
        for row in self.aliens:
            if len(row) != 0:
                return False
        return True
    
    def update_positions(self, ship: Ship, dt: float) -> None:
        """Calls move_toward_ship on each alien"""
        for row in self.aliens:
            for alien in row:
                alien.move_toward_ship(ship.get_center(), dt)