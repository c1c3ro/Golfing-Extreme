from ball import Ball
from physics_util import updateBall
from constants import *
import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

vec = pygame.math.Vector2

# BLACK BOX

def test_grav():
    ball = Ball(2, 100)
    assert ball.ball_grav == 0.09882

def test_updateBall1():
    ball = Ball(0, 100)
    ball.pos = vec(150, 200)
    assert updateBall(ball) == vec(150, 200.9)

def test_updateBall2():
    ball = Ball(1, 100)
    ball.pos = vec(100, 50)
    ball.vel = vec(5.3, 8)
    assert updateBall(ball) == vec(104.505, 58.33855)

def test_updateBall3():
    ball = Ball(2, 50)
    ball.pos = vec(50, 24)
    ball.vel = vec(6.8, 15.4)
    assert updateBall(ball) == vec(55.78, 39.54823)


# WHITE BOX

def test_updateBall4():
    ball = Ball(0, 100)
    ball.pos = vec(100, 200)
    ball.on_sand = True
    ball.vel = vec(0.02, 0.03)
    assert updateBall(ball) == vec(99.999, 200)

def test_updateBall5():
    ball = Ball(0, 500)
    ball.pos = vec(500, 126)
    ball.vel = vec(7.68, -10)
    assert updateBall(ball) == vec(506.528, 121.9)

def test_updateBall6():
    ball = Ball(1, 258)
    ball.pos = vec(258, 26)
    ball.vel = vec(0.035, -5)
    assert updateBall(ball) == vec(258.02975, 21.33855)

def test_updateBall7():
    ball = Ball(2, 425)
    ball.pos = vec(425.6, 0.3)
    ball.on_sand = True
    ball.vel = vec(0.0684, 0.03)
    assert updateBall(ball) == vec(425.59658, 0.300)