import pygame
from sprites import *
from constants import *
from os import path
from terrain_generator import *
from menu import *
import math
import constants

vec = pygame.math.Vector2

pygame.init()

mode = EARTH_MODE

ball_grav = BALL_GRAV

# JOGO
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf Extreme")
icon = pygame.image.load(path.join('img', 'golf-ball8.png'))
pygame.display.set_icon(icon)
flag = pygame.image.load(path.join('img', 'flag.png'))
score = 1
score_font = pygame.font.Font("freesansbold.ttf", 10)

# SONS
background_song = pygame.mixer.Sound('sky_loop.wav')
golf_hit = pygame.mixer.Sound('golf_ball.wav')

# TERRENO
terrain = TerrainGenerator(WIDTH, HEIGHT, 8, (200, 320), mode)
terrain_group = pygame.sprite.Group()
terrain_group.add(terrain)

# BOLA
ball = Ball(mode, terrain.X[1] + 10)
ball_group = pygame.sprite.Group()
ball_group.add(ball)

menu = Menu()

running = True
on_sand = False
on_hole = 0

mouse_old = False
mouse_curr = False

clock = pygame.time.Clock()

running = menu.initial_menu(screen)

background_song.play(-1)
background_song.set_volume(0.4)

while running:
    clock.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ball.pos = (terrain.X[1] + 10, 200)
                terrain_group.remove(terrain)
                terrain = TerrainGenerator(WIDTH, HEIGHT, 8, (200, 320), mode)
                terrain_group.add(terrain)
                on_hole = 0
                score += 1


    if mode == EARTH_MODE:
        screen.fill(BROWN_SKY)
    elif mode == MARS_MODE:
        screen.fill(SKY_MARS)
    elif mode == MOON_MODE:
        screen.fill(SKY_MOON)

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
        #plano_inclinado = CONSTANTE_PLANO * ball_grav * angle_sin
        #if ball.vel.x - plano_inclinado >= COEFICIENTE_ATRITO_ESTATICO:
        #    ball.vel.x -= plano_inclinado
        if terrain.onHole(ball.rect.x, ball.rect.y):
            # aqui é o evento para quando a bola entra no buraco
            print('Yay! Dentro do buraco!')
            on_hole += 1

        '''else:
            #apenas para propositos de debug
            x_div = terrain.getDiv(ball.rect.x)
            print('X_div: {}, Y[div]: {}, Y[div + 1]: {}'.format(x_div, terrain.Y[x_div-1], terrain.Y[x_div]))'''

        
        '''vel_mag = ball.vel.magnitude()
        print(vel_mag)
        if vel_mag < 1.5:
            ball.vel.x = 0
            ball.vel.x = 0'''
        while pygame.sprite.groupcollide(ball_group, terrain_group, False, False, pygame.sprite.collide_mask):
            on_sand = True
            ball.rect.y -= 0.5
            #verificando se a velocidade da bola está pequena demais:
            #print(ball.vel, ball.vel.magnitude())
            if ball.vel.magnitude() <= 1.5:
                ball.vel.x = 0
                ball.vel.y = 0
                #jogar a bola novamente
                mouse_pos = pygame.mouse.get_pos()
                try:
                    dot_pos = (mouse_pos - ball.pos)/5
                except:
                    continue
                #desenhando a força
                for i in range(1, 6):
                    pygame.draw.circle(screen, WHITE, (math.floor(i*dot_pos.x + ball.pos.x), math.floor(i*dot_pos.y + ball.pos.y)), i*2, 1)

                mouse_curr = pygame.mouse.get_pressed()[0]

                if(mouse_curr == False and mouse_old == True):
                    mouse_old = mouse_curr
                    #agora joga a bola
                    golf_hit.play()
                    traction = vec(K_FORCE * (mouse_pos - ball.pos).x, K_FORCE * (mouse_pos - ball.pos).y)
                    ball.vel += traction
                    on_sand = False


            #ball.vel.y = 0
    else:
        on_sand = False

    if ball.rect.x < 0 or ball.rect.x > WIDTH:
        ball.pos = (terrain.X[1] + 10, 200)
        ball.vel = vec(0, 0)
        ball.acc = vec(0, 0)

    if on_hole > 100:
        ball.pos = (terrain.X[1] + 10, 200)
        terrain_group.remove(terrain)
        terrain = TerrainGenerator(WIDTH, HEIGHT, 8, (200, 320), mode)
        terrain_group.add(terrain)
        on_hole = 0
        score += 1

    terrain_group.draw(screen)
    
    if menu.firt:
        menu.firt = False
        running = menu.help(screen)
    
    ball_group.draw(screen)

    # DESENHANDO A BANDEIRA
    screen.blit(flag, (terrain.X[-3] - 2, terrain.Y[-3] - 20))
    screen.blit(score_font.render(str(score), True, WHITE), (terrain.X[-3] + 3, terrain.Y[-3] - 18))


    mouse_old = mouse_curr

    ball_group.update(on_sand)
    pygame.display.update()


pygame.quit()
