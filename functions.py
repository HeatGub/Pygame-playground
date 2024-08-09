
import random
import numpy as np
import pygame
# from main import pygame, SCREEN, WIDTH, HEIGHT, gravity

class SimplePendulum:
    def __init__(self, pivotX, pivotY, len, angle):
        self.pivotX = pivotX
        self.pivotY = pivotY
        self.len = len
        self.circleColor=[random.randint(20,200),random.randint(20,200),random.randint(20,200)]
        self.angle = angle
        self.angVel = 0
        self.angAcc = 0

    def update(self):
        from main import SCREEN, WIDTH, HEIGHT, gravity

        self.force = gravity * np.sin(self.angle)
        self.angAcc = (-1 * self.force) / self.len
        self.angVel += self.angAcc
        self.angle += self.angVel

        x = WIDTH/2 + self.len*np.sin(self.angle)
        y = HEIGHT/2 + self.len*np.cos(self.angle)

        pygame.draw.line(SCREEN, 'white', (self.pivotX, self.pivotY), (x, y), int(self.len/100))
        pygame.draw.circle(SCREEN, self.circleColor, [x, y], self.len/10)

class Ball:
    def __init__(self, x, y, velX, velY, radius):
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY
        self.radius = radius
        self.color=[random.randint(20,200),random.randint(20,200),random.randint(20,200)]

    def update(self):
        from main import SCREEN, WIDTH, HEIGHT, gravity
        # self.forceY = gravity #mass later
        # self.forceX = 0
        self.accY = gravity #slow them down for now/
        self.velY += self.accY
        self.y += self.velY
        self.x += self.velX

        #bounce off the walls
        if (self.x - self.radius) <= 0: #LEFT
            self.x = 0 + self.radius #otherwise falls off the screen
            self.velX = -self.velX
        elif (self.x + self.radius) >= WIDTH: #RIGHT
            self.x = WIDTH - self.radius
            self.velX = -self.velX
        if (self.y + self.radius) >= HEIGHT: #BOTTOM
            self.y = HEIGHT - self.radius
            self.velY = -self.velY
        elif (self.y - self.radius) <= 0: #TOP
            self.y = 0 + self.radius
            self.velY = -self.velY

        pygame.draw.circle(SCREEN, self.color, [self.x, self.y], self.radius)
