import pygame
import sys

pygame.init()

WIDTH = 400
HEIGHT = 800

GRID_WIDTH = 10
GRID_HEIGHT = 20

column = WIDTH / GRID_WIDTH
row = HEIGHT / GRID_HEIGHT

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode([WIDTH, HEIGHT])


game_over = False

def draw_Grid():

	for col in range(GRID_WIDTH):
		x = column * col

		pygame.draw.line(screen, WHITE, [x,0], [x,HEIGHT])

	for r in range(GRID_HEIGHT):
		y = row * r
		pygame.draw.line(screen, WHITE, [0,y], [WIDTH,y])


while not game_over:

	#screen.fill(WHITE)
	draw_Grid()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over == True
			sys.exit()
			pygame.quit()

		if event.type == pygame.MOUSEBUTTONDOWN:
		
			x_pos, y_pos = pygame.mouse.get_pos()
			print(x_pos)

			pygame.draw.rect(screen, WHITE, [ x_pos, y_pos, 50, 20])

	

	pygame.display.flip()

pygame.quit()




