import pygame
import sys


pygame.init()
# snake class
class Grid(object): 
    # Function to initialise the node object 
    def __init__(self, screen, size, row, column, color = (192,192,192)):
        self.screen = screen
        self.size = size
        self.row = row
        self.column = column
        self.color = color

    # need to have a coordinate system for the gird. 

    def make_grid(self):
        
        spacing = [self.size[0] // self.row, self.size[1] // self.column]
        
        x = 0
        y = 0
        
        for srowLines in range(self.row):
            x = x + spacing[0]
            pygame.draw.line(self.screen, self.color, (x,0),(x,self.size[0]))

        for columnLines in range(self.column):
            y = y + spacing[1]
            pygame.draw.line(self.screen, self.color, (0,y),(self.size[1], y))



