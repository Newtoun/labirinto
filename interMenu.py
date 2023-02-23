import pygame
import Botao
from LabirintoAutomatico import labirintoAutomatico
from LabirintoManual import LabirintoManual
from interface import interface
from Estado import Estado
from Gabarito import Gabarito
#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
fundo_Imagem = pygame.image.load("fundo.png")

#INSIDE OF THE GAME LOOP

#REST OF ITEMS ARE BLIT'D TO SCREEN.

def Escolhe_Criacao_Labirinto():#tela de escolha labirinto
	
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')

	#load button images
	criar_Automatico = pygame.image.load('criarAutomatico.png').convert_alpha()
	exit_img = pygame.image.load('criarManualmente.png').convert_alpha()

	#create button instances

	criar_auto = Botao.Button(50, 300, criar_Automatico, 0.6)
	exit_button = Botao.Button(420, 300, exit_img, 0.6)
	mat = labirintoAutomatico(37,27)
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo da imagem
		screen.blit(fundo_Imagem, (0, 0))

		if criar_auto.draw(screen):
			pygame.quit()
			resolve = interface(mat)
			resolve.to_execute_Automatico()
			print('START')

			pygame.quit()
		if exit_button.draw(screen):
			pygame.quit()
			resolve = interface(mat)
			resolve.to_execute_Manual()

			print('EXIT')

		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()
	pygame.quit()


def Tela_inicial():#tela inicial
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')

	#load button images
	the_maze = pygame.image.load('themaze.png').convert_alpha()
	start_img = pygame.image.load('save.png').convert_alpha()
	rafael_img = pygame.image.load('raff.png').convert_alpha()
	rafael_img2 = pygame.image.load('raffEsq.png').convert_alpha()

	#create button instances
	rafael2 = Botao.Button(600,320,rafael_img2,0.8)
	rafael3 = Botao.Button(125,320,rafael_img,0.8)
	the_maze_screen = Botao.Button(100,25,the_maze,1)
	start_button = Botao.Button(300, 300, start_img, 0.8)
	
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		the_maze_screen.draw(screen)
		rafael2.draw(screen)
		rafael3.draw(screen)

		if start_button.draw(screen):
			pygame.quit()
			pygame.time.delay(300)
			Escolhe_Criacao_Labirinto()
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()



	pygame.quit()

def Tela_Nivel():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')

	#load button images

	nivel1_img = pygame.image.load('nivel1.png').convert_alpha()


	#create button instances
	
	nivel1_button = Botao.Button(300, 300, nivel1_img, 0.8)
	
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))

		if nivel1_button.draw(screen):
			pygame.quit()
			pygame.time.delay(300)
			Escolhe_Criacao_Labirinto()
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()
	
Tela_Nivel()
