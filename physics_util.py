import pygame
import math
from constants import *

vec = pygame.math.Vector2

def bounce(ball, terrain):
    div_index = terrain.getDiv(ball.rect.x)
    #Pegando um "vetor" que vou usar para calcular o
    #angulo entre a bola e o chão para usar no quique
    div_vec_1 = vec(terrain.X[div_index], terrain.Y[div_index])
    div_vec_2 = vec(terrain.X[div_index + 1], terrain.Y[div_index + 1])
    div_vec = div_vec_1 - div_vec_2
    #agora eu vou pegar o vetor normal à reta que passa por div_vec_1 e div_vec_2
    normal_vec = vec(-(div_vec_2.y - div_vec_1.y), (div_vec_2.x - div_vec_1.x))
    #vou pegar o os ângulos para usar na física do plano inclinado
    angle = math.atan((div_vec_2.y - div_vec_1.y)/(div_vec_2.x - div_vec_1.x))
    angle_sin = math.sin(math.radians(angle + 180))
    angle_cos = math.cos(math.radians(angle + 180))
    #agora eu vou inverter o vetor de velocidade da bola com relação à normal do plano
    #esse vetor vai ser o quique da bola
    bounce_vec = ball.vel.reflect(normal_vec)
    #adicionando isso à velocidade da bola
    ball.vel = pygame.math.Vector2(0, 0)
    ball.vel += bounce_vec

def shotIndicator(ball, screen):
    if ball.vel.magnitude() <= 3.5:
        ball.vel.x = 0
        ball.vel.y = 0
        #jogar a bola novamente
        mouse_pos = pygame.mouse.get_pos()
        try:
            dot_pos = (mouse_pos - ball.pos)/5
        except:
            return
        #desenhando a força
        for i in range(1, 6):
            pygame.draw.circle(screen, WHITE, (math.floor(i*dot_pos.x + ball.pos.x), math.floor(i*dot_pos.y + ball.pos.y)), i*2, 1)

        return mouse_pos


def updateBall(ball):
    ball.acc = vec(0, ball.ball_grav)
    if ball.on_sand:
        ball.acc = vec(0, 0)
    else:
        if ball.vel.y < -5:
            ball.vel.y = -5

    # apply friction
    ball.acc.x += ball.vel.x * BALL_FRICTION
    # equations of motion
    ball.vel += ball.acc
    if abs(ball.vel.x) < 0.1 and abs(ball.vel.y) < 0.1:
        ball.vel = vec(0, 0)
    ball.pos += ball.vel + 0.5 * ball.acc
    return ball.pos
