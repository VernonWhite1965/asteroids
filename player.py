# Player class and parameters
# import pygame, constants data, and circleshape

import pygame
from constants import *
from circleshape import CircleShape

# define class for player and pass circleshape parameters
class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0


	# draw function to convert the circle boundary to triangle shape
	def draw(self, screen):
	pygame.draw.polygon(screen, "white", self.triangle(), 2)

	# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]