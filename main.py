import pygame
import time
import constants
import button
import random

start_button = button.Button((constants.WIDTH/2) - 60, constants.HEIGHT/2 - 80, constants.IMAGE_START_BUTTON, 1)
settings_button = button.Button((constants.WIDTH/2) - 60, constants.HEIGHT/2 + 100, constants.IMAGE_SETTINGS_BUTTON, 1)
mula_button = button.Button(40, constants.HEIGHT/2 - 200, constants.IMAGE_MULA, 1)
cuca_button = button.Button(40, constants.HEIGHT/2 - 100, constants.IMAGE_CUCA, 1)
saci_button = button.Button(40,  constants.HEIGHT/2, constants.IMAGE_SACI, 1)
back_button = button.Button((constants.WIDTH/2) - 300, constants.HEIGHT - 100, constants.IMAGE_BACK_BUTTON, 1)
atack_button = button.Button((constants.WIDTH/2) - 300, constants.HEIGHT - 100, constants.IMAGE_ATTACK_BUTTON, 1)
jump_button = button.Button((constants.WIDTH/2) , constants.HEIGHT - 100, constants.IMAGE_JUMP_BUTTON, 1)
defense_button = button.Button((constants.WIDTH/2) + 200, constants.HEIGHT - 100, constants.IMAGE_DEFEND_BUTTON, 1)



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

class Combat():
    def __init__(self):
        pass

    def action(self, player_action):
        computer_action = ["defend", "jump", "attack", "attack"]
        r = random.randint(0, 3)
        cp_action = computer_action[r]
        print(cp_action)
        if player_action == "attack":
            if cp_action == "attack":
                g.ply.health -= g.opp.attack
                g.opp.health -= g.ply.attack
            elif cp_action == "defend":
                g.opp.health -= max(0, g.ply.attack - g.opp.defense)
            elif cp_action == "jump":
                pass
        elif player_action == "defend":
            if cp_action == "attack":
                g.ply.health -= max(0, g.opp.attack - g.ply.defense)
            elif cp_action == "defend":
                pass
            elif cp_action == "jump":
                pass
        elif player_action == "jump":
            if cp_action == "attack":
                pass
            elif cp_action == "defend":
                pass
            elif cp_action == "jump":
                pass

        

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        pygame.display.set_caption(constants.TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 20)
        self.running = True
        self.scrn = "Menu"
        self.current_turn = "Player"
        self.winner = ""

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

            if self.scrn == "Character":
                self.draw_text("ESCOLHA SEU PERSONAGEM:", constants.FONT, constants.WHITE, 300, 30)
                if saci_button.draw(self.screen):
                    self.choose_player(0)
                    self.scrn = "Combat"
                if mula_button.draw(self.screen):
                    self.choose_player(1)
                    self.scrn = "Combat"
                if cuca_button.draw(self.screen) and self.scrn == "Character":
                    self.choose_player(2)
                    self.scrn = "Combat"
                if back_button.draw(self.screen):
                    self.scrn = "Menu"

                pygame.display.flip()

            if self.scrn == "Combat":
                self.screen.blit(constants.IMAGE_BACKGROUND, (0,0))
                self.draw_player()
                self.draw_text(str(self.ply.health), constants.FONT, constants.BLACK, 50, 150)
                self.draw_opponent()
                self.draw_text(str(self.opp.health), constants.FONT, constants.BLACK, constants.WIDTH - 100, 150)
                if atack_button.draw(self.screen):
                    self.com.action("attack")
                    print("ataque")
                if defense_button.draw(self.screen):
                    self.com.action("defend")
                    print("defesa")
                if jump_button.draw(self.screen):
                    self.com.action("jump")
                    print("pular")

                if self.ply.health <= 0:
                    self.scrn = "Result"
                    self.winner = "Computer"
                    print("Player died")
                elif self.opp.health <= 0:
                    self.scrn = "Result"
                    self.winner = "Player"
                    print("Player Win")

            if self.scrn == "Result":
                self.screen.fill(constants.BLACK)
                if self.winner == "Player":
                    self.draw_text("Você ganhou!", constants.FONT, constants.WHITE, constants.WIDTH/2 - 100, constants.HEIGHT/2)
                else:
                    self.draw_text("Você perdeu!", constants.FONT, constants.WHITE, constants.WIDTH/2 - 100, constants.HEIGHT/2)
                    
                self.draw_text("PRECIONE QUALQUER TECLA!!!", constants.FONT, constants.WHITE, constants.WIDTH/2 - 150, constants.HEIGHT/2 + 200)
                

            self.events()
            pygame.display.flip()

        self.quit_game()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.scrn == "Result" and event.type == pygame.KEYDOWN:
                self.scrn = "Menu"
        
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
        self.com = Combat()
    
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