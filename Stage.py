"""
Alien Invasion - Stage Class
Daniel Kensington
This file defines the class Stage. It exists to allow the AlienInvasion class to easily switch between parts of the program
"""


from pygame.event import Event
from abc import ABC, abstractmethod


class Stage(ABC):
    """This class allows the AlienInvasion class to easily switch between parts of the program"""

    @abstractmethod
    def process_event(self, event: Event) -> None: ...