import pygame
import random
import math
from constants import *

import numpy as np #importando o numpy pra fazer operações com vetores
#para instalar ele é só fazer:
#python -m pip install numpy

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('golf-ball16.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = -500
        #força resultante agindo na bolinha:
        #como o jogo é em 2d, a força é um vetor bidimensional
        #inicializando ela em 0
        self.f_r = np.zeros((1, 2))
        self.m = MASSA

    def update(self, moving):
        if moving == True:
            self.f_r = np.subtract(
                np.subtract(self.f_r, self.m * GRAVIDADE_TERRA), (C_A_ESFERA_LISA * np.power(self.f_r, 2))
                )
            print(self.f_r[0, 1])
            #self.rect.bottom += self.vel[0, 1]
            self.rect.move_ip(self.f_r[0, 0], self.f_r[0, 1])
        
