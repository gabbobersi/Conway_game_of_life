from enum import Enum


class Scenes(Enum):
    PLAY = 'play'         # Game is running.
    HOME = 'home'         # Main menu is displayed. User can't interact with the grid. Animation is played.
    OPTION = 'option'     # Option menu is displayed. User can't interact with the grid.
    QUIT = 'quit'         # Default state in case of fault.
    VALID = (PLAY, HOME, OPTION, QUIT)