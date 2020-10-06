import pygame
from sprites import *
from constants import *
from terrain_generator import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf Extreme")
icon = pygame.image.load('golf-ball25.png')
pygame.display.set_icon(icon)

terrain = TerrainGenerator(WIDTH, HEIGHT, 8, (200, 320))
terrain_group = pygame.sprite.Group()
terrain_group.add(terrain)

ball = Ball()
ball_group = pygame.sprite.Group()
ball_group.add(ball)

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    terrain_group.draw(screen)

    if not pygame.sprite.groupcollide(ball_group, terrain_group, False, False):
        if not pygame.sprite.groupcollide(ball_group, terrain_group, False, False,
                                      pygame.sprite.collide_mask):
            ball_group.update()

    ball_group.draw(screen)

    pygame.display.update()


pygame.quit()