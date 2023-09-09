from UI_elements.color import Color
from UI_elements.button import Button
from game_scenes.scenes import Scenes

import pygame

class OptionScene:
    def __init__(self, options, ui_manager):
        self.options = options
        self.ui_manager = ui_manager

        # Available settings to change
        self.tmp_toolbar_pos = self.options.get_actual_value('toolbar')
        self.tmp_player_color = self.options.get_actual_value('player_color')
        self.tmp_resolution = self.options.get_actual_value('resolution')
        self.tmp_tick_speed = self.options.get_actual_value('tick_speed')

    def run(self):
        self.ui_manager.clear_elements()         # Clear the UI manager
        self.options.screen.fill(Color.WHITE.value)

        self.ui_manager.add_button('Toolbar: {}'.format(self.tmp_toolbar_pos.get('name')), 300, 50, Color.CUSTOM_RED.value)
        self.ui_manager.add_button('Resolution: {}'.format(self.tmp_resolution.get('name')), 300, 50, Color.CUSTOM_RED.value)
        self.ui_manager.add_button('Player color: {}'.format(self.tmp_player_color.get('name')), 300, 50, Color.CUSTOM_RED.value)
        self.ui_manager.add_button('Game speed: {}'.format(self.tmp_tick_speed.get('name')), 300, 50, Color.CUSTOM_RED.value)
        self.ui_manager.add_button('Main menu', 300, 50, Color.CUSTOM_RED.value)
        
        # middle_screen = (self.options.window_width - 100) // 2, (self.options.window_height - 200) // 2
        # btn_toolbar_position =  Button(self.options.screen.get_screen(), 'Toolbar: {}'.format(self.tmp_toolbar_pos.get('name')), True,
        #                                 middle_screen[0] - distance_from_center, middle_screen[1] - 220, 300)
        
        # btn_change_resolution = Button(self.options.screen.get_screen(), 'Resolution: {}'.format(self.tmp_resolution.get('name')), True, 
        #                                 middle_screen[0] - distance_from_center, middle_screen[1] - 150, 300)
        
        # btn_change_player_color = Button(self.options.screen.get_screen(), 'Player color: {}'.format(self.tmp_player_color.get('name')), True, 
        #                                 middle_screen[0] - distance_from_center, middle_screen[1] - 70, 300)
        
        # btn_change_game_speed = Button(self.options.screen.get_screen(), 'Game speed: {}'.format(self.tmp_tick_speed.get('name')), True, 
        #                                 middle_screen[0] - distance_from_center, middle_screen[1], 300)
        
        # btn_main_menu = Button(self.options.screen.get_screen(), 'Main menu', True, 
        #                                 middle_screen[0] - distance_from_center, middle_screen[1] + 70, 300)

        btn_main_menu = self.ui_manager.get_element('Main menu')
        while True:
            btn_toolbar_position = self.ui_manager.get_element('Toolbar: {}'.format(self.tmp_toolbar_pos.get('name')))
            btn_change_resolution = self.ui_manager.get_element('Resolution: {}'.format(self.tmp_resolution.get('name')))
            btn_change_player_color = self.ui_manager.get_element('Player color: {}'.format(self.tmp_player_color.get('name')))
            btn_change_game_speed = self.ui_manager.get_element('Game speed: {}'.format(self.tmp_tick_speed.get('name')))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Scenes.QUIT.value
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if btn_main_menu.is_clicked(mouse_pos):
                        self.save_options()
                        return Scenes.HOME.value
                    
                    if btn_toolbar_position.is_clicked(mouse_pos):
                        self.tmp_toolbar_pos = self.options.get_next_value('toolbar')
                        btn_toolbar_position.update(text='Toolbar: {}'.format(self.tmp_toolbar_pos.get('name')))

                    if btn_change_resolution.is_clicked(mouse_pos):
                        self.tmp_resolution = self.options.get_next_value('resolution')
                        btn_change_resolution.update(text='Resolution: {}'.format(self.tmp_resolution.get('name')))

                    if btn_change_game_speed.is_clicked(mouse_pos):
                        self.tmp_tick_speed = self.options.get_next_value('tick_speed')
                        btn_change_game_speed.update(text='Game speed: {}'.format(self.tmp_tick_speed.get('name')))

                    if btn_change_player_color.is_clicked(mouse_pos):
                        self.tmp_player_color = self.options.get_next_value('player_color')
                        btn_change_player_color.update(text='Player color: {}'.format(self.tmp_player_color.get('name')))

            # btn_change_resolution.draw()
            # btn_change_player_color.draw()
            # btn_change_game_speed.draw()
            # btn_main_menu.draw()
            # btn_toolbar_position.draw()
            self.ui_manager.draw()

            pygame.display.update()
            self.options.clock_tick()

    def save_options(self):
        """Updates the options object."""
        self.options.set_value('toolbar', self.tmp_toolbar_pos)
        self.options.set_value('player_color', self.tmp_player_color)
        self.options.set_value('resolution', self.tmp_resolution)
        self.options.set_value('tick_speed', self.tmp_tick_speed)