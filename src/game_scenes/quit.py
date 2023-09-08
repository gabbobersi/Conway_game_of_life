import sys

import pygame

class QuitScene:
    def __init__(self, options):
        self.options = options      # For now is idle

    @staticmethod
    def run() -> None:
        print("Game is closing correctly.")
        pygame.quit()
        sys.exit()