# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def start_pygame(self):
""" Initialize pygame system stuff and draw empty window """
    if not pygame.display.get_init():
        pygame.display.init()
    if not pygame.font.get_init():
        pygame.font.init()

def game_loop(self):
    While True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen = pygame.display.set_mode((SCEEN_WIDHR, SCREEN_HEIGHT))
	pygame.display.flip()



def main():
    start_pygame()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #pygame.display.flip()
    game_loop()



if __name__ == "__main__":
    main()

