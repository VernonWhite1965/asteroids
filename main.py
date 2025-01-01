import sys					# import sys
import pygame					# import pygame
from constants import *				# import all from constants.py
from player import Player			# import Player from player.py
from asteroid import Asteroid			# import Asteroid from asteroid.py
from asteroidfield import AsteroidField		# import AsteroidField from asteroidfield.py
from shot import Shot				# import Shot from shot.py



def main():									# main function for asteroid gamey
	pygame.init()								# initialize pygame
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))		# set screen to height and width from constants
	clock = pygame.time.Clock()						# initalize clock from pygame

	# Groups
	updatable = pygame.sprite.Group()					# create updatable group
	drawable = pygame.sprite.Group()					# create drawable group
	asteroids = pygame.sprite.Group()					# create asteroids group
	shots = pygame.sprite.Group()						# create shots group


	# Containers
	Player.containers = (updatable, drawable)				# add player to drawable and updatable groups

	Shot.containers = (shots, updatable, drawable)				# add shot to Shots, drawable, & updatable

	Asteroid.containers = (asteroids, updatable, drawable)			# add asteroids to asteroid, drawable, and updatable groups
	AsteroidField.containers = updatable					# add asteroid fields to updatable group
	asteroid_field = AsteroidField()					# create the asteroid field


	# Initial settings
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)			# set player's  initial spawn point

	dt = 0									# set dt variable to zero


	# Game loop
	while True:								# create infinite loop with break to draw screen
		for event in pygame.event.get():				# loop thought pygame events
			if event.type == pygame.QUIT:				# provide break point to quit game
				return

		for obj in updatable:						# update objects in updatable group
			obj.update(dt)

		for asteroid in asteroids:					# checks for colisions with asteroids
			for shot in shots:
				if asteroid.collides_with(shot):
					shot.kill()
					asteroid.kill()

			if asteroid.collides_with(player):
				print("Game Over!")
				sys.exit()

		screen.fill("black")						# draw screen as black

		for obj in drawable:						# update objects in drwable group
			obj.draw(screen)

		pygame.display.flip()						# refresh screen with pygame

		dt = clock.tick(60) / 1000					# limit the framerate to 60 FPS


if __name__ == "__main__":
	main()
