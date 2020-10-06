import pygame
import random
import math
from constants import *

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('golf-ball25.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = -500

    def update(self):
        self.rect.bottom += 5
