import pygame 
import sys
import random

pygame.init();

class Food():
    def __init__(self, screen, grid, size = 20, color = (128,0,0)):
        self.screen = screen
        self.size = size
        self.color = color
        
        self.grid = grid

        self.position = self.randomPosition()
        print(self.position[0]%20, self.position[1]%20)

    def drawfood(self):
        pygame.draw.rect(self.screen, self.color,(self.position[0], self.position[1], self.size, self.size))

    def randomPosition(self):
        return random.randrange(0,self.grid.size[0], 20), random.randrange(0,self.grid.size[1], 20)
