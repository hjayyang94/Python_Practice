import sys
import pygame
import random
from tetris_board import Board

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

WIDTH = 400
HEIGHT = 800
NUM_COL = 10
NUM_ROW = 20

NEW_PIECE = True

WIDTH_BLOCK= WIDTH/NUM_COL
HEIGHT_BLOCK= HEIGHT/NUM_ROW

Board = Board(NUM_COL,NUM_ROW)

class Block():
	def __init__(self, coordinates):
		self.rect = pygame.Rect(0 , 0, WIDTH_BLOCK, HEIGHT_BLOCK)
		self.rect.center = (coordinates[0] * WIDTH_BLOCK + WIDTH_BLOCK/2, coordinates[1] * HEIGHT_BLOCK + HEIGHT_BLOCK/2)
		self.image = pygame.Surface(self.rect.size)
		self.image.fill(WHITE)
		self.pos = self.rect.center
		self.timer = 0
		self.coordinates = coordinates

	def __del__(self):
		del self.rect
		del self.image
		del self.pos
		del self.timer
		del self.coordinates
		print("Block Deleted")

	def move(self, direction):
		if direction == "left" and self.coordinates[0] > 0 and not Board.spot_taken((self.coordinates[0] - 1, self.coordinates[1])):
			self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
		elif direction == "right" and self.coordinates[0] < NUM_COL-1 and not Board.spot_taken((self.coordinates[0] + 1, self.coordinates[1])):
			self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])

		elif direction == "down":
			if self.coordinates[1] < NUM_ROW-1 and Board.spot_taken((self.coordinates[0],self.coordinates[1]+1)):
				self.place_piece(self.coordinates)
				

			elif not self.coordinates[1] >= NUM_ROW-1:
				self.coordinates = (self.coordinates[0], self.coordinates[1]+1)
			else:
				self.place_piece(self.coordinates)

		self.coord_to_pos()

	def update(self, time, direction = ''):
		self.timer += time
		if self.timer >= 1000:
			self.timer = 0
			self.move('down')
		elif direction:
			self.move(direction)

	def coord_to_pos(self):
		self.rect.center = (self.coordinates[0] * WIDTH_BLOCK + WIDTH_BLOCK/2, self.coordinates[1] * HEIGHT_BLOCK + HEIGHT_BLOCK/2)

	def draw(self, surface):
		surface.blit(self.image, self.rect)

	def place_piece(self, coordinates):
		Board.add_block(coordinates)
		Board.piece_new()

		Board.clear_row(coordinates)


class Game(object):
	def __init__(self):
		self.gameover = False
		self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
		self.screen_rect = self.screen.get_rect()
		self.fps = 60
		self.clock = pygame.time.Clock()
		self.block = None
		self.new_piece = True
		self.block_done = []

	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.gameover = True

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
						self.block.update(0,'left')
				elif event.key == pygame.K_RIGHT:
						self.block.update(0,'right')
				elif event.key == pygame.K_DOWN:
						self.block.update(0,'down')
	
	def update(self, time):

		if not Board.piece_status():
			x = random.randint(0,NUM_COL-1)
			block = Block((x,0))
			print("Spawn")
			self.block = block
			Board.piece_done()
		#else:
			
			
		self.block.update(time)

	def draw(self):
		self.screen.fill(BLACK)
		for col in range(NUM_COL):
			x = WIDTH_BLOCK * col
			pygame.draw.line(self.screen, WHITE, [x,0], [x, HEIGHT])

		for row in range(NUM_ROW):
			y = HEIGHT_BLOCK * row
			pygame.draw.line(self.screen, WHITE, [0,y], [WIDTH, y])

		#for block in self.blocks:
		self.block.draw(self.screen)
		self.draw_existing(Board.return_boxes(), self.screen)	

	def draw_existing(self, list_boxes, surface):
		for box in list_boxes:
			rect = pygame.Rect(0 , 0, WIDTH_BLOCK, HEIGHT_BLOCK)
			rect.center = ((box[0] * WIDTH_BLOCK + WIDTH_BLOCK/2, box[1] * HEIGHT_BLOCK + HEIGHT_BLOCK/2))
			
			image = pygame.Surface(rect.size)
			image.fill(WHITE)


			image = pygame.Surface(rect.size)
			image.fill(WHITE)
			surface.blit(image, rect)

	def run(self):
		while not self.gameover:
			time = self.clock.tick(self.fps)
		
			self.event_loop()
			self.update(time)
			self.draw()
		
			pygame.display.update()
		Board.print_board()

if __name__ == "__main__":
	game = Game()
	game.run()
	pygame.quit()
	sys.exit()