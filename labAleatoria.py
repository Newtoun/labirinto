from labirinto import labirinto
from Estado import Estado
from Gabarito import Gabarito
import pygame

pygame.init()


pygame.display.set_caption("Labirinto")

speed = 25

altura = 11
largura = 9
ponto_inicial = 0
ponto_final = 0
screen = pygame.display.set_mode((9*25,11*25))
def inicializa_Matriz_Zero(altura,largura):
        mat = []     
        for i in range(altura):
            lista = [0]*largura
            mat.append(lista)
        return mat
x = 50
y = 50
map = inicializa_Matriz_Zero(altura,largura)



def game_map():
    #caminho
    global rect_one
    caminho = pygame.Surface((100, 100), pygame.SRCALPHA)
    rect_one = pygame.draw.rect(caminho, (0, 80, 75), (0, 0, 25, 25)) 
    #parede
    global rect_two
    parede = pygame.Surface((80, 80), pygame.SRCALPHA)
    rect_two = pygame.draw.rect(parede, (0, 255, 255), (0, 0, 25, 25)) 

    
    
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            image = parede if cell == 0 else caminho
            screen.blit(image, [x*25, y*25]) 
    pygame.display.update() 


def player():
    player = pygame.draw.rect(screen, (255,0,0), (x, y, 25, 25))   

def manuel():
    global x, y, ponto_inicial, ponto_final
    loop = True
    
    while loop:
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        #player controls
        keys = pygame.key.get_pressed()
        
        pos = x, y

        if keys[pygame.K_LEFT]:
            print("ESQ")
            x -= speed
        if keys[pygame.K_RIGHT]:
            print("DIR")
            x += speed
        if keys[pygame.K_UP]:
            y -= speed
            print('CIMA')
        if keys[pygame.K_DOWN]:
            print("BAIXO")
            y += speed    
        if keys[pygame.K_c]:
            row = y // 25
            column = x // 25
            print("CAMIN")
            map[row][column] = 1
        if keys[pygame.K_s]:
            print("SAI")
            loop = False
        if keys[pygame.K_i]:
            ponto_inicial = (x//25,y//25)
        if keys[pygame.K_f]:
            ponto_final = (x//25,y//25)

        row = y // 25
        column = x // 25
        if (column==0 or column >= largura-1) or (row==0 or row >=altura-1):
            x, y = pos

        screen.fill((255,255,255))
        game_map()
        player()
        pygame.display.update()
        
    pygame.quit()

manuel()

for i in range(altura):
    for j in range(largura):
        print(map[i][j],end=" ")
    print()
print(ponto_inicial)
print(ponto_final)

