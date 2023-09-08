from UI_elements.color import Color
from grid import Grid
from team import TeamManager
from game_scenes.scenes import Scenes
from UI_elements.button import Button
from UI_elements.label import TemplateLabel
from UI_elements.toolbar.factory import ToolbarFactory

import pygame

class PlayScene:
    def __init__(self, options):
        self.options = options
        self.team_manager = TeamManager('player', 'enemy', self.options)

    def run(self):
        self.options.screen.fill(Color.WHITE.value)
        grid = Grid(self.options, self.team_manager)

        btn_Stop = Button(self.options.screen.get_screen(), 'Stop', False, 0, 0)
        btn_Activate = Button(self.options.screen.get_screen(), 'Activate', True, 0, 0)
        active_button = btn_Activate

        btn_Randomize = Button(self.options.screen.get_screen(), 'Random', True, 0, 0)
        btn_Clear = Button(self.options.screen.get_screen(), 'Clear', True, 0, 0)
        btn_Invasion = Button(self.options.screen.get_screen(), 'Invasion', True, 0, 0, background_color=Color.CUSTOM_BLUE.value)
        btn_main_menu = Button(self.options.screen.get_screen(), 'Main menu', True, 0, 0)

        # Setting up labels, based on the toolbar position.
        lbl_alive = TemplateLabel(self.options.screen.get_screen(), 10, 100, 'Alive cells: {}', grid.get_alive_cells)
        lbl_killed = TemplateLabel(self.options.screen.get_screen(), 10, 100, 'Dead cells: {}', grid.get_dead_cells)
        lbl_born = TemplateLabel(self.options.screen.get_screen(), 10, 100, 'Born cells: {}', grid.get_born_cells)

        # Create toolbar
        buttons = [btn_Stop, btn_Activate, btn_Randomize, btn_Clear, btn_Invasion, btn_main_menu]
        template_labels = [lbl_alive, lbl_killed, lbl_born]

        factory_toolbar = ToolbarFactory(self.options.screen, Color.BLACK.value, buttons, template_labels)
        toolbar = factory_toolbar.get_instance(self.options.get_actual_value('toolbar').get('value'))
    
        self.options.screen.fill(Color.WHITE.value)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return Scenes.QUIT.value
                
                if event.type == pygame.KEYDOWN:
                    # Space bar can switch between Activate and Stop mode.
                    if event.key == pygame.K_SPACE:
                        print("Space bar pressed.")
                        mouse_pos = pygame.mouse.get_pos()
                        if btn_Activate.visible:
                            active_button = btn_Stop
                        elif btn_Stop.visible:
                            active_button = btn_Activate  
                    # R key activate Random button.
                    elif event.key == pygame.K_r:
                        grid.randomize()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    cell_x = mouse_pos[0] // self.options.cell_size
                    cell_y = mouse_pos[1] // self.options.cell_size

                    if event.button == 1:           # Left mouse button
                        grid.activate_cell(cell_x, cell_y, self.team_manager.player.color)
                    elif event.button == 3:         # Right mouse button
                        grid.deactivate_cell(cell_x, cell_y)

                    # Verify if the button is clicked
                    if btn_Activate.visible and btn_Activate.is_clicked(mouse_pos):
                        active_button = btn_Stop
                    elif btn_Stop.visible and btn_Stop.is_clicked(mouse_pos):
                        active_button = btn_Activate
                    elif btn_Randomize.is_clicked(mouse_pos):
                        grid.randomize()          
                    elif btn_Clear.is_clicked(mouse_pos):
                        grid.clear()
                    elif btn_Invasion.is_clicked(mouse_pos):
                        grid.invasion()
                    elif btn_main_menu.is_clicked(mouse_pos):
                        return Scenes.HOME.value

                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    cell_x = mouse_pos[0] // self.options.cell_size
                    cell_y = mouse_pos[1] // self.options.cell_size

                    if pygame.mouse.get_pressed()[0]:    # Left mouse button       
                        grid.activate_cell(cell_x, cell_y, self.team_manager.player.color)
                    elif pygame.mouse.get_pressed()[2]:  # Right mouse button
                        grid.deactivate_cell(cell_x, cell_y)

            grid.draw()

            if active_button == btn_Activate:
                # Activate btn is visible. Stop the game, enter "draw" mode.
                self.tick_speed = 60
                btn_Stop.visible = False
                btn_Activate.visible = True
                btn_Activate.draw()
            elif active_button == btn_Stop:
                # Stop btn is visible. Activate the game, enter "game of life" mode.
                self.tick_speed = 10
                btn_Stop.visible = True
                btn_Activate.visible = False
                grid.apply_game_rules()
                btn_Stop.draw()
            else:
                print("An error occurred :: no button is active! Please restart the game.")
                return Scenes.QUIT.value
            toolbar.draw()
            pygame.display.update()
            self.options.clock_tick()