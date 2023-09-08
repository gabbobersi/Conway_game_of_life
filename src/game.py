from options import Options
from game_scenes.scenes import Scenes
from game_scenes.home import HomeScene
from game_scenes.play import PlayScene
from game_scenes.option import OptionScene
from game_scenes.quit import QuitScene

import pygame


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.options = Options()      
        self.scene = Scenes.HOME.value    # Starting scene

    def run(self):
        if self.scene not in Scenes.VALID.value:
            print("Error :: Invalid game state {}. I'm exiting...".format(self.scene))
            self.scene = Scenes.QUIT.value

        while True:
            if self.scene == Scenes.HOME.value:
                print("Starting home scene...")
                scene = HomeScene(self.options)
                self.scene = scene.run()

            elif self.scene == Scenes.OPTION.value:
                print("Starting option scene...")
                scene = OptionScene(self.options)
                self.scene = scene.run()
            
            elif self.scene == Scenes.PLAY.value:
                print("Starting play scene...")
                scene = PlayScene(self.options)
                self.scene = scene.run()
            
            elif self.scene == Scenes.QUIT.value:
                print("Starting quit scene...")
                scene = QuitScene(self.options)
                self.scene = scene.run()
