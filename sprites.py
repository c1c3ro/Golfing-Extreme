import pygame
import random
import math
from constants import *

vec = pygame.math.Vector2

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('golf-ball8.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 0
        self.pos = vec(100, 0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self, on_sand):
        self.acc = vec(0, BALL_GRAV)
        if on_sand:
            self.acc = vec(0, 0)
        else:
            if self.vel.y < -4:
                self.vel.y = -4
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -BALL_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = BALL_ACC
        if keys[pygame.K_SPACE]:
            self.vel.y -= 20

        # apply friction
        self.acc.x += self.vel.x * BALL_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

