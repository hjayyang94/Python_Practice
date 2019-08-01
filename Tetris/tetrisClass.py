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
Board = Board(WIDTH,HEIGHT)

class Block(pygame.sprite.Sprite):
	def __init__(self,centerpoint, *groups):
		super(Block, self).__init__(*groups)
		self.rect = pygame.Rect(0 , 0, WIDTH_BLOCK, HEIGHT_BLOCK)
		self.rect.center = centerpoint
		self.image = pygame.Surface(self.rect.size)
		self.image.fill(WHITE)
		self.pos = self.rect.center
		self.timer = 0
		self.stop = False

	def move(self, time, direction):

		self.timer += time
		if self.timer >= 1000:  #spawn every second
			self.pos = self.pos[0] , self.pos[1] + HEIGHT_BLOCK
			self.timer = 0

		if direction == "left":
			self.pos = self.pos[0] - WIDTH_BLOCK, self.pos[1]
		elif direction == "right":
			self.pos = self.pos[0] + WIDTH_BLOCK, self.pos[1]
		elif direction == "down":
			self.pos = self.pos[0] , self.pos[1] + HEIGHT_BLOCK
		self.rect.center = self.pos
	

	def update(self, time, direction = ''):
		if self.pos[1] >= HEIGHT - HEIGHT_BLOCK:
			self.stop = True	

		if not self.stop:
			self.move(time, direction)

	def draw(self, surface):
		surface.blit(self.image, self.rect)
		

class Game(object):
	def __init__(self):
		self.gameover = False
		self.width = WIDTH
		self.height = HEIGHT
		self.width_block = WIDTH_BLOCK
		self.height_block = HEIGHT_BLOCK
		self.screen = pygame.display.set_mode([self.width, self.height])
		self.screen_rect = self.screen.get_rect()
		self.fps = 60
		self.clock = pygame.time.Clock()
		self.blocks = pygame.sprite.Group()
		self.new_piece = True


	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.gameover = True

			#elif event.type == pygame.key.get_pressed():
			#	if keys[pygame.K_DOWN]:
			#		print('holding key')
			#		self.blocks.update(0,'down')
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.blocks.update(0,'left')
				elif event.key == pygame.K_RIGHT:
					self.blocks.update(0,'right')
				elif event.key == pygame.K_DOWN:
					self.blocks.update(0,'down')

	def new_piece():
		self.new_piece = True	

	def update(self, time):
		if self.new_piece == True:
			x = random.randint(1,11)
			Block((x * WIDTH_BLOCK - WIDTH_BLOCK/2, HEIGHT_BLOCK/2), self.blocks)
			self.new_piece = False
		self.blocks.update(time)

	def draw(self):
		self.screen.fill(BLACK)
		for col in range(10):
			x = self.width_block * col
			pygame.draw.line(self.screen, WHITE, [x,0], [x,self.height])

		for row in range(20):
			y = self.height_block * row
			pygame.draw.line(self.screen, WHITE, [0,y], [self.width, y])

		self.blocks.draw(self.screen)



	def run(self):
		while not self.gameover:
			time = self.clock.tick(self.fps)
			
			self.event_loop()
			self.update(time)
			self.draw()
		
			pygame.display.update()
		



if __name__ == "__main__":
	game = Game()
	game.run()
	pygame.quit()
	sys.exit()


