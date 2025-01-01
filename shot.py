# Shot class creation
# import pygame and circleshape

import pygame
from constants import *
from circleshape import CircleShape

# define class for asteroids
class Shot(CircleShape):
	# define inital settings and inhertance from CircleShape
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)


	# draw function to draw circle boundary
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	# update function 
	def update(self, dt):
		self.position += self.velocity * dt
