from LabirintoAutomatico import LabirintoAutomatico
from Estado import Estado
from Gabarito import Gabarito
import pygame


speed = 25
x = y = 25
class LabirintoManual:
    def __init__(self,largura,altura):
        self.largura  = largura
        self.altura = altura
        self.matriz = self.inicializa_Matriz_Zero()
        self.ponto_Inicial = 0
        self.ponto_Final = 0
        pygame.init()
        pygame.display.set_caption("Labirinto")
        self.screen = pygame.display.set_mode((self.largura*25,self.altura*25))

    def inicializa_Matriz_Zero(self):
        mat = []     
        for i in range(self.altura):
            lista = [0]*self.largura
            mat.append(lista)
        return mat

    def imprime_Matriz(self):
        for i in range(self.altura):
            for j in range(self.largura):
                print(self.matriz[i][j],end=" ")
            print()

    def game_map(self):
        #caminho
        global rect_one
        caminho = pygame.Surface((100, 100), pygame.SRCALPHA)
        rect_one = pygame.draw.rect(caminho, (0, 80, 75), (0, 0, 25, 25)) 
        #parede
        global rect_two
        parede = pygame.Surface((80, 80), pygame.SRCALPHA)
        rect_two = pygame.draw.rect(parede, (0, 255, 255), (0, 0, 25, 25)) 

        for y in range(self.altura):
            for x in range(self.largura):
                if self.matriz[y][x] == 0:
                    image = parede
                else:
                    image = caminho
                self.screen.blit(image, [x*25, y*25]) 
        pygame.display.update()



    def player(self):
        player = pygame.draw.rect(self.screen, (255,0,0), (x, y, 25, 25))

    def escolhe_inicio_fim(self):
        global x, y
        escolhas = 0
        loop = True
        while loop:
            if escolhas==0:
                x=0
            elif escolhas==1:
                x=(self.largura-1)*25
            pygame.time.delay(100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

            #player controls
            keys = pygame.key.get_pressed()
            
            pos = x, y

            
            if keys[pygame.K_UP]:
                y -= speed
            if keys[pygame.K_DOWN]:
                y += speed                
            if keys[pygame.K_s]:
                loop = False
            if keys[pygame.K_i] and escolhas==0:
                escolhas+=1
                self.I = (x//25,y//25)
                self.matriz[y//25][x//25] = 1
            if keys[pygame.K_f] and escolhas==1:
                escolhas+=1
                self.ponto_Final = (x//25,y//25)
                self.matriz[y//25][x//25] = 1
            
            if escolhas==2:
                loop = False
            
            self.screen.fill((255,255,255))
            LabirintoManual.game_map(self)
            LabirintoManual.player(self)
            pygame.display.update()



    def manuel(self):
        global x, y
        loop = True 
        LabirintoManual.escolhe_inicio_fim(self)
        x = y  = 25
        
        while loop:
            pygame.time.delay(100)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

            #player controls
            keys = pygame.key.get_pressed()
            
            pos = x, y

            if keys[pygame.K_LEFT]:
                x -= speed
            if keys[pygame.K_RIGHT]:
                x += speed
            if keys[pygame.K_UP]:
                y -= speed
            if keys[pygame.K_DOWN]:
                y += speed    
            if keys[pygame.K_c]:
                row = y // 25
                column = x // 25
                self.matriz[row][column] = 1
            if keys[pygame.K_s]:
                loop = False

            linha = y // 25
            coluna = x // 25
            if (coluna==0 or coluna >= self.largura-1) or (linha==0 or linha >=self.altura-1):
                x, y = pos

            self.screen.fill((255,255,255))
            LabirintoManual.game_map(self)
            LabirintoManual.player(self)
            pygame.display.update()
            
        pygame.quit()



