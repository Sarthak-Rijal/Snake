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
    def __init__(self, screen, size, grid, speed = 2, direction = (1, 0), color = (128, 128, 128), snake = [[40,80]]):
        
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

    #if eaten it sould increase in size
    #def increaseSize():
     #   self.snake.appendleft()

    #set direction
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

             

    def move(self):

        for position in self.snake:
            position[0] += self.speed * self.direction[0]
            position[1] += self.speed * self.direction[1]

            #at each line segment check if there is a legal move 
            
            if (position[0] % self.size == 0 and position[1] % self.size == 0 and
                len(self.inputQueue) != 0):

                if (self.getDirection() == RIGHT):
                    if (self.inputQueue[-1] == UP or self.inputQueue[-1] == DOWN):
                            self.direction = self.inputQueue.pop()
                    else:
                        self.inputQueue.pop()
                
                elif (self.getDirection() == LEFT):
                    if (self.inputQueue[-1] == UP or self.inputQueue[-1] == DOWN):
                            self.direction = self.inputQueue.pop()
                    else:
                        self.inputQueue.pop()

                elif (self.getDirection() == UP):
                    if (self.inputQueue[-1] == LEFT or self.inputQueue[-1] == RIGHT):
                            self.direction = self.inputQueue.pop()
                    else:
                        self.inputQueue.pop()

                elif (self.getDirection() == DOWN):
                    if (self.inputQueue[-1] == LEFT or self.inputQueue[-1] == RIGHT):
                            self.direction = self.inputQueue.pop()
                    else:
                        self.inputQueue.pop()
                        
        self._draw()




    # #draws the cell
    def _draw (self):

        for position in self.snake:
                    pygame.draw.rect(self.screen, self.color, (position[0],position[1],self.size,self.size))

                                                  






