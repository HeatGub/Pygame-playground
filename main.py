import functions
import pygame
import numpy as np

pygame.init()
WIDTH = 1000
HEIGHT = 900
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Window')
font = pygame.font.Font('freesansbold.ttf', 20)
font_big = pygame.font.Font('freesansbold.ttf', 50)
clock = pygame.time.Clock()
FPS = 60
circleColor=[100,150,0]

def drawWindow(time):
    SCREEN.fill([0,0,5])
    #pygame.draw.line(SCREEN, 'white', (0, 100 ), (800, 100), 2)
    #pygame.draw.line(SCREEN, 'white', (100, 0), (100, 800), 5)
    #pygame.display.flip() #redraws whole screen
    x = WIDTH/2 + 300*np.sin(time/10)
    y = HEIGHT/2 + 300*np.cos(time/10)
    pygame.draw.circle(SCREEN, circleColor, [x, y], 30) #going in circle

    pygame.display.update()

def gameLoop():
    run = True
    t = 0

    while run:
        clock.tick(FPS) #controls framerate
        t = t+1
        drawWindow(t)

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

gameLoop()