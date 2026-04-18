import pygame
from Alien import Alien


class Fleet:
    def __init__(self, width: int, height: int):
        self.Aliens: list[list[Alien]] = []