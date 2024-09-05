import pygame
from constants import *

def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    while 1==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        suface = pygame.surface.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
        suface.fill("#000000")
        pygame.display.flip()

if __name__ == "__main__":
    main()