import pygame
from Grid import *
from Snake import *
import sys

pygame.init()

#arbritary screen size and setup 
size = (1600, 800)
snake_pos = [size[0]/2 -20,size[1]/2 - 20]
snake_size = 20
screen = pygame.display.set_mode(size)

grid_color = (192,192,192)
row = 80
column = 40
RED = (255, 0, 0)
#FPS
clock = pygame.time.Clock()
FPS = 30

gameGrid = Grid(screen, size, row, column)
snake =  Snake(screen, snake_size)

def drawsnake():
    pygame.draw.rect(screen, RED,(snake_pos[0],snake_pos[1],snake_size,snake_size))


def screencolor():
    global screen
    screen.fill((50, 205, 50))
    
    gameGrid.make_grid()
    

def check_control(x,y):
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                #x = snake_pos[0]
                #y = snake_pos[1]
                if event.key == pygame.K_LEFT:
                    x -= snake_size
                elif event.key == pygame.K_RIGHT:
                    x += snake_size
                elif event.key == pygame.K_UP:
                    y -= snake_size
                elif event.key == pygame.K_DOWN:
                    y += snake_size
     return x,y

                


def play():
    global screen
    
    game_over = False
    while not game_over:
        screencolor()
        #event listner
        #drawsnake()
        #a,b = check_control(snake_pos[0], snake_pos[1])
        #snake_pos[0] = a
        #snake_pos[1] = b
        snake.move()
        pygame.display.update()
        clock.tick(FPS)

play()
