import pygame
import constants
import button
import random

start_button = button.Button((constants.WIDTH/2) - 60, constants.HEIGHT/2 - 80, constants.IMAGE_START_BUTTON, 1)
settings_button = button.Button((constants.WIDTH/2) - 60, constants.HEIGHT/2 + 100, constants.IMAGE_SETTINGS_BUTTON, 1)
mula_button = button.Button((constants.WIDTH/2) - 60, constants.HEIGHT/2 - 200, constants.IMAGE_MULA, 1)
cuca_button = button.Button((constants.WIDTH/2) - 60, constants.HEIGHT/2 - 100, constants.IMAGE_CUCA, 1)
saci_button = button.Button((constants.WIDTH/2) - 60, constants.HEIGHT/2, constants.IMAGE_SACI, 1)

class characters:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

charac = [
    characters("Saci", 100, 20, 10),
    characters("Mula sem cabeça", 120, 15, 15),
    characters("Cuca", 90, 25, 9)
]

class Combat():
    def __init__(self, jogador, adversario):
        self.jogador = jogador
        self.adversario = adversario

    def atacar(self):
        # Implementar lógica de defesa
        pass

    def defender(self):
        # Implementar lógica de defesa
        pass

    def desviar(self):
        # Implementar lógica de desvio
        pass

class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    
class Computer:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        pygame.display.set_caption(constants.TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)
        self.running = True
        self.scrn = "Menu"

    def run(self):
        self.running = True
        print("rodando")
        while self.running:
            self.clock.tick(constants.FPS)
            #self.screen.blit(constants.IMAGE_BACKGROUND, (0,0))
            if self.scrn == "Menu":
                self.screen.fill(constants.GREEN)
                if start_button.draw(self.screen):
                    self.screen.fill(constants.BLACK)
                    self.scrn = "Character"
                    pygame.display.flip()

            if self.scrn == "Character":
                self.draw_text("ESCOLHA SEU PERSONAGEM:", constants.FONT, constants.WHITE, 300, 30)
                if saci_button.draw(self.screen):
                    self.choose_player(0)
                    self.scrn = "Combat"
                if mula_button.draw(self.screen):
                    self.choose_player(1)
                    self.scrn = "Combat"
                if cuca_button.draw(self.screen):
                    self.choose_player(2)
                    self.scrn = "Combat"
                if settings_button.draw(self.screen):
                    self.scrn = "Menu"

                pygame.display.flip()

            if self.scrn == "Combat":
                self.screen.blit(constants.IMAGE_BACKGROUND, (0,0))
                self.draw_player()
                self.draw_opponent()
                Combat(self.ply, self.opp)

            self.events()
        
        self.quit_game()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        pygame.display.update()
    
    def draw_text(self, text, font, color, x, y):
        img = self.font.render(text, True, color)
        self.screen.blit(img,( x, y))

    def choose_player(self, indice):
        self.choose = charac[indice]
        print(self.choose.name)
        r = random.randint(0, 2)
        while r == indice:
            r = random.randint(0, 2)
        self.opponent = charac[r]
        print(self.opponent.name)
        self.ply = Player(self.choose.name, self.choose.health, self.choose.attack, self.choose.defense)
        self.opp = Computer(self.opponent.name, self.opponent.health, self.opponent.attack, self.opponent.defense)
    
    def draw_player(self):
        if self.choose.name == "Mula sem cabeça":
            self.screen.blit(constants.IMAGE_MULA, (30, 200))
        if self.choose.name == "Cuca":
            self.screen.blit(constants.IMAGE_CUCA, (30, 200))
        if self.choose.name == "Saci":
            self.screen.blit(constants.IMAGE_SACI, (30, 200))

    def draw_opponent(self):
        if self.opponent.name == "Mula sem cabeça":
            self.screen.blit(constants.IMAGE_MULA, (constants.WIDTH - 130, 200))
        if self.opponent.name == "Cuca":
            self.screen.blit(constants.IMAGE_CUCA, (constants.WIDTH - 130, 200))
        if self.opponent.name == "Saci":
            self.screen.blit(constants.IMAGE_SACI, (constants.WIDTH - 130, 200))

    def quit_game(self):
        print("sair")
        pygame.quit()

g = Game()
g.run()