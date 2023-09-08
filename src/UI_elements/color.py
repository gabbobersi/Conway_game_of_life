"""
Defines some colors for the game.
"""
from enum import Enum

class Color(Enum):
    BLACK: tuple[int, int, int]= (0, 0, 0)
    WHITE: tuple[int, int, int]= (200, 200, 200)
    RED: tuple[int, int, int]= (255, 0, 0)
    GREEN: tuple[int, int, int]= (0, 255, 0)
    BLUE: tuple[int, int, int]= (0, 0, 255)
    GRAY: tuple[int, int, int]= (200, 200, 200)
    LIGHT_GREEN: tuple[int, int, int]= (17, 242, 174)

    CUSTOM_RED: tuple[int, int, int]= (255, 71, 71)
    CUSTOM_BLUE: tuple[int, int, int]= (71, 71, 255)
    CUSTOM_GREEN: tuple[int, int, int]= (71, 255, 71)
    CUSTOM_BLACK: tuple[int, int, int]= (71, 71, 71)
    CUSTOM_YELLOW: tuple[int, int, int]= (255, 255, 71)
    CUSTOM_WHITE: tuple[int, int, int]= (255, 255, 255)
    CUSTOM_GRAY: tuple[int, int, int]= (200, 200, 200)
    CUSTOM_LIGHT_GREEN: tuple[int, int, int]= (17, 242, 174)