import pygame
from sprites import *
from constants import *
from terrain_generator import *

import numpy as np

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf Extreme")
icon = pygame.image.load('golf-ball16.png')
pygame.display.set_icon(icon)

terrain = TerrainGenerator(WIDTH, HEIGHT, 8, (200, 320))
terrain_group = pygame.sprite.Group()
terrain_group.add(terrain)

ball = Ball()
ball_group = pygame.sprite.Group()
ball_group.add(ball)

running = True
clock = pygame.time.Clock()

moving = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Espaço!")
                ball.rect.move_ip(10, 5)
                ball.f_r = np.add(ball.f_r, np.array([20, -20]))
                moving = True
                #ball_group.update()

    terrain_group.draw(screen)
    pygame.draw.polygon(screen, BROWN_SAND, terrain.points)

    if not pygame.sprite.groupcollide(ball_group, terrain_group, False, False,
                                      pygame.sprite.collide_mask):
        moving = True
    else:
        moving = False

    ball.update(moving)

    ball_group.draw(screen)
    pygame.display.update()


pygame.quit()