import pygame
from cell import *
import sys


pygame.init()
# snake class
class Grid(object): 
    # Function to initialise the node object 
    def __init__(self, screen, size, row, column, color):
        
        self.screen = screen
        
        self.size = size
        
        self.row = row
        self.column = column

        self.Cells = [[]]


    def make_grid(self):

        x = 0
        y = 0

        for row in range(0, self.size[0], 20):
            for col in range(0, self.size[1], 20):
                self.Cells.append(cell(self.screen, (255, 255, 255), row, col, 20, "BOARD"))



            



