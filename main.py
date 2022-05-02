from src.orb import Orb
from src.orbit import Orbit
from src.constants import WINDOW_X, WINDOW_Y
from src.glow_screen import GlowScreen
import pygame
def main():
    pygame.init()

    window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

    glow_screen = GlowScreen(window)
    glow_screen.loop()


if __name__ == "__main__":
    main()