import pygame 
import sys

pygame.init();
class Food():
    def __init__(self, screen, size = 20, color = (128,0,0), pos = [15, 15]):
        self.screen = screen
        self.size = size
        self.color = color
        
        self.posx = pos[0]
        self.posy = pos[1]

    def drawfood(self):
        pygame.draw.rect(self.screen, self.color,(self.posx, self.posy, self.size, self.size))

    