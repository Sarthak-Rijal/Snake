import pygame
import sys
import random
pygame.init()

# cell class
class cell(object): 
    # Function to initialise the node object 
    def __init__(self, screen, color, x, y, size, cellType):
        
        self.screen = screen
        
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        
        self.cellType = cellType
        
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))

    def getX(self):
        return self.x

    def getY(self):
        self.y 

    def setCell(self, Type):
        self.cellType = Type
    

       