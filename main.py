import pygame
from sprites import *
from constants import *
from terrain_generator import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf Extreme")
icon = pygame.image.load('golf-ball10.png')
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

    #hits = pygame.sprite.groupcollide(ball_group, terrain_group, False, False,
    #                                  pygame.sprite.collide_mask)

    hits = pygame.sprite.collide_mask(terrain, ball)
    if hits:
        on_sand = True
        ball.rect.midbottom = hits
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
