import sys
import pygame

WHITE = (255, 255, 255)

class Block(pygame.sprite.Sprite):
	def __init__(self,centerpoint, *groups):
		super(Block, self).__init__(*groups)
		self.rect = pygame.Rect(0 , 0, 64, 64)
		self.rect.center = centerpoint
		self.image = pygame.Surface(self.rect.size)
		self.image.fill(WHITE)
		self.pos = self.rect.center
		self.speed = .1

	def move(self, time):
		self.pos = self.pos[0] + (self.speed * time), self.pos[1]
		self.rect.center = self.pos

	def update(self, time):
		self.move(time)

	def draw(self, surface):
		surface.blit(self.image, self,rect)
		

class Game(object):
	def __init__(self):
		self.gameover = False
		self.width = 400
		self.height = 800
		self.screen = pygame.display.set_mode([self.width, self.height])
		self.screen_rect = self.screen.get_rect()
		self.fps = 60
		self.clock = pygame.time.Clock()
		self.spawn_timer = 0
		self.spawn_frequency = 3000 #milliseconds
		self.blocks = pygame.sprite.Group()

	def event_loop(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.gameover = True

	def update(self, time):
		self.spawn_timer += time
		if self.spawn_timer >= self.spawn_frequency:
			print("SPAWN")
			self.spawn_timer -= self.spawn_frequency
			Block((self.width/2,self.height/2), self.blocks)
		self.blocks.update(time)

	def draw(self):
		for col in range(10):
			x = self.width/10 * col
			pygame.draw.line(self.screen, WHITE, [x,0], [x,self.height])

		for row in range(20):
			y = self.height/20 * row
			pygame.draw.line(self.screen, WHITE, [0,y], [self.width, y])

		self.blocks.draw(self.screen)



	def run(self):
		while not self.gameover:
			time = self.clock.tick(self.fps)
			self.draw()
			self.event_loop()
			self.update(time)
		
			pygame.display.update()
		



if __name__ == "__main__":
	game = Game()
	game.run()
	pygame.quit()
	sys.exit()


