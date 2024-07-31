import functions
import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Window')
font = pygame.font.Font('freesansbold.ttf', 20)
font_big = pygame.font.Font('freesansbold.ttf', 50)
clock = pygame.time.Clock()
fps = 60

def draw():
    pygame.draw.line(screen, 'white', (0, 100 ), (800, 100), 2)
    pygame.draw.line(screen, 'white', (100, 0), (100, 800), 5)

#game loop
run = True
while run:
    clock.tick(fps)
    draw()

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()