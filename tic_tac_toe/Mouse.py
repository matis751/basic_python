import pygame
import sys

class Mouse:

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.square_position = 0
        self.square_position_x = 0
        self.square_position_y = 0
        self.player = 0
        self.list_squares = [[ ],[ ]]
        self.square_player = 0

