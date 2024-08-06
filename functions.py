
import random
import numpy as np
# from main import pygame, SCREEN, WIDTH, HEIGHT, gravity

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
        from main import pygame, SCREEN, WIDTH, HEIGHT, gravity

        self.force = gravity * np.sin(self.angle)
        self.angAcc = (-1 * self.force) / self.len
        self.angVel += self.angAcc
        self.angle += self.angVel

        x = WIDTH/2 + self.len*np.sin(self.angle)
        y = HEIGHT/2 + self.len*np.cos(self.angle)

        pygame.draw.line(SCREEN, 'white', (self.pivotX, self.pivotY), (x, y), int(self.len/100))
        pygame.draw.circle(SCREEN, self.circleColor, [x, y], self.len/10)