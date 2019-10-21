import pygame


pygame.init()

#arbritary screen size and setup 
size = (600, 800)

screen = pygame.display.set_mode(size)
grid_color = (192,192,192)

#FPS
clock = pygame.time.Clock()
FPS = 30



def play():

    while True:
     
        #event listner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          


    
        clock.tick(FPS)

play()