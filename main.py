import sys

import pygame

from color import *
from costants import CELL_SIZE, GRID_WIDTH, GRID_HEIGHT, SCREEN, CLOCK
from button import Button
from grid import Grid

def main():
    pygame.init()
    grid = Grid()

    btn_Activate = Button(SCREEN, 'Activate', True, 20, 20)
    btn_Stop = Button(SCREEN, 'Stop', False, 20, 20)
    active_button = btn_Activate

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

                if event.button == 1: 
                    # Activate cell if left mouse button
                    if grid.get_color(cell_x, cell_y) == WHITE:
                        grid.set_color(RED, cell_x, cell_y)
                elif event.button == 3:
                    # Deactivate cell if right mouse button
                    if grid.get_color(cell_x, cell_y) == RED:
                        grid.set_color(WHITE, cell_x, cell_y)

                # Verify if the button is clicked, and if so, perform some actions per button
                if btn_Activate.visible and btn_Activate.is_clicked(mouse_pos):
                    active_button = btn_Stop
                elif btn_Stop.visible and btn_Stop.is_clicked(mouse_pos):
                    active_button = btn_Activate
        grid.draw()

        if active_button == btn_Activate:
            # Stop the game, draw mode
            tick_speed = 20
            btn_Stop.visible = False
            btn_Activate.visible = True
            btn_Activate.draw()
        elif active_button == btn_Stop:
            # Activate the game, play mode
            tick_speed = 3
            btn_Stop.visible = True
            btn_Activate.visible = False
            grid.apply_game_rules()
            btn_Stop.draw()
        else:
            print("An error occurred :: no button is active! Please restart the game.")

        pygame.display.update()
        tick_speed = tick_speed if tick_speed else 20
        CLOCK.tick(tick_speed)


if __name__ == '__main__':
    main()