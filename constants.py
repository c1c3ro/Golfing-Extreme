import numpy as np

#CORES
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BROWN_SKY = [249, 203, 133]
BROWN_SAND = [230, 129, 58]

# TAMANHO DA TELA / ESSE SERÁ O PADRAO
WIDTH = 800
HEIGHT = 400

#DIVISAO QUE O BURACO DA BOLA VAI FICAR
#CONTANDO DA DIREITA PRA ESQUERDA
HOLE_DIV = 2

GRAVIDADE_TERRA = 9.1

#BALL
BALL_ACC = 0.5
BALL_FRICTION = -0.1
BALL_GRAV = 0.6 #TERRA
BALL_GRAV = 0.2257 #MARTE
#BALL_GRAV = 0.09882 #LUA
COEFICIENTE_ATRITO_ESTATICO = 0.00099 #UM LIMIAR ONDE SE A FORÇA NO PLANO INCLINADO FOR MENOR QUE ISSO ELA FIC ANULA
CONSTANTE_PLANO = 30 #UMA CONSTANTE PARA DEIXAR A FORÇA NO PLANO INCLINADO MAIS REAL (TAVA MUITO FRACA)
