import pygame
import random
import math
from constants import *

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('golf-ball16.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = -500
        self.vel = 0

    def update(self):
        self.vel += GRAVIDADE_TERRA/40
        self.rect.bottom += self.vel
