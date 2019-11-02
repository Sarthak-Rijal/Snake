import pygame
from Grid import *
from Snake import *
from Food import *
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
food = Food(screen, gameGrid)


    

def play():
    global screen
    
    game_over = False

    gameGrid.make_grid()
    
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameGrid.updateGrid()
        food.drawfood()
        snake.update()

        pygame.display.update()
        clock.tick(FPS)

play()
