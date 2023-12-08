import pygame
import os

#Dimensões da tela
WIDTH = 800
HEIGHT = 500

#Título do jogo
TITLE = 'LEGENDS BRAZILIAN'

#FPS
FPS = 30

#Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (244, 233, 51)
GREEN = (30, 255, 10)

#Imagens

IMAGE_CUCA = pygame.transform.scale(pygame.image.load(os.path.join('img', 'cuca.png')), (100, 100))
IMAGE_SACI = pygame.transform.scale(pygame.image.load(os.path.join('img', 'saci.png')), (100, 100))
IMAGE_MULA = pygame.transform.scale(pygame.image.load(os.path.join('img', 'mula.png')), (100, 100))
IMAGE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('img', 'bg.jpg')), (800, 500))
IMAGE_SETTINGS_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_config.png')), (120, 80))
IMAGE_START_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_iniciar.png')), (120, 80))
IMAGE_BACK_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_voltar.png')), (120, 80))
IMAGE_ATTACK_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_atacar.png')), (120, 80))
IMAGE_DEFEND_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_defender.png')), (120, 80))
IMAGE_JUMP_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_pular.png')), (120, 80))


#Fonte
FONT = 'arial'


