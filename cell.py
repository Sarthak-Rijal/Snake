import pygame
import sys
import random
from constants import *
pygame.init()



# cell class
class cell(object): 
    # Function to initialise the node object 
    def __init__(self, screen, x, y, size, cellType):
        
        self.screen = screen
        
        
        self.x = x
        self.y = y
        self.size = size
        
        self.cellType = cellType
        

    def getX(self):
        return self.x

    def getY(self):
        self.y 

    def setCell(self, Type):
        self.cellType = Type
    
    def draw(self):

        if (self.cellType == "BOARD"):
            pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.size, self.size))
        
        if (self.cellType == "SNAKE"):
            pygame.draw.rect(self.screen, GREEN, (self.x, self.y, self.size, self.size))

        if (self.cellType == "FOOD"):
            pygame.draw.rect(self.screen, RED, (self.x, self.y, self.size, self.size))

       