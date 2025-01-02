# Asteroids class creation
# import pygame and circleshape

import pygame					# import pygame
import random					# import Python's random func
from constants import *				# import all from constants.py
from circleshape import CircleShape		# import CircleShape from circleshapes.py

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


	# asteroid split or kill
	def split(self):
		self.kill()					# kill instance of asteroid

		if self.radius <= ASTEROID_MIN_RADIUS:		# check astgeroid for minimum size
			return

		random_angle = random.uniform(20, 50)		# randomize split angle

		a = self.velocity.rotate(random_angle)		# create split by using + and - andgles to vector new astorids
		b = self.velocity.rotate(-random_angle)

		new_radius = self.radius - ASTEROID_MIN_RADIUS	# create new smaller radius of medium or small asteroids

		# create two smaller asteroids at + and - vectors in medium or small size
		asteroid = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid.velocity = a * 1.2
		asteroid = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid.velocity = b * 1.2
