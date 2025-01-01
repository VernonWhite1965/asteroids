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

	# rotate player
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt


	# update player potion and rotation
	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:	# rotate left
			self.rotate(-dt)
		if keys[pygame.K_d]:	# rotate right
			self.rotate(dt)
