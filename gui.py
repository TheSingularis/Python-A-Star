import pygame
import block as b
import grid as g
import pathfinder as p

from tkinter import *
from tkinter import messagebox

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
BLOCK_SIZE = 10

win = None
pencil = None
grid = None


def main():
    global win, pencil, grid

    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    win.fill((87, 89, 93))

    pygame.display.set_caption("A* Pathfinding Demo")

    pygame.font.init()

    pencil = b.State.WALL

    grid_ = g.Grid(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE)
    grid = grid_.grid
    run = True
    started = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if not started:
                if pygame.mouse.get_pressed()[0]:
                    for col in grid:
                        for value in col:
                            rect = value.get_rect()
                            if rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                                if pencil == b.State.START:
                                    found, block = grid_.start_or_end_found(b.State.START)
                                    if found:
                                        block.set_state(b.State.EMPTY)
                                    value.set_state(b.State.START)
                                elif pencil == b.State.END:
                                    found, block = grid_.start_or_end_found(b.State.END)
                                    if found:
                                        block.set_state(b.State.EMPTY)
                                    value.set_state(b.State.END)
                                else:
                                    value.set_state(b.State.WALL)
                elif pygame.mouse.get_pressed()[2]:
                    for col in grid:
                        for value in col:
                            rect = value.get_rect()
                            if rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                                value.set_state(b.State.EMPTY)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        pencil = b.State.START
                    if event.key == pygame.K_2:
                        pencil = b.State.END
                    if event.key == pygame.K_3:
                        pencil = b.State.WALL
                    if event.key == pygame.K_SPACE:
                        if not grid_.find_start() is None and not grid_.find_end() is None:
                            started = True
                            a_star = p.Pathfinder(grid_)
                            a_star.find_path(lambda: grid_.draw_grid(win, b.colours), grid_.find_start(), grid_.find_end())
                        else:
                            Tk().wm_withdraw()
                            messagebox.showinfo('ERROR', 'Please select start and end points')

        win.fill((87, 89, 93))
        grid_.draw_grid(win, b.colours)


main()
