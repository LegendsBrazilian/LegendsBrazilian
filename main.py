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
info_button = button.Button(constants.IMAGE_INFO_BUTTON, 1)
banner_mula = button.Button(constants.IMAGE_CARTAZ_MULA, 1)
banner_saci = button.Button(constants.IMAGE_CARTAZ_SACI, 1)
banner_cuca = button.Button(constants.IMAGE_CARTAZ_CUCA, 1)



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
                g.opp.health -= max(0, 2*g.ply.attack - g.opp.defense)
                self.tim_sa_op -= 1
            if cp_action == "super_attack":
                g.ply.health -= 2*g.opp.attack
                g.opp.health -= 2*g.ply.attack

        #se player defender
        elif player_action == "defend":
            if cp_action == "super_attack":
                g.ply.health -= max(0, 2*g.opp.attack - g.ply.defense)
            elif cp_action == "attack":
                g.ply.health -= max(0, g.opp.attack - g.ply.defense)
            

        #se player pular
        elif player_action == "jump":
            pass
        
        if player_action != "super_attack" and player_action != "jump":
            self.tim_sa_pl = max(0, self.tim_sa_pl - 1)
        
        if cp_action != "jump":
            self.tim_sa_op = max(0, self.tim_sa_op - 1)

        return cp_action
        #g.show_message(str(cp_action), 1000)


class Game:
    def __init__(self):
        #inicia o pygame
        pygame.init()
        pygame.display.set_icon(constants.LOGO)
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        pygame.display.set_caption(constants.TITLE)
        self.clock = pygame.time.Clock()

        #cria o loop do jogo
        self.running = True

        #define a primeira tela para renderizar
        self.scrn = "Menu"

        self.winner = ""

        #variaveis rolagem histõrico
        self.y = 20
        self.linVa = 50
        self.mx = 0
        self.n = 1

        self.op_ac = ""
        self.canPlay = True

        #definir a acao que o jogador fez
        self.current_action = ""

        #animacoes
        self.va_c = 0;
        self.cont_c = 0;
        self.p_x = 70


    def run(self):
        print("rodando")
        #loop principal do jogo
        while self.running:
            self.clock.tick(constants.FPS) # 30FPS
            self.screen.blit(constants.IMAGE_BACKGROUND, (0,0))

            #Menu Inicial
            if self.scrn == "Menu":
                self.screen.blit(constants.IMAGE_TITLE, (270, 100)) #renderiza o titulo //LEGENDS BRAZILIAN
                #se start_button -> tela selecionar personagem
                if start_button.draw(self.screen, (constants.WIDTH/2) - 60, constants.HEIGHT/2 + 50):
                    self.scrn = "Character" #tela selecionar personagem
                #se history_button -> tela histórico
                elif history_button.draw(self.screen, (constants.WIDTH/2) - 60, constants.HEIGHT/2 + 150):
                    self.linVa = 50 #define inicio da primeira linha
                    self.scrn = "History" # tela histórico
                #se info_button -> tela de como jogar
                elif info_button.draw(self.screen, constants.WIDTH - 60, constants.HEIGHT - 60):
                    self.scrn = "Howtoplay"#tela como jogar
            
            #Histórico de partidas
            elif self.scrn == "History":
                self.screen.blit(constants.IMAGE_BACKGROUND_BLUR, (0,0))
                self.read_data() # lê o arquivo --./data/history.txt--, aonde os dados das partidas do jogador
                self.draw_text("HISTÓRICO DE BATALHA", constants.FONT_TITLE, constants.BLACK, 300, 20)
                #se back_button -> tela Menu
                if back_button.draw(self.screen, constants.WIDTH - 150, constants.HEIGHT - 80):
                    self.scrn = "Menu"

            #Como jogar
            elif self.scrn == "Howtoplay":
                self.screen.blit(constants.IMAGE_BACKGROUND_BLUR, (0,0))
                self.read_draw_howtoplay() #le o arquivo --./data/howtoplay.txt--
                #se back_button -> tela Menu
                if back_button.draw(self.screen, constants.WIDTH - 150, constants.HEIGHT - 80):
                    self.scrn = "Menu"

            #Pause -- so esta habilitado na tela de combate
            elif self.scrn == "Pause":
                self.screen.blit(constants.IMAGE_BACKGROUND_BLUR, (0,0)) # fundo de tela
                self.screen.blit(constants.IMAGE_TITLE, (400, constants.HEIGHT/2 - 35)) #renderiza o titulo //LEGENDS BRAZILIAN
                #se continue_button -> retorna ao combate
                if continue_button.draw(self.screen, constants.WIDTH/2 - 200, constants.HEIGHT/2 -100):
                    self.scrn = "Combat"
                #se quit_button -> tela Menu
                if quit_button.draw(self.screen, constants.WIDTH/2 - 200, constants.HEIGHT/2 + 50):
                    self.scrn = "Menu"

            #Escolher personagem
            elif self.scrn == "Character":
                self.screen.blit(constants.IMAGE_BACKGROUND_BLUR, (0,0)) # fundo de tela
                self.draw_text("ESCOLHA SEU PERSONAGEM:", constants.FONT, constants.BLACK, 300, 30)
                #se banner_saci -> seleciona o personagem saci para a batalha
                if banner_saci.draw(self.screen, constants.WIDTH/2 - 325,  constants.HEIGHT/2 - 120):
                    self.choose_player(0)
                    self.scrn = "Combat"
                #se banner_mula -> seleciona o personagem mula para a batalha
                if banner_mula.draw(self.screen, constants.WIDTH/2 - 75, constants.HEIGHT/2 - 120):
                    self.choose_player(1)
                    self.scrn = "Combat"
                #se banner_cuca -> seleciona o personagem cuca para a batalha
                if banner_cuca.draw(self.screen, constants.WIDTH/2 + 175, constants.HEIGHT/2 - 120):
                    self.choose_player(2)
                    self.scrn = "Combat"
                #se back_button -> tela Menu
                if back_button.draw(self.screen, (constants.WIDTH/2) - 300, constants.HEIGHT - 100):
                    self.scrn = "Menu"

                self.current_action = "stop"
                self.canPlay = True

                

            #Tela combate
            elif self.scrn == "Combat":
                self.screen.blit(constants.IMAGE_BACKGROUND_COMBAT, (0,0))
                self.draw_text("Esc - PAUSAR", constants.FONT, constants.WHITE, 10, 10)
                #print(self.current_action)

                # animacoes de cada acao
                if self.current_action == "super_attack":
                    self.attack_ani("super_attack", self.cont_c * 10)
                    self.cont_c += 1
                    if self.cont_c == 29:
                        self.va_c = 0
                        self.cont_c = 0
                        self.canPlay = True
                        self.current_action = "stop"
                    self.draw_player()

                elif self.current_action == "attack":
                    self.attack_ani("attack", self.cont_c * 10)
                    self.cont_c += 1
                    if self.cont_c == 29:
                        self.va_c = 0
                        self.cont_c = 0
                        self.canPlay = True
                        self.current_action = "stop"
                    self.draw_player()

                elif self.current_action == "defend":
                    self.cont_c += 1
                    if self.cont_c == 29:
                        self.va_c = 0
                        self.cont_c = 0
                        self.canPlay = True
                        self.current_action = "stop"
                    self.draw_player()

                elif self.current_action == "jump":
                    self.cont_c += 1
                    if self.cont_c == 10:
                        self.va_c = 0
                        self.cont_c = 0
                        self.canPlay = True
                        self.current_action = "stop"
                    self.draw_player()

                else:
                    self.va_c = 0
                    self.draw_player()

                # renderiza vida do player
                self.screen.blit(constants.IMAGE_BANNER_VIDA, (75, 150))
                self.draw_text(str(self.ply.health), constants.FONT, constants.BLACK, 115, 155)

                # renderiza o computador e sua vida
                self.draw_opponent()
                self.screen.blit(constants.IMAGE_BANNER_VIDA_OP, (constants.WIDTH - 170, 150))
                self.draw_text(str(self.opp.health), constants.FONT, constants.BLACK, constants.WIDTH - 150, 155)

                # renderiza a ultima acao do computador
                self.draw_text(str(self.op_ac), constants.FONT, constants.WHITE, constants.WIDTH - 160, 130)


                if self.canPlay == True:
                    #se atack_button -> jogador faz a acao de atacar
                    if atack_button.draw(self.screen, 100, constants.HEIGHT - 100):
                        self.va_c = 1
                        self.current_action = "attack"
                        self.cont_c = 0
                        self.canPlay = False
                        self.op_ac = self.com.action("attack")
                    #se super_atack -> jogador faz a acao de super ataque
                    if self.com.tim_sa_pl == 0:
                        if (super_atack.draw(self.screen, 250, constants.HEIGHT - 100)):
                            self.va_c = 2
                            self.current_action = "super_attack"
                            self.cont_c = 0
                            self.canPlay = False
                            self.op_ac = self.com.action("super_attack")
                    else:
                        constants.IMAGE_SUPER_ATTACK_BUTTON.set_alpha(60)
                        self.screen.blit(constants.IMAGE_SUPER_ATTACK_BUTTON, (250, constants.HEIGHT - 100))
                    #se defense_button -> jogador faz a acao de defesa
                    if defense_button.draw(self.screen, 450, constants.HEIGHT - 100):
                        self.va_c = 4
                        self.current_action = "defend"
                        self.cont_c = 0
                        self.canPlay = False
                        self.op_ac = self.com.action("defend")
                    #se jump_button -> jogador faz a acao de pular
                    if jump_button.draw(self.screen, 600 , constants.HEIGHT - 100):
                        self.va_c = 3
                        self.current_action = "jump"
                        self.cont_c = 0
                        self.canPlay = False
                        self.op_ac = self.com.action("jump")
                
                #renderiza o numero de rodadas de espera para utilizar o super ataque novamente
                #self.draw_text(str(self.com.tim_sa_pl), constants.FONT, constants.BLACK, 300, constants.HEIGHT - 120)

                #verifica condicao termino do jogo
                #se vida do jogador chegar em 0
                if self.ply.health <= 0:
                    self.scrn = "Result" # -> Tela de Resultado
                    self.winner = "Computer" # define o computador como vencedor
                    self.write_data(str(self.ply.name), "DERROTA", str(self.opp.name)) # escreve no arquivo de dados o resultado
                    # print("Player died")
                #se vida do computador chegar em 0
                elif self.opp.health <= 0:
                    self.scrn = "Result" # -> Tela de Resultado
                    self.winner = "Player" # define o jogador como vencedor
                    self.write_data(str(self.ply.name), "VITORIA", str(self.opp.name)) # escreve no arquivo de dados o resultado
                    # print("Player Win")


            elif self.scrn == "Result":
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
                if event.button == 5:
                    if self.linVa <= self.mx:
                        self.linVa == self.mx
                    else:
                        self.linVa -= 50
                elif event.button == 4:
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
        font = pygame.font.SysFont(font, 20)
        img = font.render(text, True, color)
        self.screen.blit(img,( x, y))

    def show_message(self, message, duration):
        text = self.font.render(message, True, constants.WHITE)
        text_rect = text.get_rect(center=(constants.WIDTH // 2, constants.HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(duration)

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
    
    def attack_ani(self, atck, x):
        if atck == "attack":
            if self.choose.name == "Mula sem cabeca":
                power = constants.MULA_SPRITE[6]
            elif self.choose.name == "Cuca":
                power = constants.CUCA_SPRITE[5]
            elif self.choose.name == "Saci":
                power = constants.SACI_SPRITE[5]
        else:
            if self.choose.name == "Mula sem cabeca":
                power = constants.MULA_SPRITE[5]
            elif self.choose.name == "Cuca":
                power = constants.CUCA_SPRITE[6]
            elif self.choose.name == "Saci":
                power = constants.SACI_SPRITE[6]

    
        self.screen.blit(power, (70 + x, 130))

    def draw_player(self):
        if self.choose.name == "Mula sem cabeca":
            image = constants.MULA_SPRITE[self.va_c]
            self.screen.blit(image, (30, 120))
        if self.choose.name == "Cuca":
            image = constants.CUCA_SPRITE[self.va_c]
            self.screen.blit(image, (70, 150))
        if self.choose.name == "Saci":
            image = constants.SACI_SPRITE[self.va_c]
            self.screen.blit(image, (60, 130))

        

    def draw_opponent(self):
        if self.opp.name == "Mula sem cabeca":
            image = constants.MULA_SPRITE_INV[0]
            self.screen.blit(image, (550, 120))
        if self.opp.name == "Cuca":
            image = constants.CUCA_SPRITE_INV[0]
            self.screen.blit(image, (550, 150))
        if self.opp.name == "Saci":
            image = constants.SACI_SPRITE_INV[0]
            self.screen.blit(image, (450, 130))

    def read_data(self):
        f = "data/history.txt"
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

    def read_draw_howtoplay(self):
        f = "data/howtoplay.txt"
        with open(f, 'r', encoding='utf-8') as archive:
            lines = archive.readlines()

        self.draw_text("COMO JOGAR:", constants.FONT_TITLE, constants.BLACK, constants.WIDTH/2 - 100, 10)
        y = 30
        for li in lines:
            li.rstrip('\n')
            spl_li = li.split(" ", 1)
            if spl_li[0] == '#':
                self.draw_text(str(spl_li[1]), constants.FONT, constants.BLACK, 30, y)
            elif spl_li[0] == '*':
                self.draw_text(str(spl_li[1]), constants.FONT, constants.BLACK, 50, y)
            y += 20
            



    def write_data(self, p, r, e):
        with open('data/history.txt', 'a') as archive:
            archive.write(p + " | " + r + " | " + e + '\n')

    def quit_game(self):
        print("sair")
        pygame.quit()

g = Game()
g.run()