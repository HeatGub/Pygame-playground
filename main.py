# .\.venv\Scripts\activate.bat
import pygame
import random
import functions

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

pendulums = []
for i in range(25):
    p = functions.simplePendulum(WIDTH/2, HEIGHT/2, random.randint(50,250), -1-3*random.random())
    pendulums.append(p)

def drawWindow():
    SCREEN.fill('black')
    for pendulum in pendulums:
        pendulum.update()
    pygame.display.flip() #redraws whole screen

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
    #print(__name__)

if __name__ == gameLoop(): # Execute Code When the File Runs as a Script, but Not When It's Imported as a Module
    gameLoop()