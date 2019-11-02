import pygame
from Grid import *
from Snake import *
import sys

pygame.init()

GREY = (128, 128, 128)
BLACK = (0,0,0)
WHITE = (255,255,255)
NAVY_BLUE = (2, 6, 74)

#arbritary screen size and setup 
size = (1600, 800)
snake_pos = [size[0]/2 -20,size[1]/2 - 20]
snake_size = 20
screen = pygame.display.set_mode(size)

grid_color = BLACK
row = 80
column = 40
RED = (255, 0, 0)
#FPS
clock = pygame.time.Clock()
FPS = 30

gameGrid = Grid(screen, size, row, column, GREY)
snake =  Snake(screen, snake_size, gameGrid)

def drawsnake():
    pygame.draw.rect(screen, WHITE,(snake_pos[0],snake_pos[1],snake_size,snake_size))


def screencolor():
    global screen
    screen.fill(NAVY_BLUE)
    
    gameGrid.make_grid()
    

def play():
    global screen
    
    game_over = False
    while not game_over:
        screencolor()
    
        snake.takeInput()
        snake.move()

        pygame.display.update()
        clock.tick(FPS)

play()
