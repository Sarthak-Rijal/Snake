import pygame
import time
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
    def __init__(self, screen, size, grid, speed = 5, direction = (1, 0), color = (128, 128, 128), snake = [[40,80]]):
        
        self.screen = screen
        self.size = size
        self.grid = grid
        
        self.direction = direction
        self.speed = speed
        self.snake = snake

        self.color = color

        self.inputQueue = deque()

    def getDirection(self):
        return self.direction

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

             

    def __changeDirection(self, validDirections):

            if (self.inputQueue[-1] == validDirections[0] or self.inputQueue[-1] == validDirections[1]):
                    self.direction = self.inputQueue.pop()
            else:
                self.inputQueue.pop()

    def move(self):
        #update snake postion
        for position in self.snake:
            position[0] += self.speed * self.direction[0]
            position[1] += self.speed * self.direction[1]

            #when the snake snaps to the grid  AND there are moves in the queue
            # move to a given legal direction
            
            if (position[0] % self.size == 0 and position[1] % self.size == 0 and
                len(self.inputQueue) != 0):

                if (self.getDirection() == RIGHT):
                    self.__changeDirection((UP, DOWN))
                
                elif (self.getDirection() == LEFT):
                    self.__changeDirection((UP, DOWN))

                elif (self.getDirection() == UP):
                    self.__changeDirection((RIGHT, LEFT))

                elif (self.getDirection() == DOWN):
                    self.__changeDirection((RIGHT, LEFT))

        self._draw()




    # #draws the cell
    def _draw (self):

        for position in self.snake:
                    pygame.draw.rect(self.screen, self.color, (position[0],position[1],self.size,self.size))

                                                  






