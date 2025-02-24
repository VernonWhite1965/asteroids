# Player class and parameters
# import pygame, constants data, and circleshape

import pygame					# import pygame
from constants import *				# import all from constants.py
from circleshape import CircleShape		# import CircleShape from circleshape.py
from shot import Shot				# import Shot from shot.py


# define class for player and pass circleshape parameters
class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shoot_timer = 0


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
		self.shoot_timer -= dt		# shoot timer count down after shooting

		keys = pygame.key.get_pressed()	# check for pressed keys

		if keys[pygame.K_a]:		# rotate left
			self.rotate(-dt)
		if keys[pygame.K_d]:		# rotate right
			self.rotate(dt)
		if keys[pygame.K_w]:		# move up
			self.move(dt)
		if keys[pygame.K_s]:		# move down
			self.move(-dt)
		if keys[pygame.K_SPACE]:	# player shoots
			self.shoot()


	# player position
	def  move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt


	# player shoots
	def shoot(self):
		if self.shoot_timer > 0:
			return
		self.shoot_timer = PLAYER_SHOOT_COOLDOWN
		shot = Shot(self.position.x, self.position.y)
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

