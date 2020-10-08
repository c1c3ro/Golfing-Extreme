import pygame
from sprites import *
from constants import *
from terrain_generator import *
import math

vec = pygame.math.Vector2

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf Extreme")
icon = pygame.image.load('golf-ball8.png')
pygame.display.set_icon(icon)

terrain = TerrainGenerator(WIDTH, HEIGHT, 8, (200, 320))
terrain_group = pygame.sprite.Group()
terrain_group.add(terrain)

ball = Ball()
ball_group = pygame.sprite.Group()
ball_group.add(ball)

running = True
on_sand = False

clock = pygame.time.Clock()

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BROWN_SKY)

    if pygame.sprite.groupcollide(ball_group, terrain_group, False, False, pygame.sprite.collide_mask):
        div_index = terrain.getDiv(ball.rect.x)
        #Pegando um "vetor" que vou usar para calcular o
        #angulo entre a bola e o chão para usar no quique
        div_vec_1 = vec(terrain.X[div_index], terrain.Y[div_index])
        div_vec_2 = vec(terrain.X[div_index + 1], terrain.Y[div_index + 1])
        div_vec = div_vec_1 - div_vec_2
        #printando esse vetor para propósitos de: eu quero ver se tá tudo funcionando direito
        #print(div_vec)
        #agora eu vou pegar o vetor normal à reta que passa por div_vec_1 e div_vec_2
        normal_vec = vec(-(div_vec_2.y - div_vec_1.y), (div_vec_2.x - div_vec_1.x))
        #print(normal_vec)
        #vou pegar o os ângulos para usar na física do plano inclinado
        angle = math.atan((div_vec_2.y - div_vec_1.y)/(div_vec_2.x - div_vec_1.x))
        angle_sin = math.sin(math.radians(angle + 180))
        angle_cos = math.cos(math.radians(angle + 180))
        #print(math.degrees(angle))
        #print("Angulo: {}\nSeno: {}\nCoseno: {}".format(angle, math.sin(math.radians(angle)), math.cos(math.radians(angle))))
        #agora eu vou inverter o vetor de velocidade da bola com relação à normal do plano
        #esse vetor vai ser o quique da bola
        bounce_vec = ball.vel.reflect(normal_vec)
        #print(bounce_vec)
        #adicionando isso à velocidade da bola
        ball.vel = vec(0, 0)
        ball.vel += bounce_vec
        #aqui é onde acontece a física do plano inclinado:
        plano_inclinado = CONSTANTE_PLANO * BALL_GRAV * angle_sin
        if ball.vel.x - plano_inclinado >= COEFICIENTE_ATRITO_ESTATICO:
            ball.vel.x -= plano_inclinado
        if terrain.onHole(ball.rect.x):
            # aqui é o evento para quando a bola entra no buraco
            print('Yay! Dentro do buraco!')
        while pygame.sprite.groupcollide(ball_group, terrain_group, False, False, pygame.sprite.collide_mask):
            on_sand = True
            ball.rect.y -= 0.25
            ball.vel.y = 0
    else:
        on_sand = False


    #if hits and ball.rect.y > hits[1]:
    #    ball.rect.midbottom = hits

    terrain_group.draw(screen)
    ball_group.draw(screen)

    ball_group.update(on_sand)
    pygame.display.update()


pygame.quit()
