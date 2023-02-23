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
	start_img = pygame.image.load('save.png').convert_alpha()
	exit_img = pygame.image.load('exitD.png').convert_alpha()

	#create button instances

	start_button = Botao.Button(125, 350, start_img, 0.8)
	exit_button = Botao.Button(450, 350, exit_img, 0.8)

	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		if start_button.draw(screen):
			pygame.quit()
			pygame.time.delay(300)
			Escolhe_Criacao_Labirinto()
			print('START')

			#pygame.quit()
		if exit_button.draw(screen):
			pygame.quit()
			print('EXIT')

		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()



	pygame.quit()


Tela_inicial()