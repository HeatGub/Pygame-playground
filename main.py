# .\.venv\Scripts\activate.bat
#import functions
import pygame
import numpy as np
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Window')
font = pygame.font.Font('freesansbold.ttf', 20)
font_big = pygame.font.Font('freesansbold.ttf', 50)
clock = pygame.time.Clock()
FPS = 60

gravity = 1

def drawWindow():
    SCREEN.fill('black')
    p.update()
    for pendulum in pendulums:
        pendulum.update()
    pygame.display.flip() #redraws whole screen

class simplePendulum:
    def __init__(self, pivotX, pivotY, len, angle):
        self.pivotX = pivotX
        self.pivotY = pivotY
        self.len = len
        self.circleColor=[random.randint(20,200),random.randint(20,200),random.randint(20,200)]
        self.angle = angle
        self.angVel = 0
        self.angAcc = 0

    def update(self):
        self.force = gravity * np.sin(self.angle)
        self.angAcc = (-1 * self.force) / self.len
        self.angVel += self.angAcc
        self.angle += self.angVel

        x = WIDTH/2 + self.len*np.sin(self.angle)
        y = HEIGHT/2 + self.len*np.cos(self.angle)

        pygame.draw.line(SCREEN, 'white', (self.pivotX, self.pivotY), (x, y), int(self.len/100))
        pygame.draw.circle(SCREEN, self.circleColor, [x, y], self.len/10)

pendulums = []
for i in range(25):
    p = simplePendulum(WIDTH/2, HEIGHT/2, random.randint(50,250), -1-3*random.random())
    pendulums.append(p)

def gameLoop():
    run = True

    while run:
        clock.tick(FPS) #controls framerate
        drawWindow()

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == gameLoop(): # Execute Code When the File Runs as a Script, but Not When It's Imported as a Module
    gameLoop()