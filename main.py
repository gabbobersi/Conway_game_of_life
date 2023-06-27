import sys

import pygame

from color import *
from costants import CELL_SIZE, SCREEN, CLOCK, WINDOW_WIDTH, WINDOW_HEIGHT
from button import Button
from grid import Grid

def main():
    pygame.init()
    grid = Grid()

    btn_Activate = Button(SCREEN, 'Activate', True, 20, 20)
    btn_Stop = Button(SCREEN, 'Stop', False, 20, 20)
    btn_Randomize = Button(SCREEN, 'Random', True, 20, 100)

    active_button = btn_Activate

    standard_font = pygame.font.Font('fonts/arial.ttf', 20) 

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
                elif btn_Randomize.is_clicked(mouse_pos):
                    grid.randomize()               
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

        lbl_alive_text = "Alive cells: {}".format(grid.get_alive_cells())
        lbl_killed_text = "Killed cells: {}".format(grid.killed_cells_counter)
        lbl_born_text = "Born cells: {}".format(grid.born_cells_counter)

        lbl_text = standard_font.render(lbl_alive_text, True, BLACK) 
        label_rect = lbl_text.get_rect()
        label_rect.center = (197, 30)
        SCREEN.blit(lbl_text, label_rect)

        lbl_text = standard_font.render(lbl_killed_text, True, BLACK) 
        label_rect = lbl_text.get_rect()
        label_rect.center = (200, 60)
        SCREEN.blit(lbl_text, label_rect)

        lbl_text = standard_font.render(lbl_born_text, True, BLACK) 
        label_rect = lbl_text.get_rect()
        label_rect.center = (197, 90)
        SCREEN.blit(lbl_text, label_rect)

        pygame.display.update()
        tick_speed = tick_speed if tick_speed else 20
        CLOCK.tick(tick_speed)


if __name__ == '__main__':
    main()