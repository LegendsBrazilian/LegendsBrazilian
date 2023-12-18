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
CUCA_SPRITE = [pygame.transform.scale(pygame.image.load("./img/cuca/cuca-1.png"), (200,200)),
               pygame.transform.scale(pygame.image.load("./img/cuca/cuca-2.png"),(200, 200)),
               pygame.transform.scale(pygame.image.load("./img/cuca/cuca-3.png") ,(200, 200)),
               pygame.transform.scale(pygame.image.load("./img/cuca/cuca-4.png") ,(200, 200)),
               pygame.transform.scale(pygame.image.load("./img/cuca/cuca-5.png") ,(200, 200)),
               pygame.transform.scale(pygame.image.load("./img/cuca/cuca-6.png") ,(200, 200)),
               pygame.transform.scale(pygame.image.load("./img/cuca/cuca-7.png") ,(200, 200)),
               ]
SACI_SPRITE = [pygame.transform.scale(pygame.image.load("./img/saci/sacy-1.png"), (300,300)),
               pygame.transform.scale(pygame.image.load("./img/saci/sacy-2.png"),(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/saci/sacy-3.png") ,(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/saci/sacy-4.png") ,(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/saci/sacy-5.png") ,(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/saci/sacy-6.png") ,(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/saci/sacy-7.png") ,(300, 300)),
               ]
MULA_SPRITE = [pygame.transform.scale(pygame.image.load("./img/mula/mula-1.png"), (300,300)),
               pygame.transform.scale(pygame.image.load("./img/mula/mula-2.png"),(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/mula/mula-3.png") ,(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/mula/mula-4.png") ,(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/mula/mula-5.png") ,(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/mula/mula-6.png") ,(300, 300)),
               pygame.transform.scale(pygame.image.load("./img/mula/mula-7.png") ,(300, 300)),
               ]

CUCA_SPRITE_INV = [pygame.transform.flip(CUCA_SPRITE[0], True, False),
                   pygame.transform.flip(CUCA_SPRITE[1], True, False),
                   pygame.transform.flip(CUCA_SPRITE[2], True, False),
                   pygame.transform.flip(CUCA_SPRITE[3], True, False),
                   pygame.transform.flip(CUCA_SPRITE[4], True, False),
                   pygame.transform.flip(CUCA_SPRITE[5], True, False),
                   pygame.transform.flip(CUCA_SPRITE[6], True, False),
                   ]
SACI_SPRITE_INV = [pygame.transform.flip(SACI_SPRITE[0], True, False),
                   pygame.transform.flip(SACI_SPRITE[1], True, False),
                   pygame.transform.flip(SACI_SPRITE[2], True, False),
                   pygame.transform.flip(SACI_SPRITE[3], True, False),
                   pygame.transform.flip(SACI_SPRITE[4], True, False),
                   pygame.transform.flip(SACI_SPRITE[5], True, False),
                   pygame.transform.flip(SACI_SPRITE[6], True, False),
                   ]
MULA_SPRITE_INV = [pygame.transform.flip(MULA_SPRITE[0], True, False),
                   pygame.transform.flip(MULA_SPRITE[1], True, False),
                   pygame.transform.flip(MULA_SPRITE[2], True, False),
                   pygame.transform.flip(MULA_SPRITE[3], True, False),
                   pygame.transform.flip(MULA_SPRITE[4], True, False),
                   pygame.transform.flip(MULA_SPRITE[5], True, False),
                   pygame.transform.flip(MULA_SPRITE[6], True, False),
                   ]

IMAGE_SACI = pygame.transform.scale(pygame.image.load(os.path.join('img', 'saci.png')), (100, 100))
IMAGE_MULA = pygame.transform.scale(pygame.image.load(os.path.join('img', 'mula.png')), (100, 100))
IMAGE_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('img', 'bg.jpeg')), (800, 800))
IMAGE_BACKGROUND_BLUR = pygame.transform.scale(pygame.image.load(os.path.join('img', 'bg_blur.jpg')), (800, 800))
IMAGE_BACKGROUND_COMBAT = pygame.transform.scale(pygame.image.load(os.path.join('img', 'bg_combate.png')), (800, 500))
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
IMAGE_CARTAZ_CUCA = pygame.transform.scale(pygame.image.load(os.path.join('img', 'cartaz_cuca.png')), (150, 150))
IMAGE_CARTAZ_MULA = pygame.transform.scale(pygame.image.load(os.path.join('img', 'cartaz_mula.png')), (150, 150))
IMAGE_CARTAZ_SACI = pygame.transform.scale(pygame.image.load(os.path.join('img', 'cartaz_saci.png')), (150, 150))
IMAGE_BANNER_VIDA = pygame.transform.scale(pygame.image.load(os.path.join('img', 'banner_vida.png')), (90, 30))
IMAGE_BANNER_VIDA_OP = pygame.transform.scale(pygame.image.load(os.path.join('img', 'banner_vida_op.png')), (90, 30))



#Fonte
FONT = 'arial'
FONT_TITLE = 'arial'