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

class TerrainGenerator(pygame.sprite.Sprite):
    #Terrain generator é uma classe que irá
    #gerar os terrenos do desert golfing de forma
    #procedural, utilizando a biblioteca random.
    #Irei dividir a tela do jogo em quantidades
    #especificadas pelo usuário e pegar pares aleatórios
    #de pontos (x, y) em cada uma das subdivisões
    #para gerar o terreno.
    def __init__(self, app_width, app_height, x_div, y_min_max):
        super().__init__()
        #recebendo os inteiros largura e a altura da tela do
        #jogo para que possa ser calculado as sub-divisões
        #para o terreno.
        self.app_width = app_width
        self.app_height = app_height
        self.x_div = x_div
        self.y_min_max = y_min_max
        self.points = [(0, self.app_height)] + self.generate() + [(self.app_width, self.app_height), (0, self.app_height)]
        self.image = pygame.Surface([app_width, app_height], pygame.SRCALPHA, 32)
        pygame.draw.polygon(self.image, BROWN_SAND, self.points)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def generate(self):
        #A função generate vai receber um inteiro x_div
        #contendo o número de divisões a serem feitas
        #horizontalmente e uma tupla y_min_max em que
        #sua primeira posição é um y_min e sua segunda
        #posição é um y_max. y_min_max = (y_min, y_max)

        #O terreno vai iniciar em x = 0
        #por isso a lista de pontos x é iniciada
        #contendo um 0
        X = [0]

        #Definindo um tamanho relativo de
        #cada subdivisão
        divs_size = self.app_width/self.x_div

        for div in range(self.x_div):
            #Definindo o ponto inicial e final de
            #cada subdivisão no X
            div_start = X[div]
            div_end = (div + 1) * divs_size

            #Pegando um ponto x aleatório entre o início
            #e o fim da subdivisão
            x = random.uniform(div_start, div_end)

            #Por fim, eu adiciono esse ponto a lista de
            #pontos X
            X.append(x)

            #print(x)

        #Por fim, o último ponto deve ser o tamanho
        #da tela, app_width
        X.append(self.app_width)

        #print(X)

        #No Y vai funcionar de uma forma parecida:
        #eu vou gerar um número aleatório em o y_min
        #e o y_max para fazer par com cada um dos pontos X
        #e armazená-los em uma lista
        Y = []

        for x in range(len(X)):
            y = random.uniform(self.y_min_max[0], self.y_min_max[1])
            Y.append(y)

        #AQUI É ONDE EU CRIO O BURACO DA BOLA
        x_hole = X[len(X) - HOLE_DIV - 1]
        y_hole = Y[len(Y) - HOLE_DIV - 1]

        y_hole -= 15

        X.insert(len(X) - HOLE_DIV - 1, x_hole)
        Y.insert(len(Y) - HOLE_DIV - 1, y_hole)

        x_hole += 15

        X.insert(len(X) - HOLE_DIV, x_hole)
        Y.insert(len(Y) - HOLE_DIV, y_hole + 15) 

        X.insert(len(X) - HOLE_DIV, x_hole)
        Y.insert(len(Y) - HOLE_DIV, y_hole) 

        X[len(X) - HOLE_DIV] += 20

        return [(math.floor(X[i]), math.floor(Y[i])) for i in range(len(X))]
            

if __name__ == "__main__" :
    size = window_width, window_height = 800, 400

    terrain = TerrainGenerator(window_width, window_height, 8, (200, 320))
    terrain_group = pygame.sprite.Group()
    terrain_group.add(terrain)

    pygame.init()
    display = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    running = True

    while(running):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        terrain_group.draw(display)

        pygame.display.update()