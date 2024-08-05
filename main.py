import functions
import pygame
import numpy as np

pygame.init()
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Window')
font = pygame.font.Font('freesansbold.ttf', 20)
font_big = pygame.font.Font('freesansbold.ttf', 50)
clock = pygame.time.Clock()
FPS = 60
circleColor=[100,150,0]
speed = 0.1

def drawWindow(time):
    SCREEN.fill([0,0,5])
    x = WIDTH/2 + 200*np.sin(time*speed)
    y = HEIGHT/2 + 200*np.cos(time*speed)
    drawPendulum(WIDTH/2, HEIGHT/2, x, y)
    pygame.display.update()
    #pygame.display.flip() #redraws whole screen

def drawPendulum(pivotX, pivotY, x, y):
    pygame.draw.line(SCREEN, 'white', (pivotX, pivotY), (x, y), 4)
    pygame.draw.circle(SCREEN, circleColor, [x, y], 30)

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