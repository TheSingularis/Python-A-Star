import pygame
from enum import Enum


class State(Enum):
    EMPTY = 1
    WALL = 2
    START = 3
    END = 4
    OPEN = 5
    CLOSED = 6
    PATH = 7


colours = {
    State.EMPTY: [253, 255, 252],
    State.WALL: [1, 22, 39],
    State.START: [51, 202, 127],
    State.END: [231, 29, 54],
    State.OPEN: [255, 120, 90],
    State.CLOSED: [255, 231, 76],
    State.PATH: [57, 160, 237],
}


class Block:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.state = State.EMPTY

        self.gCost = 0
        self.hCost = 0
        self.parent = None

        self.rect = pygame.Rect(self.x, self.y, width, width)

    def get_rect(self):
        return self.rect

    def set_state(self, state):  # this may need to be changed if it doesnt like the Enum passed in
        self.state = state

    def draw(self, win, colour):
        pygame.draw.rect(win, colour, self.rect)

    def f_cost(self):
        return self.gCost + self.hCost
