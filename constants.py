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
RED = (226, 10, 16)

#Imagens
LOGO = pygame.transform.scale(pygame.image.load(os.path.join('img', 'logo.png')), (80, 80))
IMAGE_CUCA = pygame.transform.scale(pygame.image.load(os.path.join('img', 'cuca.png')), (100, 100))
IMAGE_SACI = pygame.transform.scale(pygame.image.load(os.path.join('img', 'saci.png')), (100, 100))
IMAGE_MULA = pygame.transform.scale(pygame.image.load(os.path.join('img', 'mula.png')), (100, 100))
IMAGE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('img', 'bg.jpeg')), (800, 800))
IMAGE_BACKGROUND_BLUR = pygame.transform.scale(pygame.image.load(os.path.join('img', 'bg_blur.jpg')), (800, 800))
IMAGE_TITLE = pygame.transform.scale(pygame.image.load(os.path.join('img', 'titulo.png')), (270, 85))
IMAGE_SETTINGS_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_config.png')), (120, 80))
IMAGE_START_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_iniciar.png')), (120, 80))
IMAGE_BACK_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_voltar.png')), (100, 70))
IMAGE_ATTACK_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_atacar.png')), (120, 80))
IMAGE_SUPER_ATTACK_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_ataque_forte.png')), (120, 80))
IMAGE_DEFEND_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_defender.png')), (120, 80))
IMAGE_JUMP_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_pular.png')), (120, 80))
IMAGE_HISTORY_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_historico.png')), (120, 80))
IMAGE_QUIT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_sair.png')), (120, 80))
IMAGE_CONTINUE_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_continuar.png')), (120, 80))
IMAGE_INFO_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join('img', 'botao_info.png')), (50, 50))


#Fonte
FONT = 'arial'
FONT_TITLE = 'Helvetica'


