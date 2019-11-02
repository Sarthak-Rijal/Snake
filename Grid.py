import pygame
from cell import *
import sys


pygame.init()
# snake class
class Grid(object): 
    # Function to initialise the node object 
    def __init__(self, screen, size, row, column, color):
        
        self.screen = screen
        self.row = row
        self.column = column
        
        self.size = size

        self.Cells = {}

    
    def make_grid(self):

        for row in range(0, self.size[0], 20):
            for col in range(0, self.size[1], 20):
                self.Cells[(row,col)] = cell(self.screen, row, col, 20, "BOARD")



    def updateGrid(self):
        for position, cell in self.Cells.items():
            cell.draw()

            
    def updateCell(self, location, cellType):
        self.Cells.get((location[0], location[1])).setCell(cellType)


