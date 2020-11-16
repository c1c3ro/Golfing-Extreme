import random
import math
from constants import *

def getDivSizes(app_width, x_div):
    #Definindo um tamanho relativo de
    #cada subdivisão
    return app_width/x_div

def XDiv(app_width, x_div, divs_size):
    #O terreno vai iniciar em x = 0
    #por isso a lista de pontos x é iniciada
    #contendo um 0
    X = [0]

    for div in range(x_div):
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
    X.append(app_width)

    return X

def YDiv(X, y_min_max):
    #No Y vai funcionar de uma forma parecida:
    #eu vou gerar um número aleatório em o y_min
    #e o y_max para fazer par com cada um dos pontos X
    #e armazená-los em uma lista
    Y = []

    for x in range(len(X)):
        if x != 2:
            y = random.uniform(y_min_max[0], y_min_max[1])
            Y.append(y)
        # FAZENDO A SEGUNDA E TERCEIRA COORD Y IGUAIS PARA O TERRENO FICAR PLANO PARA A BOLA
        else:
            Y.append(Y[1])

    return Y

def mkHole(X, Y):
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

    return X, Y

def normalizeTerrain(X, Y):
    #essa função vai transformar os pontos com coordenadas float em coordenadas int
    #para evitar futuros problemas
    return [(math.floor(X[i]), math.floor(Y[i])) for i in range(len(X))]

