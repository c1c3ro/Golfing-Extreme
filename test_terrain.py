from ball import Ball
from terrain_util import getDivSizes, normalizeTerrain, XDiv, YDiv
from constants import *
import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

vec = pygame.math.Vector2

#BLACK BOX

def test_getDivSizes():
    app_width = 800
    x_div = 8
    assert getDivSizes(app_width, x_div) == 100

def test_normalizeTerrain():
    X = [1.345, 2.54, 1.90958, 3.444, 2.5683, 5.41092, 7.0912]
    Y = [2.3, 4.237, 1.985, 2.33, 5.67, 6.12, 0.001]
    assert normalizeTerrain(X, Y) == [(1, 2), (2, 4), (1, 1), (3, 2), (2, 5), (5, 6), (7, 0)]

def test_normalizeTerrain2():
    X = [-1.345, -2.54, -1.90958, -3.444, -2.5683, -5.41092, -7.0912]
    Y = [-2.3, -4.237, -1.985, -2.33, -5.67, -6.12, -0.001]
    assert normalizeTerrain(X, Y) == [(-2, -3), (-3, -5), (-2, -2), (-4, -3), (-3, -6), (-6, -7), (-8, -1)]

def test_normalizeTerrain3():
    X = [0, 0, 0, 0, 0, 0, 0]
    Y = [1, 2, 3, 4, 5, 6, 7]
    assert normalizeTerrain(X, Y) == [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]

# WHITE BOX

def test_XDiv():
    app_width = 800
    x_div = 8
    divs_size = 100
    #O tamanho da lista X retornada por XDiv é sempre x_div + 2 (o ponto final e o inicial) 
    assert len(XDiv(app_width, x_div, divs_size)) == 10

def test_XDiv2():
    app_width = 100
    x_div = 0
    divs_size = 0
    #O tamanho da lista X retornada por XDiv é sempre x_div + 2 (o ponto final e o inicial) 
    assert len(XDiv(app_width, x_div, divs_size)) == 2

def test_YDiv():
    X = [2, 3, 4, 5, 1, 2, 7]
    y_min_max = (10, 20)
    #Verifica se os valores estão mesmo limitados pelo y_min_max
    assert all(10 <= y <= 20 for y in YDiv(X, y_min_max))

def test_YDiv2():
    X = [2, 3, 4, 5, 1, 2, 7]
    y_min_max = (10, 20)
    #Verifica se a primeira e a segunda coordenadas do y são iguais como determina o código
    Y = YDiv(X, y_min_max)
    assert Y[1] == Y[2]