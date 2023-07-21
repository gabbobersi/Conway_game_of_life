import sys

import pygame
from UI_elements.color import *
from UI_elements.button import Button
from UI_elements.label import Label
from UI_elements.toolbar import ToolbarFactory

from grid import Grid
from screen import Screen
from team import TeamManager
from options import Options

TITLE = pygame.display.set_caption('Game of Life')
CLOCK = pygame.time.Clock()

VALID_GAME_STATES = [
    'draw',             # Game is stopped. 
    'play',             # Game is running.
    'main_menu',        # Main menu is displayed. User can't interact with the grid. Animation is played.
    'option_menu',      # Option menu is displayed. User can't interact with the grid.
    'quit'              # Default state in case of fault.
]

class Game:
    def __init__(self):
        pygame.init()
        self.options = Options()        
        self.window_width, self.window_height = self.options.resolution        
        self.team_manager = TeamManager('player', self.options.player_color, 'enemy', self.options.enemy_color)

        self.screen = Screen(self.window_width, self.window_height)
        self.state = 'main_menu'
        self.cell_size = 10          

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if value not in VALID_GAME_STATES:
            print("Error :: Invalid game stated {}".format(value))
            self.state = 'quit'
            return
        self._state = value

    def main_menu(self):
        self.screen.fill(WHITE)
        middle_screen = (self.window_width - 100) // 2, (self.window_height - 200) // 2

        btn_Start = Button(self.screen.get_screen(), 'Start', True, middle_screen[0], middle_screen[1] - 150)
        btn_Option = Button(self.screen.get_screen(), 'Options', True, middle_screen[0], middle_screen[1] - 70)
        btn_Quit = Button(self.screen.get_screen(), 'Quit', True, middle_screen[0], middle_screen[1])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 'quit'
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    mouse_pos = pygame.mouse.get_pos()
                    if btn_Start.is_clicked(mouse_pos):
                        self.state = 'play'
                        return
                    elif btn_Option.is_clicked(mouse_pos):
                        self.state = 'option_menu'
                        return
                    elif btn_Quit.is_clicked(mouse_pos):
                        self.state = 'quit'
                        return
            
            btn_Start.draw()
            btn_Option.draw()
            btn_Quit.draw()

            pygame.display.update()
            CLOCK.tick(self.options.tick_speed)        

    def option_menu(self):
        self.screen.fill(WHITE)
        middle_screen = (self.window_width - 100) // 2, (self.window_height - 200) // 2
        
        distance_from_center = 100
        btn_toolbar_position =  Button(self.screen.get_screen(), 'Toolbar: {}'.format(self.options.toolbar_position), True,
                                        middle_screen[0] - distance_from_center, middle_screen[1] - 220, 300)
        btn_change_resolution = Button(self.screen.get_screen(), 'Change resolution', True, 
                                        middle_screen[0] - distance_from_center, middle_screen[1] - 150, 300)
        btn_change_player_color = Button(self.screen.get_screen(), 'Change player color', True, 
                                        middle_screen[0] - distance_from_center, middle_screen[1] - 70, 300)
        btn_change_game_speed = Button(self.screen.get_screen(), 'Change game speed', True, 
                                        middle_screen[0] - distance_from_center, middle_screen[1], 300)
        btn_main_menu = Button(self.screen.get_screen(), 'Main menu', True, 
                                        middle_screen[0] - distance_from_center, middle_screen[1] + 70, 300)

        # Settings available to change
        opt_toolbar_position = self.options.toolbar_position
        opt_player_color = None
        opt_enemy_color = None
        opt_resolution = None
        opt_tick_speed = None

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 'quit'
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if btn_main_menu.is_clicked(mouse_pos):
                        # Updating options
                        self.options.toolbar_position = opt_toolbar_position if opt_toolbar_position else self.options.toolbar_position
                        self.options.player_color = opt_player_color if opt_player_color else self.options.player_color
                        self.options.enemy_color = opt_enemy_color if opt_enemy_color else self.options.enemy_color
                        self.options.resolution = opt_resolution if opt_resolution else self.options.resolution
                        self.options.tick_speed = opt_tick_speed if opt_tick_speed else self.options.tick_speed
                        self.state = 'main_menu'
                        return
                    if btn_toolbar_position.is_clicked(mouse_pos):
                        if opt_toolbar_position == 'top':
                            opt_toolbar_position = 'left'
                            btn_toolbar_position.update(text='Toolbar: LEFT')
                            print("Label attiva: left")
                        elif opt_toolbar_position == 'left':
                            opt_toolbar_position = 'top'
                            btn_toolbar_position.update(text='Toolbar: TOP')
                            print("Label attiva: top")

            btn_change_resolution.draw()
            btn_change_player_color.draw()
            btn_change_game_speed.draw()
            btn_main_menu.draw()
            btn_toolbar_position.draw()

            pygame.display.update()
            CLOCK.tick(self.options.tick_speed)

    def play(self):
        self.screen.fill(WHITE)
        grid = Grid(self.screen.get_screen(), self.cell_size, self.team_manager)

        btn_Stop = Button(self.screen.get_screen(), 'Stop', False, 0, 0)
        btn_Activate = Button(self.screen.get_screen(), 'Activate', True, 0, 0)
        active_button = btn_Activate

        btn_Randomize = Button(self.screen.get_screen(), 'Random', True, 0, 0)
        btn_Clear = Button(self.screen.get_screen(), 'Clear', True, 0, 0)
        btn_Invasion = Button(self.screen.get_screen(), 'Invasion', True, 0, 0, background_color=CUSTOM_BLUE)
        btn_main_menu = Button(self.screen.get_screen(), 'Main menu', True, 0, 0)

        # Setting up labels, based on the toolbar position.
        lbl_alive = Label(self.screen.get_screen(), 10, 100)
        lbl_killed = Label(self.screen.get_screen(), 10, 100)
        lbl_born = Label(self.screen.get_screen(), 10, 100)

        # Create toolbar
        buttons = [btn_Stop, btn_Activate, btn_Randomize, btn_Clear, btn_Invasion, btn_main_menu]
        labels = [lbl_alive, lbl_killed, lbl_born]

        factory_toolbar = ToolbarFactory(self.screen, BLACK, buttons, labels)
        toolbar = factory_toolbar.get_toolbar(self.options.toolbar_position)
    
        self.screen.fill(WHITE)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 'quit'
                    return
                
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
                    cell_x = mouse_pos[0] // self.cell_size
                    cell_y = mouse_pos[1] // self.cell_size
                    print(cell_x, cell_y)

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
                        self.state = 'main_menu'
                        return

                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    cell_x = mouse_pos[0] // self.cell_size
                    cell_y = mouse_pos[1] // self.cell_size
                    print(cell_x, cell_y)

                    if pygame.mouse.get_pressed()[0]:    # Left mouse button       
                        grid.activate_cell(cell_x, cell_y, self.team_manager.player.color)
                    elif pygame.mouse.get_pressed()[2]:  # Right mouse button
                        grid.deactivate_cell(cell_x, cell_y)

            grid.draw()

            if active_button == btn_Activate:
                # Activate btn is visible. Stop the game, enter "draw" mode.
                self.options.tick_speed = 60
                btn_Stop.visible = False
                btn_Activate.visible = True
                btn_Activate.draw()
            elif active_button == btn_Stop:
                # Stop btn is visible. Activate the game, enter "game of life" mode.
                self.options.tick_speed = 10
                btn_Stop.visible = True
                btn_Activate.visible = False
                grid.apply_game_rules()
                btn_Stop.draw()
            else:
                print("An error occurred :: no button is active! Please restart the game.")
                self.state = 'quit'
                return

            toolbar.draw()
            # btn_Randomize.draw()
            # btn_Clear.draw()
            # btn_Invasion.draw()
            # btn_main_menu.draw()

            lbl_alive.draw('Alive cells: {}'.format(grid.alive_cells_counter))
            lbl_killed.draw('Killed cells: {}'.format(grid.killed_cells_counter))
            lbl_born.draw('Born cells: {}'.format(grid.born_cells_counter))

            pygame.display.update()
            CLOCK.tick(self.options.tick_speed)

    def run(self):
        while True:
            if self.state == 'main_menu':
                self.options.tick_speed = 40
                self.main_menu()

            elif self.state == 'option_menu':
                self.options.tick_speed = 40
                self.option_menu()
            
            elif self.state == 'play':
                self.options.tick_speed = 4
                self.play()
            
            elif self.state == 'quit':
                print("Game is closing correctly.")
                pygame.quit()
                sys.exit()