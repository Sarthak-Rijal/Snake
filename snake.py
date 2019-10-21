import pygame
import sys

pygame.init()

#arbritary screen size and setup 
size = (600, 600)
snake_pos = [size[0]/2,size[1]/2]
screen = pygame.display.set_mode(size)
grid_color = (192,192,192)
rows = 15

#FPS
clock = pygame.time.Clock()
FPS = 30

def make_grid():
    sizeBtwn = [size[0] // rows, size[1] // rows]
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn[0]
        y = y + sizeBtwn[1]

        pygame.draw.line(screen, (255,255,255), (x,0),(x,size[0]))
        pygame.draw.line(screen, (255,255,255), (0,y),(size[1], y))

def screencolor():
    global screen
    screen.fill((50, 205, 50))
    
    make_grid()
    pygame.display.update()

def check_control():
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                x = snake_pos[0]
                y = snake_pos[1]
                if event.key == pygame.K_LEFT:
                    x -= 5
                elif event.key == pygame.K_RIGHT:
                    x += 5
                elif event.key == pygame.K_UP:
                    y -= 5
                elif event.key == pygame.K_DOWN:
                    y +=5




def play():
    global screen
    game_over = False
    while not game_over:
        screencolor()
        #event listner
        check_control()

          


    
        clock.tick(FPS)

play()
