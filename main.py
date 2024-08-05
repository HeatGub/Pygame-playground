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

def drawWindow(time):
    SCREEN.fill('black')
    #drawPendulum(WIDTH/2, HEIGHT/2, x, y)
    drawPendulum(WIDTH/2, HEIGHT/2, 200)
    #pygame.display.update()
    pygame.display.flip() #redraws whole screen

circleColor=[100,150,0]
gravity = 1
angle = np.pi/2
angVel = 0
angAcc = 0

def drawPendulum(pivotX, pivotY, len):
    global angle
    global angVel
    global angAcc
    force = gravity * np.sin(angle)
    angAcc = (-1 * force) / len
    angVel += angAcc
    angle += angVel

    x = WIDTH/2 + len*np.sin(angle)
    y = HEIGHT/2 + len*np.cos(angle)

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