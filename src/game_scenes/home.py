from game_scenes.scenes import Scenes
from UI_elements.color import Color
from UI_elements.button import Button

import pygame

class HomeScene:
    def __init__(self, options):
        self.options = options

    def run(self):
        self.options.screen.fill(Color.WHITE.value)
        middle_screen = (self.options.window_width - 100) // 2, (self.options.window_height - 200) // 2

        btn_Start = Button(self.options.screen.get_screen(), 'Start', True, middle_screen[0], middle_screen[1] - 150)
        btn_Option = Button(self.options.screen.get_screen(), 'Options', True, middle_screen[0], middle_screen[1] - 70)
        btn_Quit = Button(self.options.screen.get_screen(), 'Quit', True, middle_screen[0], middle_screen[1])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Scenes.QUIT.value
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = pygame.mouse.get_pos()
                    if btn_Start.is_clicked(mouse_pos):
                        return Scenes.PLAY.value
                    elif btn_Option.is_clicked(mouse_pos):
                        return Scenes.OPTION.value
                    elif btn_Quit.is_clicked(mouse_pos):
                        return Scenes.QUIT.value
            
            btn_Start.draw()
            btn_Option.draw()
            btn_Quit.draw()

            pygame.display.update()
            self.options.clock_tick()       