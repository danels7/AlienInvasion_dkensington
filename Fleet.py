from pygame import Surface
from Alien import Alien
from AlienInvasion import WINDOWWIDTH, WINDOWHEIGHT
from Laser import Laser
from Ship import Ship
from Alien import ALIENIMG


class Fleet():
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
        for row in self.aliens:
            for alien in row:
                alien.draw()

    def remove_alien(self, id: int) -> None:
        expectedRow = id // self.width
        for index, alien in enumerate(self.aliens[expectedRow]):
            if alien.get_id() == id:
                self.aliens[expectedRow].pop(index)
                return
            
    def reset_fleet_pos(self) -> None:
        for row in self.aliens:
            for alien in row:
                alien.reset()

    def process_lasers(self, lasers: list[Laser]) -> list[int]:
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
        for row in self.aliens:
            for alien in row:
                if alien.is_touching_ship(ship):
                    return True
        return False