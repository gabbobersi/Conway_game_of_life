from game_scenes.scenes import Scenes
from UI_elements.color import Color

import pygame

class HomeScene:
    def __init__(self, options, ui_manager):
        self.options = options
        self.ui_manager = ui_manager
    
    def run(self):
        self.options.screen_update()    # Change resolution according to the actual options
        self.ui_manager.clear_elements()         # Clear the UI manager
        self.options.screen.fill(Color.WHITE.value)

        self.ui_manager.add_button('Start', 100, 50, Color.CUSTOM_RED.value)
        self.ui_manager.add_button('Option', 100, 50, Color.CUSTOM_RED.value)
        self.ui_manager.add_button('Quit', 100, 50, Color.CUSTOM_RED.value)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Scenes.QUIT.value
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = pygame.mouse.get_pos()

                    if self.ui_manager.get_element('Start').is_clicked(mouse_pos):
                        return Scenes.PLAY.value
                    elif self.ui_manager.get_element('Option').is_clicked(mouse_pos):
                        return Scenes.OPTION.value
                    elif self.ui_manager.get_element('Quit').is_clicked(mouse_pos):
                        return Scenes.QUIT.value

            self.ui_manager.draw()
            pygame.display.update()
            self.options.clock_tick()       