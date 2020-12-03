import pygame
from menu import Menu
from constants import *

pygame.init()

#As funçoes testadas recebem os inputs atraves da interface#

# WHITE BOX

def test_animationclose():#fechar janela
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    expect= menu.animation(screen)
    assert expect == False
    
def test_animation():
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    expect= menu.animation(screen)
    assert expect == True

# BLACK BOX

def test_initial_menustart():#clicar no botão start
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    expect = menu.initial_menu(screen)
    assert expect == True

def test_initial_menuexit():#clicar no botão exit
    menu = Menu()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    expect = menu.initial_menu(screen)
    assert expect == False
