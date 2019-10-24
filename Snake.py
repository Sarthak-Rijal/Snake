import pygame
import sys


pygame.init()
# snake class
class snake(object): 
    # Function to initialise the node object 
    def __init__(size = 40, direction = (0, -1), color = (255, 0, 0), ):
        self.size = size
        self.direction = direction
        self.color = color

    #if eaten it sould increase in size
    def increaseSize():
        pass

    #set direaction
    def setDirection():

    def drawSnake():
        pygame.draw.rect(screen, )

    # #draws the cell
    def _draw (self, screen, color = (0,0,0)):
        pygame.draw.rect(screen, color, self.color, )
                                                  






