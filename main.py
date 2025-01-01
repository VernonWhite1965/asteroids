# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
	# Init pygame and set screen parameter to width and height from constants.txt
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# start pygame clock and set delta time (dt) to zero
	clock = pygame.time.Clock()
	dt = 0

	# print starting game and screen size
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


	# infinite loop to start the game screen with abilty to quit
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		pygame.display.flip()
		
		# limit framerate to 60 fps
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
