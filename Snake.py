import pygame
import time
import sys


pygame.init()
# snake class
class Snake(object): 
    # Function to initialise the node object 
    def __init__(self, screen, size, grid, speed = 10, direction = (1, 0), color = (128, 128, 128), snake = [[0,0]]):
        self.screen = screen
        self.size = size
        self.direction = direction
        self.grid = grid
        self.color = color
        self.snake = snake
        self.speed = speed

    #if eaten it sould increase in size
    #def increaseSize():
     #   self.snake.append()

    #set direction
    def setDirection(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                
                if (self.direction == (-1,0)):#left
                    
                    if event.key == pygame.K_UP:
                        if (self.snake[0] % self.grid.row == 0):
                            self.direction = (0,-1)
                    elif event.key == pygame.K_DOWN:
                        self.direction = (0,1)

                elif (self.direction == (1,0)):#right
                    
                    if event.key == pygame.K_UP:
                        if (self.snake[0][0] % self.grid.row == 0):
                            self.direction = (0,-1)
                    elif event.key == pygame.K_DOWN:
                        self.direction = (0,1)

                elif (self.direction == (0,-1)):#up
                    
                    if event.key == pygame.K_LEFT:
                        self.direction = (-1,0)
                    elif event.key == pygame.K_RIGHT:
                        self.direction = (1,0)

                elif (self.direction == (0,1)):#down
                    
                    if event.key == pygame.K_LEFT:
                        self.direction = (-1,0)
                    elif event.key == pygame.K_RIGHT:
                        self.direction = (1,0)

    def move(self):

        for position in self.snake:
            position[0] += self.speed * self.direction[0]
            position[1] += self.speed * self.direction[1]
            self.setDirection()
            

        self._draw()




    # #draws the cell
    def _draw (self):

        for position in self.snake:
                    pygame.draw.rect(self.screen, self.color, (position[0],position[1],self.size,self.size))

                                                  






