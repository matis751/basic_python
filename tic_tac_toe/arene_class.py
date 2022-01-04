import pygame
import sys


class Arene:

    def __init__(self):
        size = (50, 50)
        self.line = 0
        self.row = 0
        self.surface = 0
        self.White = (255, 255, 255)
        self.Black = (0, 0, 0)
        self.square = {}
        self.space_between_raw = 0
        self.space_between_column = 0

