import pygame

class Board(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.board = { (x,y): '0' for x in range(self.width) for y in range(self.height) }
		self.piece_active = False


	def print_board(self):
		result = ''
		for row in range(self.height):
			result += str(row) + "\t-\t"
			for col in range(self.width):
				result += self.board[(col,row)] + " "
			result +="\n"
		print(result)

	def get_board(self):
		return self.board
	
	def add_block(self, coordinates):
		self.board[coordinates] = '1'
		print("Adding Block: "+ str(coordinates))

	
	def spot_taken(self, coordinates):
		return self.board[coordinates] == '1'

	def check_row(self, coordinates):
		for x in range(self.width):
			if not self.spot_taken((x, coordinates[1])):
				return False
		return True

	def clear_row(self, coordinates):
		if self.check_row(coordinates):
			for row in reversed(range(1,coordinates[1]+1)):
				for col in range(self.width):
					self.board[(col,row)] = self.board[(col,row-1)]
			for col in range(self.width):
				self.board[(col,0)] = '0'


	def piece_done(self):
		self.piece_active = True

	def piece_new(self):
		self.piece_active = False

	def return_boxes(self):
		result = []
		for coor1, coor2 in self.board:
			if self.board[(coor1,coor2)] == '1':
				result.append((coor1,coor2))
		return result




	
	def piece_status(self):
		return self.piece_active