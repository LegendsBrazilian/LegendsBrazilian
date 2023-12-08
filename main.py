import pygame
import time
import constants
import button
import random

start_button = button.Button(constants.IMAGE_START_BUTTON, 1)
history_button = button.Button(constants.IMAGE_HISTORY_BUTTON, 1)
#settings_button = button.Button((constants.WIDTH/2) - 60, constants.HEIGHT/2 + 100, constants.IMAGE_SETTINGS_BUTTON, 1)
mula_button = button.Button(constants.IMAGE_MULA, 1)
cuca_button = button.Button(constants.IMAGE_CUCA, 1)
saci_button = button.Button(constants.IMAGE_SACI, 1)
back_button = button.Button(constants.IMAGE_BACK_BUTTON, 1)
atack_button = button.Button(constants.IMAGE_ATTACK_BUTTON, 1)
super_atack = button.Button(constants.IMAGE_SUPER_ATTACK_BUTTON, 1)
jump_button = button.Button(constants.IMAGE_JUMP_BUTTON, 1)
defense_button = button.Button(constants.IMAGE_DEFEND_BUTTON, 1)
continue_button = button.Button(constants.IMAGE_CONTINUE_BUTTON, 1)
quit_button = button.Button(constants.IMAGE_QUIT_BUTTON, 1)



class characters:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

charac = [
    characters("Saci", 100, 20, 10),
    characters("Mula sem cabeca", 120, 15, 15),
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
    tim_sa_pl = 0;
    tim_sa_op = 0;
    def __init__(self):
        pass

    def action(self, player_action):
        computer_action = ["defend","jump", "attack", "super_attack"]
        
        if player_action == "super_attack" and self.tim_sa_pl != 0:
            return
        
        while True: 
            r = random.randint(0, 3)
            cp_action = computer_action[r]
            if (cp_action == "super_attack" and self.tim_sa_op == 0) or (cp_action != "super_attack"):
                break;

        if cp_action == "super_attack":
            self.tim_sa_op = 5

        print(cp_action)
        #se player atacar simples
        if player_action == "attack":
            if cp_action == "attack":
                g.ply.health -= g.opp.attack
                g.opp.health -= g.ply.attack
            elif cp_action == "defend":
                g.opp.health -= max(0, g.ply.attack - g.opp.defense)
            if cp_action == "super_attack":
                g.ply.health -= 2*g.opp.attack
                g.opp.health -= g.ply.attack
            if cp_action == "jump":
                pass

        # se player usar super ataque
        elif player_action == "super_attack" and self.tim_sa_pl == 0:
            self.tim_sa_pl = 5
            if cp_action == "attack":
                g.ply.health -= g.opp.attack
                g.opp.health -= 2*g.ply.attack
            elif cp_action == "defend":
                g.opp.health -= max(0, 2*g.ply.attack - int(1.5*g.opp.defense))
                self.tim_sa_op -= 1
            if cp_action == "super_attack":
                g.ply.health -= 2*g.opp.attack
                g.opp.health -= 2*g.ply.attack

        #se player defender
        elif player_action == "defend":
            if cp_action == "super_attack":
                g.ply.health -= max(0, 2*g.opp.attack - int(1.5*g.ply.defense))
            elif cp_action == "attack":
                g.ply.health -= max(0, g.opp.attack - g.ply.defense)
            

        #se player pular
        elif player_action == "jump":
            pass
        
        if player_action != "super_attack" and player_action != "jump":
            self.tim_sa_pl = max(0, self.tim_sa_pl - 1)
        
        if cp_action != "jump":
            self.tim_sa_op = max(0, self.tim_sa_op - 1)



        

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
        self.y = 20
        self.linVa = 50
        self.mx = 0
        self.n = 1

    def run(self):
        self.running = True
        print("rodando")
        while self.running:
            self.clock.tick(constants.FPS)
            #self.screen.blit(constants.IMAGE_BACKGROUND, (0,0))
            if self.scrn == "Menu":
                self.screen.fill(constants.GREEN)
                if start_button.draw(self.screen, (constants.WIDTH/2) - 60, constants.HEIGHT/2 - 100):
                    self.screen.fill(constants.BLACK)
                    self.scrn = "Character"
                elif history_button.draw(self.screen, (constants.WIDTH/2) - 60, constants.HEIGHT/2 ):
                    self.linVa = 50
                    self.scrn = "History"


            if self.scrn == "History":
                self.screen.fill(constants.RED)
                self.read_data()
                self.draw_text("HISTÓRICO DE BATALHA", constants.FONT_TITLE, constants.BLACK, 300, 20)
                if back_button.draw(self.screen, constants.WIDTH - 150, constants.HEIGHT - 80):
                    self.scrn = "Menu"

            if self.scrn == "Pause":
                self.screen.fill(constants.RED)
                if continue_button.draw(self.screen, constants.WIDTH/2 - 150, constants.HEIGHT/2 - 50):
                    self.scrn = "Combat"
                if quit_button.draw(self.screen, constants.WIDTH/2 - 150, constants.HEIGHT/2 + 40):
                    self.scrn = "Menu"

            if self.scrn == "Character":
                self.draw_text("ESCOLHA SEU PERSONAGEM:", constants.FONT, constants.WHITE, 300, 30)
                if saci_button.draw(self.screen, 40,  constants.HEIGHT/2):
                    self.choose_player(0)
                    self.scrn = "Combat"
                if mula_button.draw(self.screen, 40, constants.HEIGHT/2 - 200):
                    self.choose_player(1)
                    self.scrn = "Combat"
                if cuca_button.draw(self.screen, 40, constants.HEIGHT/2 - 100):
                    self.choose_player(2)
                    self.scrn = "Combat"
                if back_button.draw(self.screen, (constants.WIDTH/2) - 300, constants.HEIGHT - 100):
                    self.scrn = "Menu"

            if self.scrn == "Combat":
                self.screen.blit(constants.IMAGE_BACKGROUND, (0,0))
                self.draw_player()
                self.draw_text(str(self.ply.health), constants.FONT, constants.BLACK, 50, 150)
                self.draw_opponent()
                self.draw_text(str(self.opp.health), constants.FONT, constants.BLACK, constants.WIDTH - 100, 150)
                if atack_button.draw(self.screen, 100, constants.HEIGHT - 100):
                    self.com.action("attack")
                if super_atack.draw(self.screen, 250, constants.HEIGHT - 100):
                    self.com.action("super_attack")
                self.draw_text(str(self.com.tim_sa_pl), constants.FONT, constants.BLACK, 250, constants.HEIGHT - 90)
                if defense_button.draw(self.screen, 450, constants.HEIGHT - 100):
                    self.com.action("defend")
                if jump_button.draw(self.screen, 600 , constants.HEIGHT - 100,):
                    self.com.action("jump")

                if self.ply.health <= 0:
                    self.scrn = "Result"
                    self.winner = "Computer"
                    self.write_data(str(self.ply.name), "DERROTA", str(self.opp.name))
                    print("Player died")
                elif self.opp.health <= 0:
                    self.scrn = "Result"
                    self.winner = "Player"
                    self.write_data(str(self.ply.name), "VITORIA", str(self.opp.name))
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
            if self.scrn == "History" and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    if self.linVa <= self.mx:
                        self.linVa == self.mx
                    else:
                        self.linVa -= 50
                elif event.button == 5:
                    if self.linVa > 0:
                        self.linVa = 50
                    else:
                        self.linVa += 50
            if (self.scrn == "Combat" or self.scrn == "Pause") and event.type == pygame.KEYDOWN:
                key = event.key
                if pygame.key.name(key) == "escape":
                    self.scrn = "Combat" if self.scrn == "Pause" else "Pause"
            
        
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
        if self.choose.name == "Mula sem cabeca":
            self.screen.blit(constants.IMAGE_MULA, (30, 200))
        if self.choose.name == "Cuca":
            self.screen.blit(constants.IMAGE_CUCA, (30, 200))
        if self.choose.name == "Saci":
            self.screen.blit(constants.IMAGE_SACI, (30, 200))

    def draw_opponent(self):
        if self.opponent.name == "Mula sem cabeca":
            self.screen.blit(constants.IMAGE_MULA, (constants.WIDTH - 130, 200))
        if self.opponent.name == "Cuca":
            self.screen.blit(constants.IMAGE_CUCA, (constants.WIDTH - 130, 200))
        if self.opponent.name == "Saci":
            self.screen.blit(constants.IMAGE_SACI, (constants.WIDTH - 130, 200))

    def read_data(self):
        f  = "data/history.txt"
        with open(f, 'r') as archive:
            lines = archive.readlines()

        self.mx = -1 * (max(0, (len(lines)) - 5) * 110) 
        inv_li = reversed(lines)

        for li in inv_li:
            dt = li.split(" | ", 3)
            self.draw_data(dt[0], dt[1], dt[2])


    def draw_data(self, p, r, e):
        if p == "#PLAYER":
            self.y = self.linVa
            self.n = 1
            return
        
        self.draw_text(str(self.n), constants.FONT, constants.WHITE, 10, self.y + 40)

        if p == "Saci":
            self.screen.blit(constants.IMAGE_SACI, (40, self.y))
        elif p == "Cuca":
            self.screen.blit(constants.IMAGE_CUCA, (40, self.y))
        else:
            self.screen.blit(constants.IMAGE_MULA, (40, self.y))
            
        self.draw_text(str(r), constants.FONT, constants.WHITE, constants.WIDTH/2 , self.y + 40)

        if e == "Saci\n":
            self.screen.blit(constants.IMAGE_SACI, (constants.WIDTH - 120, self.y))
        elif e == "Cuca\n":
            self.screen.blit(constants.IMAGE_CUCA, (constants.WIDTH - 120, self.y))
        else:
            self.screen.blit(constants.IMAGE_MULA, (constants.WIDTH - 120, self.y))

        self.y += 110
        self.n += 1;

        

    def write_data(self, p, r, e):
        with open('data/history.txt', 'a') as archive:
            archive.write(p + " | " + r + " | " + e + '\n')

    def quit_game(self):
        print("sair")
        pygame.quit()

g = Game()
g.run()