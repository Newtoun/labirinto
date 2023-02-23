import pygame
import Botao
from LabirintoAutomatico import labirintoAutomatico
from LabirintoManual import LabirintoManual
from interface import interface
#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
bg = pygame.image.load("fundo.png")

#INSIDE OF THE GAME LOOP

#REST OF ITEMS ARE BLIT'D TO SCREEN.

def Escolhe_Criacao_Labirinto():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen.blit(bg, (0, 0))
	pygame.display.set_caption('Labirinto')

	#load button images
	criar_Automatico = pygame.image.load('criarAutomatico.png').convert_alpha()
	exit_img = pygame.image.load('criarManualmente.png').convert_alpha()

	#create button instances

	start_button = Botao.Button(50, 300, criar_Automatico, 0.6)
	exit_button = Botao.Button(420, 300, exit_img, 0.6)

	#game loop
	run = True
	MAT = labirintoAutomatico(11,9)
	while run:

		screen.fill((202, 228, 241))

		if start_button.draw(screen):

			print('START')

			#pygame.quit()
		if exit_button.draw(screen):

			print('EXIT')

		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()



	pygame.quit()


def Tela_inicial():
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
	MAT = labirintoAutomatico(11,9)
	while run:

		screen.fill((202, 228, 241))
		screen.blit(bg, (0, 0))
		if start_button.draw(screen):
			Escolhe_Criacao_Labirinto()
			print('START')

			#pygame.quit()
		if exit_button.draw(screen):

			print('EXIT')

		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()



	pygame.quit()

Escolhe_Criacao_Labirinto()