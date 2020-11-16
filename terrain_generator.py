'''
Terrain Generator
Código para o trabalho de Laboratório de Programação
Equipe:
- Cícero José
- Cícero Samuel
- Thiago Carlos
'''

import pygame
import random
import math
from constants import *
from terrain_util import *

class TerrainGenerator(pygame.sprite.Sprite):
    #Terrain generator é uma classe que irá
    #gerar os terrenos do desert golfing de forma
    #procedural, utilizando a biblioteca random.
    #Irei dividir a tela do jogo em quantidades
    #especificadas pelo usuário e pegar pares aleatórios
    #de pontos (x, y) em cada uma das subdivisões
    #para gerar o terreno.
    def __init__(self, app_width, app_height, x_div, y_min_max, mode):
        super().__init__()
        #recebendo os inteiros largura e a altura da tela do
        #jogo para que possa ser calculado as sub-divisões
        #para o terreno.
        self.app_width = app_width
        self.app_height = app_height
        self.x_div = x_div
        self.y_min_max = y_min_max
        self.points = [(0, self.app_height)] + self.generate() + [(self.app_width, self.app_height), (0, self.app_height)]
        self.image = pygame.Surface([self.app_width, self.app_height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        if mode == EARTH_MODE:
            pygame.draw.polygon(self.image, BROWN_SAND, self.points)
        elif mode == MARS_MODE:
            pygame.draw.polygon(self.image, RED_MARS, self.points)
        elif mode == MOON_MODE:
            pygame.draw.polygon(self.image, MOON_GREY, self.points)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        #self.X = []
        #self.Y = []

    def generate(self):
        #A função generate vai receber um inteiro x_div
        #contendo o número de divisões a serem feitas
        #horizontalmente e uma tupla y_min_max em que
        #sua primeira posição é um y_min e sua segunda
        #posição é um y_max. y_min_max = (y_min, y_max)

        #Definindo um tamanho relativo de
        #cada subdivisão
        divs_size = getDivSizes(self.app_width, self.x_div)

        #Dividindo X e Y e gerando os pontos do terreno
        X = XDiv(self.app_width, self.x_div, divs_size)

        Y = YDiv(X, self.y_min_max)

        #Fazendo buraco
        X, Y = mkHole(X, Y)

        self.X = X
        self.Y = Y

        return normalizeTerrain(X, Y)

    def getDiv(self, x):
        #retorna a divisão a que a coordenada x pertence
        if len(self.X) <= 0:
            raise Exception("As divisões não estão definidas. Rode o método generate(), se o erro persistir deve haver algo errado.")
        else:
            x_curr = self.X[0]
            for i in range(len(self.X) - 1):
                if x_curr <= x < self.X[i+1]:
                    return i
                x_curr = self.X[i+1]
            return -1

    def getY(self, y):
        if len(self.Y) <= 0:
            raise Exception("As divisões no Y não estão definidas. Rode o método generate(), se o erro persistir deve haver algo errado.")
        else:
            y_curr = self.Y[0]
            for i in range(len(self.Y) - 1):
                if y_curr <= y < self.Y[i+1]:
                    return i
                y_curr = self.X[i+1]
            return -1
        pass

    def onHole(self, x, y):
        #retorna True se o valor X for dentro do buraco
        #e False se for fora
        div_index = self.getDiv(x)
        y_index = self.getY(y)
        if (div_index + 1 == len(self.X) - HOLE_DIV - 2) and (self.Y[div_index - 1] <= y <= self.Y[div_index]):
            return True
        else:
            return False
