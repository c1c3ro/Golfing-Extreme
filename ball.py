import pygame
import random
import math
from constants import *
from os import path

vec = pygame.math.Vector2

class Ball(pygame.sprite.Sprite):

    def __init__(self, mode, initial_x):
        super().__init__()

        self.image = pygame.image.load(path.join('img', 'golf-ball8.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = 200
        self.pos = vec(initial_x, 200)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        if mode == EARTH_MODE:
            self.ball_grav = EARTH_GRAV
        elif mode == MARS_MODE:
            self.ball_grav = MARS_GRAV
        elif mode == MOON_MODE:
            self.ball_grav = MOON_GRAV

    def update(self, on_sand):
        self.acc = vec(0, self.ball_grav)
        if on_sand:
            self.acc = vec(0, 0)
        else:
            if self.vel.y < -5:
                self.vel.y = -5

        # apply friction
        self.acc.x += self.vel.x * BALL_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1 and abs(self.vel.y) < 0.1:
            self.vel = vec(0, 0)
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

