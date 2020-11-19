import pygame
import random
import math
from constants import *
from physics_util import updateBall
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
        self.on_sand = False
        if mode == EARTH_MODE:
            self.ball_grav = EARTH_GRAV
        elif mode == MARS_MODE:
            self.ball_grav = MARS_GRAV
        elif mode == MOON_MODE:
            self.ball_grav = MOON_GRAV

    def update(self):
        self.rect.midbottom = updateBall(self)
