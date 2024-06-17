import sys

import pygame

from settings import Settings
from ship import Ship

#Step 1
class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Initializing background images
        self.BG1 = self.settings.bg_expand_image1
        self.BG2 = self.settings.bg_expand_image2
        self.BG3 = self.settings.bg_expand_image3

        #Image initial position and index
        self.x = 0
        self.i = 0

        self.ship = Ship(self)
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    #Move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.

        # self.screen.fill(self.settings.bg_color) <---- This used to just fill the screen with the color I picked for background

        # Incrementing the index for image swapping
        self.i += 1
        self.i = self.i % len(self.BG1)
        self.i = self.i % len(self.BG2)
        self.i = self.i % len(self.BG3)

        # Drawing images at positions (x1,0), (x2,0), (x3,0)
        self.screen.blit(self.BG1[self.i], (self.x, 0))
        self.screen.blit(self.BG2[self.i], (self.x, 0))
        self.screen.blit(self.BG3[self.i], (self.x, 0))

        self.ship.blitme()

        # Make the most recently drawn screen visible
        # pygame.display.flip()
        pygame.display.update()
        #pygame.time.delay(150)  # setting delay for smooth animation

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()