# .\.venv\Scripts\activate.bat
import pygame
import random
import functions

pygame.init()
pygame.font.init()
WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)
pygame.display.set_caption('Pygame Window')
#font = pygame.font.Font('freesansbold.ttf', 20)
clock = pygame.time.Clock()
FPS = 60
gravity = 1

# pendulums = []
# for i in range(5):
#     p = functions.SimplePendulum(WIDTH/2, HEIGHT/2, random.randint(50,250), -1-3*random.random())
#     pendulums.append(p)

balls = []
ballsSpeed = 10
ballSize = HEIGHT/10
for i in range(10):
    b = functions.Ball(WIDTH/2,HEIGHT/2, -ballsSpeed/2+ballsSpeed*random.random(),-ballsSpeed/2+ballsSpeed*random.random(), ballSize)
    balls.append(b)


def drawWindow():
    SCREEN.fill('black')
    for i in range(len(balls)):
        balls[i].update()
        # if i == 1:
        #     print(b.velY)
    # for pendulum in pendulums:
    #     pendulum.update()
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
            # update screen parameters on window resize
            if event.type == pygame.VIDEORESIZE: 
                global WIDTH
                global HEIGHT
                global SCREEN
                WIDTH = event.w
                HEIGHT = event.h
                SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.quit()

if __name__ == gameLoop(): # Execute Code When the File Runs as a Script, but Not When It's Imported as a Module
    gameLoop()