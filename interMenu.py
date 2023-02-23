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
	nv_Dificuldade = pygame.image.load("nivel_De_Dificuldade.png")

	#load button images

	nivel1_img = pygame.image.load('nivel1.png').convert_alpha()
	nivel2_img = pygame.image.load('nivel2.png').convert_alpha()
	nivel3_img = pygame.image.load('nivel3.png').convert_alpha()


	#create button instances
	
	nivel1_button = Botao.Button(300, 240, nivel1_img, 0.8)
	nivel2_button = Botao.Button(300, 325, nivel2_img, 0.8)
	nivel3_button = Botao.Button(300, 410, nivel3_img, 0.8)

	
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(nv_Dificuldade, (50, 0))

		if nivel1_button.draw(screen):
			pygame.quit()
			pygame.time.delay(300)
			Escolhe_Criacao_Labirinto()
		if nivel2_button.draw(screen):
			return
		if nivel3_button.draw(screen):
			return
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()

def Tela_criar_labirinto():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	criar_labirinto = pygame.image.load("criar_lab.png")
	predio = pygame.image.load("predio.png")
	
	#load button images
	manual_img = pygame.image.load('manualmente.png').convert_alpha()
	auto_img = pygame.image.load('automaticamente.png').convert_alpha()
	#create button instances
	manual_button = Botao.Button(250, 250, manual_img, 0.8)
	auto_button = Botao.Button(250, 360, auto_img, 0.8)
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(criar_labirinto, (100, 25))
		screen.blit(predio, (600, 303))

		if manual_button.draw(screen):
			pygame.quit()
			pygame.time.delay(300)
			Escolhe_Criacao_Labirinto()
		if auto_button.draw(screen):
			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()

def tela_Resolver():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	criar_labirinto = pygame.image.load("resolver_lab.png")
	predio = pygame.image.load("predio.png")
	
	#load button images
	manual_img = pygame.image.load('manualmente.png').convert_alpha()
	auto_img = pygame.image.load('automaticamente.png').convert_alpha()
	#create button instances
	manual_button = Botao.Button(250, 250, manual_img, 0.8)
	auto_button = Botao.Button(250, 360, auto_img, 0.8)
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(criar_labirinto, (100, 25))
		screen.blit(predio, (600, 303))

		if manual_button.draw(screen):
			pygame.quit()
			pygame.time.delay(300)
			Escolhe_Criacao_Labirinto()
		if auto_button.draw(screen):
			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()
	return

def tela_Ganhou():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	parabens_img = pygame.image.load("parabens.png")
	raff = pygame.image.load("rafeChegou.png")
	continuar = pygame.image.load("continuar.png")
	
	#load button images
	yes_img = pygame.image.load('yes.png').convert_alpha()
	no_img = pygame.image.load('no.png').convert_alpha()
	#create button instances
	yes_button = Botao.Button(150, 340, yes_img, 0.8)
	no_button = Botao.Button(450, 340, no_img, 0.8)
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(parabens_img, (140, 0))
		screen.blit(raff, (200,140))
		screen.blit(continuar, (170,200))

		if yes_button.draw(screen):
			pygame.quit()
			pygame.time.delay(300)
			Escolhe_Criacao_Labirinto()
		if no_button.draw(screen):
			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()

def tela_Sem_Solucao():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Labirinto')
	semSolucao_img = pygame.image.load("semSolucao.png")
	continuar = pygame.image.load("continuar.png")
	
	#load button images
	yes_img = pygame.image.load('yes.png').convert_alpha()
	no_img = pygame.image.load('no.png').convert_alpha()
	#create button instances
	yes_button = Botao.Button(150, 340, yes_img, 0.8)
	no_button = Botao.Button(450, 340, no_img, 0.8)
	#game loop
	run = True
	while run:

		screen.fill((202, 228, 241))
		#desenha fundo
		screen.blit(fundo_Imagem, (0, 0))
		screen.blit(semSolucao_img, (140, 5))
		screen.blit(continuar, (150,200))

		if yes_button.draw(screen):
			pygame.quit()
			pygame.time.delay(300)
			Escolhe_Criacao_Labirinto()
		if no_button.draw(screen):
			return
		
		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
		pygame.display.update()
	pygame.quit()
	


tela_Sem_Solucao()