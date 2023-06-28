import sys

import pygame

from color import *
from costants import CELL_SIZE, SCREEN, CLOCK
from button import Button
from grid import Grid
from label import Label

def main():
    pygame.init()
    grid = Grid()

    btn_Activate = Button(SCREEN, 'Activate', True, 20, 20)
    btn_Stop = Button(SCREEN, 'Stop', False, 20, 20)
    btn_Randomize = Button(SCREEN, 'Random', True, 20, 100)

    active_button = btn_Activate

    lbl_alive = Label(SCREEN, 'Alive cells: 0', 200, 30, BLACK)
    lbl_killed = Label(SCREEN, 'Killed cells: 0', 200, 60, BLACK)
    lbl_born = Label(SCREEN, 'Born cells: 0', 200, 90, BLACK)

    SCREEN.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0] // CELL_SIZE
                cell_y = mouse_pos[1] // CELL_SIZE
                print(cell_x, cell_y)

                if event.button == 1:           # Left mouse button
                    grid.activate_cell(cell_x, cell_y)
                elif event.button == 3:         # Right mouse button
                    grid.deactivate_cell(cell_x, cell_y)

                # Verify if the button is clicked, and if so, perform some actions per button
                if btn_Activate.visible and btn_Activate.is_clicked(mouse_pos):
                    active_button = btn_Stop
                elif btn_Stop.visible and btn_Stop.is_clicked(mouse_pos):
                    active_button = btn_Activate
                elif btn_Randomize.is_clicked(mouse_pos):
                    grid.randomize()          

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0] // CELL_SIZE
                cell_y = mouse_pos[1] // CELL_SIZE
                print(cell_x, cell_y)

                if pygame.mouse.get_pressed()[0]:    # Left mouse button       
                    grid.activate_cell(cell_x, cell_y)
                elif pygame.mouse.get_pressed()[2]:  # Right mouse button
                    grid.deactivate_cell(cell_x, cell_y)

        grid.draw()

        if active_button == btn_Activate:
            # Stop the game, draw mode
            tick_speed = 20
            btn_Stop.visible = False
            btn_Activate.visible = True
            btn_Activate.draw()
        elif active_button == btn_Stop:
            # Activate the game, play mode
            tick_speed = 4
            btn_Stop.visible = True
            btn_Activate.visible = False
            grid.apply_game_rules()
            btn_Stop.draw()
        else:
            print("An error occurred :: no button is active! Please restart the game.")

        btn_Randomize.draw()
        lbl_alive.draw()
        lbl_killed.draw()
        lbl_born.draw()

        pygame.display.update()
        tick_speed = tick_speed if tick_speed else 20
        CLOCK.tick(tick_speed)


if __name__ == '__main__':
    main()