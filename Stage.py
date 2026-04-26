"""
Alien Invasion - Stage Class
Daniel Kensington
This file defines the class Stage. It exists to allow the AlienInvasion class to easily switch between parts of the program
4/26/2026
"""


from pygame.event import Event
from abc import ABC, abstractmethod


class Stage(ABC):
    """This class allows the AlienInvasion class to easily switch between parts of the program"""

    @abstractmethod
    def process_event(self, event: Event) -> None:
        """Takes an event and determines what, if anything, to do with it"""
        ...

    @abstractmethod
    def update(self, dt: float) -> None:
        """Update the state of the Stage (deltatimed)"""
        ...