from LabirintoAutomatico import labirintoAutomatico
from LabirintoManual import LabirintoManual
from Estado import Estado
from Gabarito import Gabarito
import pygame
from pygame import mixer


speed = 25
class interface:
    def __init__(self,matriz):
        self.altura = matriz.altura
        self.largura = matriz.largura
        self.matriz = matriz.matriz
        self.ponto_Inicial = matriz.ponto_Inicial
        self.ponto_Final = matriz.ponto_Final
        self.x = matriz.ponto_Inicial.x*25
        self.y = matriz.ponto_Inicial.y*25
        pygame.init()
        self.screen = pygame.display.set_mode((self.largura*25,self.altura*25))
        pygame.display.set_caption("Labirinto")

    def game_map(self):

        #caminho
        caminho = pygame.image.load('chaoClaro.png').convert_alpha()

        #parede
        parede = pygame.image.load('parede.png').convert_alpha()
        #tracante
        chaoEscuro = pygame.image.load('chaoEscuro.png').convert_alpha()
        #casa
        casa = pygame.image.load('casa.png').convert_alpha()
        
        
        for y, row in enumerate(self.matriz):
            for x, cell in enumerate(row):
                if cell == 0:
                    image = parede
                elif cell == 1:
                    image = caminho
                else:
                    image = chaoEscuro
                self.screen.blit(image, [x*25, y*25])
                self.screen.blit(casa, [self.ponto_Final.x*25, self.ponto_Final.y*25])  
        pygame.display.update() 


    def player(self):
        player = pygame.image.load('raffChao.png').convert_alpha()
        self.screen.blit(player, [self.x, self.y])  

    def automatico(self,resposta): ####mudar

        loop = True
        i = 0
        while loop:
            pygame.time.delay(100)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
            
            row = self.y // 25
            column = self.x // 25
            
            if self.matriz[row][column] == 1:
                self.matriz[row][column] = 2
            pos = self.x, self.y

            if resposta[i]=='left':
                self.x -= speed
            if resposta[i]=='right':
                self.x += speed
            if resposta[i]=='up':
                self.y -= speed
            if resposta[i]=='down':
                self.y += speed

            pygame.time.delay(300)
            i+=1
            row = self.y // 25
            column = self.x // 25
            if self.matriz[row][column] == 0:
                self.x, self.y = pos

            self.screen.fill((255,255,255))
            interface.game_map(self)
            interface.player(self)
            pygame.display.update()
            
            if row == self.ponto_Final.y and column == self.ponto_Final.x:
                loop = False

        pygame.quit()

    def manual(self):
        loop = True
        Retorno = False

        while loop:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

            #player controls
            keys = pygame.key.get_pressed()
            
            pos = self.x, self.y

            row = self.y // 25
            column = self.x // 25
            if self.matriz[row][column] == 1:
                self.matriz[row][column] = 2

            if keys[pygame.K_LEFT]:
                self.x -= speed
            if keys[pygame.K_RIGHT]:
                self.x += speed
            if keys[pygame.K_UP]:
                self.y -= speed
            if keys[pygame.K_DOWN]:
                self.y += speed
            
            row = self.y // 25
            column = self.x // 25
            if self.matriz[row][column] == 0:
                self.x, self.y = pos

            self.screen.fill((255,255,255))
            interface.game_map(self)
            interface.player(self)
            pygame.display.update()

            if row == self.ponto_Final.y and column == self.ponto_Final.x:
                loop = False
                Retorno = True

        pygame.quit()
        return Retorno

    def to_execute(self):#FUNCAO PARA APAGAR
        estadoInicial = Estado(self.matriz,self.ponto_Inicial,self.ponto_Final,0, [])
        resposta = Gabarito.busca_Informada(estadoInicial)
        if (len(resposta) <= 0):
            print("não tem saida")
        else:
            print("ESCOLHA:")
            print("DIGITE 1 PARA MANUAL")
            print("DIGITE 2 PARA AUTOMATICO")
            escolha = int(input())
            if(escolha == 1):
                self.manual()
            else:
                self.automatico(resposta)
    def to_execute_Manual(self):
        return self.manual()
        
    def to_execute_Automatico(self):
        estadoInicial = Estado(self.matriz,self.ponto_Inicial,self.ponto_Final,0, [])
        resposta = Gabarito.busca_Informada(estadoInicial)
        print(resposta)
        if (resposta == []):
           pygame.quit()
           return True
        else:
            self.automatico(resposta)
            return False

#mat =LabirintoManual(27,17)
#mat.manual()

#print("X: {} - Y: {}".format(mat.po))
#lab = interface(mat)
#lab.to_execute_Automatico()