# Asteroids class creation
# import pygame and circleshape

import pygame
from circleshape import CircleShape

# define class for asteroids
class Asteroid(CircleShape):
	# define inital settings and inhertance from CircleShape
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	# draw function to convert the circle boundary to triangle shape
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position , self.radius, 2)

	# update function 
	def update(self, dt):
		self.position += self.velocity * dt
