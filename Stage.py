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
    def process_event(self, event: Event) -> None:
        """Takes an event and determines what, if anything, to do with it"""
        ...

    # optional
    def update(self, dt: float) -> None:
        """
        Optional implementation: Used to update the state of the Stage (deltatimed)
        If this function is not implemented, calling it is safe and will do nothing
        """
        ...