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
class Block(object): 
    # Function to initialise the node object 
    def __init__(self, screen, size, grid, timeBlock = 0,  speed = 5, direction = (1, 0), color = (128, 128, 128), snake = [[40,80]]):
        
        #######MAIN WINDOW SETTINGS#############
        self.screen = screen
        self.size = size
        self.grid = grid
        #######################################


        ###############CELL STATES###########
        self.direction = direction
        self.speed = speed
        self.snake = snake
        ###################################
        
        #Cosmetic##########
        self.color = color

        #ALGORITHMS
        self.inputQueue = deque()


    #######################
    #Getter Class    (//top left(x,y))[: ]   
    def getDirection(self):
        return self.direction


    #SETTIER FUNCTION ##########################
    def takeInput(self):
        time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            
           # print(time)

   
            

            ###CONTROL INPUT################################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.inputQueue.appendleft(UP)
                if event.key == pygame.K_DOWN:
                    self.inputQueue.appendleft(DOWN)
                if event.key == pygame.K_LEFT:
                    self.inputQueue.appendleft(LEFT)
                if event.key == pygame.K_RIGHT:
                    self.inputQueue.appendleft(RIGHT)
            #################################################

    #PRIVATE CLASS
    ############CHANGE DIRECTION#################################
    def setDirection(self, direction, defult =True):               #
                                                                #
            #######################manuel Change Direction                                               #
            if (self.inputQueue[-1] == direction[0] or self.inputQueue[-1] == direction[1]):
                    self.direction = self.inputQueue.pop()
            else:
                print(self.inputQueue.pop())
            
            
            
            #self.direction = direction
    
    def moveThroughWalls (self, position):
        ######Through Walls################################
        if (position[0] > self.grid.size[0]):
            position[0] = 0
        if (position[0] + self.size < 0):
            position[0] = self.grid.size[0] - self.size
        
        if (position[1] > self.grid.size[1]):
            position[1] = 0
        if (position[1] + self.size < 0):
            position[1] = self.grid.size[1] - self.size
    ######################################################################################################

    ####UPDATER FUNCTION##############################################
    ##################################################################
    def move(self, time):
        #[KEYBOARD MOVEMENTS]
        
        
        for position in self.snake:

                        
            position[0] += self.speed * self.direction[0]
            position[1] += self.speed * self.direction[1]

            
                
            self.moveThroughWalls(position)

            #when the snake snaps to the grid  AND there are moves in the queue
            # move to a given legal direction
            
            if (position[0] % self.size == 0 and position[1] % self.size == 0 and
                len(self.inputQueue) != 0):

                if (self.getDirection() == RIGHT):
                    self.setDirection((UP, DOWN))
                
                elif (self.getDirection() == LEFT):
                    self.setDirection((UP, DOWN))

                elif (self.getDirection() == UP):
                    self.setDirection((RIGHT, LEFT))

                elif (self.getDirection() == DOWN):
                    self.setDirection((RIGHT, LEFT))

        self._draw()
#########################################################################################
#########################################################################################


###############Private Draw Variable#################################################################
    # #draws the cell

    def _draw (self):

        # print(self.inputQueue)
        for position in self.snake:
                    pygame.draw.rect(self.screen, self.color, (position[0],position[1],self.size,self.size))

                                                  

################################################################################################################




