import pygame
import sys

pygame.init()

WIDTH = 400
HEIGHT = 800

GRID_WIDTH = 10
GRID_HEIGHT = 20

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode([WIDTH, HEIGHT])


game_over = False

def draw_Grid(width, height, columns, rows):
	column = width / columns
	row = height / rows

	for col in range(columns):
		x = column * col

		pygame.draw.line(screen, WHITE, [x,0], [x,HEIGHT])

	for r in range(rows):
		y = row * r
		pygame.draw.line(screen, WHITE, [0,y], [WIDTH,y])


while not game_over:

	#screen.fill(WHITE)
	draw_Grid(WIDTH,HEIGHT,GRID_WIDTH,GRID_HEIGHT)

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




