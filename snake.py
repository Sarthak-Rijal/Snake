import pygame
import sys

pygame.init()

#arbritary screen size and setup 
size = (600, 600)
snake_pos = [size[0]/2 -20,size[1]/2 - 20]
snake_size = 40
screen = pygame.display.set_mode(size)

grid_color = (192,192,192)
rows = 15
RED = (255, 0, 0)
#FPS
clock = pygame.time.Clock()
FPS = 30


def drawsnake():
    pygame.draw.rect(screen, RED,(snake_pos[0],snake_pos[1],snake_size,snake_size))

def make_grid():
    sizeBtwn = [size[0] // rows, size[1] // rows]
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn[0]
        y = y + sizeBtwn[1]

        pygame.draw.line(screen, grid_color, (x,0),(x,size[0]))
        pygame.draw.line(screen, grid_color, (0,y),(size[1], y))

def screencolor():
    global screen
    screen.fill((50, 205, 50))
    
    make_grid()
    

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
        drawsnake()
        a,b = check_control(snake_pos[0], snake_pos[1])
        snake_pos[0] = a
        snake_pos[1] = b
        pygame.display.update()
        clock.tick(FPS)

play()
