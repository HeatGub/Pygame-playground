# .\.venv\Scripts\activate.bat
import pygame
import random
import functions

pygame.init()

WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)
pygame.display.set_caption('Pygame Window')
clock = pygame.time.Clock()
FPS = 60
gravity = 0.07

# pendulums = []
# for i in range(5):
#     p = functions.SimplePendulum(WIDTH/2, HEIGHT/2, random.randint(50,250), -1-3*random.random())
#     pendulums.append(p)

balls = []
ballsSpeed = 10
ballSize = HEIGHT/6
for i in range(3):
    b = functions.Ball(WIDTH/2,HEIGHT/2, -ballsSpeed/4+ballsSpeed/2*random.random(),-ballsSpeed/2+ballsSpeed*random.random(), ballSize)
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

dt = 0
def gameLoop():
    global dt # to pass it to the module
    run = True
    while run:
        last_tick = pygame.time.get_ticks()
        clock.tick(FPS) #controls framerate
        drawWindow()

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # update screen parameters on window resize
            if event.type == pygame.VIDEORESIZE: 
                global WIDTH, HEIGHT, SCREEN
                WIDTH = event.w
                HEIGHT = event.h
                SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        dt = pygame.time.get_ticks() - last_tick # time delta

    pygame.quit()

if __name__ == gameLoop(): # Execute Code When the File Runs as a Script, but Not When It's Imported as a Module
    gameLoop()