import pygame
import time
from cell import *
from constants import *
import sys
from collections import deque


UP = (0,-1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


pygame.init()

# snake class
class Snake(object): 
    # Function to initialise the node object 
    def __init__(self, screen, size, grid, direction = (1, 0), color = (128, 128, 128)):
        
        self.screen = screen
        self.grid = grid
        self.inputQueue = deque()

        self.direction = direction
        self.snake = deque()
        self.size = size


        #instantiate the snake
        self.snake.append( ((20,20), SNAKE) )
        self.head = self.snake[0]

    
    def update(self):
        for snakeBody in self.snake:
            self.grid.updateCell( snakeBody[0], snakeBody[1] )
    
    #queue future turns
    def takeInput(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.inputQueue.appendleft(UP)
                if event.key == pygame.K_DOWN:
                    self.inputQueue.appendleft(DOWN)
                if event.key == pygame.K_LEFT:
                    self.inputQueue.appendleft(LEFT)
                if event.key == pygame.K_RIGHT:
                    self.inputQueue.appendleft(RIGHT)

             
        

                                                  






