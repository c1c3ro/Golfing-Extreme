import pygame
from sprites import *
from constants import *
from os import path
from terrain_generator import *
from menu import *
import math
import constants
from physics_util import *

vec = pygame.math.Vector2

pygame.init()

mode = 0

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
                score += 1
                if score == 11:
                    mode += 1
                    score = 1
                ball.pos = (terrain.X[1] + 10, 200)
                terrain_group.remove(terrain)
                terrain = TerrainGenerator(WIDTH, HEIGHT, 8, (200, 320), mode)
                terrain_group.add(terrain)
                on_hole = 0



    if mode == EARTH_MODE:
        screen.fill(BROWN_SKY)
    elif mode == MARS_MODE:
        screen.fill(SKY_MARS)
    elif mode == MOON_MODE:
        screen.fill(SKY_MOON)

    if pygame.sprite.groupcollide(ball_group, terrain_group, False, False, pygame.sprite.collide_mask):
        #quique da bola
        bounce(ball, terrain)

        if terrain.onHole(ball.rect.x, ball.rect.y):
            # aqui é o evento para quando a bola entra no buraco
            print('Yay! Dentro do buraco!')
            on_hole += 1

        while pygame.sprite.groupcollide(ball_group, terrain_group, False, False, pygame.sprite.collide_mask):
            on_sand = True
            ball.rect.y -= 0.5
            
            #Desenhando o indicador de força da tacada
            mouse_pos = shotIndicator(ball, screen)

            #tacada do golfe
            mouse_curr = pygame.mouse.get_pressed()[0]

            if(mouse_curr == False and mouse_old == True):
                mouse_old = mouse_curr
                #agora joga a bola
                golf_hit.play()
                traction = vec(K_FORCE * (mouse_pos - ball.pos).x, K_FORCE * (mouse_pos - ball.pos).y)
                ball.vel += traction
                on_sand = False
    else:
        on_sand = False

    if ball.rect.x < 0 or ball.rect.x > WIDTH:
        ball.pos = (terrain.X[1] + 10, 200)
        ball.vel = vec(0, 0)
        ball.acc = vec(0, 0)

    if on_hole > 100:
        score += 1
        if score == 11:
            mode += 1
            score = 1
        ball.pos = (terrain.X[1] + 10, 200)
        terrain_group.remove(terrain)
        terrain = TerrainGenerator(WIDTH, HEIGHT, 8, (200, 320), mode)
        terrain_group.add(terrain)
        on_hole = 0

    if score == 11:
        mode += 1
        score = 1

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
