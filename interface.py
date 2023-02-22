from LabirintoAutomatico import labirintoAutomatico
from Estado import Estado
from Gabarito import Gabarito
import pygame


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
        global rect_one
        surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        rect_one = pygame.draw.rect(surface, (0, 80, 75), (0, 0, 25, 25)) 
        #parede
        global rect_two
        surface_one = pygame.Surface((80, 80), pygame.SRCALPHA)
        rect_two = pygame.draw.rect(surface_one, (0, 255, 255), (0, 0, 25, 25))
        #tracante
        global rect_three
        surface_two = pygame.Surface((80, 80), pygame.SRCALPHA)
        rect_three = pygame.draw.rect(surface_two, (255, 153, 51), (0, 0, 25, 25)) 

        tileX = 0
        tileY = 0
        
        for y, row in enumerate(self.matriz):
            tileX = 0
            for x, cell in enumerate(row):
                if cell == 0:
                    image = surface_one
                elif cell == 1:
                    image = surface
                else:
                    image = surface_two
                self.screen.blit(image, [x*25, y*25]) 
        pygame.display.update() 


    def player(self):
        player = pygame.draw.rect(self.screen, (255,0,0), (self.x, self.y, 25, 25))   

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

        pygame.quit()

    def to_execute(self):
        estadoInicial = Estado(self.matriz,self.ponto_Inicial,self.ponto_Final,0, [])
        resposta = Gabarito.busca_Informada(estadoInicial)
        print("ESCOLHA:")
        print("DIGITE 1 PARA MANUAL")
        print("DIGITE 2 PARA AUTOMATICO")
        escolha = int(input())
        if(escolha == 1):
            self.manual()
        else:
            self.automatico(resposta)
lab = labirintoAutomatico(27,13)
mat = interface(lab)
mat.to_execute()

