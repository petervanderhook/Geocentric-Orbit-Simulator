import pygame
from src.orb import Orb
from src.orbit import Orbit

class Screen:
    """
    Use the Screen class as a parent class for your own screens
    """

    def __init__(self, window, fps=30, bgcolor=None):
        """Constructor must receive the window"""
        self.window = window
        self.running = True
        self.fps = fps
        self.bgcolor = bgcolor
        if not self.bgcolor:
            self.bgcolor = (0, 0, 0)
        

    def loop(self):
        """Main screen loop: deals with Pygame events"""

        self.clock = pygame.time.Clock()

        while self.running:
            self.clock.tick(30)

            # Fill the screen
            self.window.fill(self.bgcolor)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    # Override this method to customize your screens!

                    # Maybe add hotkeys to slow down or increase the clock tick for faster shit.
                    self.process_event(event)

            # Override this method to customize what happens in your screens!
            result = self.process_loop()

            # Update display
            pygame.display.update()

        return result

    def process_event(self, event):
        pass

    def process_loop(self):
        pass
