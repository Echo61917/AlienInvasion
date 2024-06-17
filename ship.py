import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/Main Ship - Base - Full health.png')
        self.expand_image = pygame.transform.scale_by(self.image, 2) #This change the size of the ship
        self.rect = self.expand_image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal posiiont

        #Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 5
        if self.moving_left:
            self.rect.x -= 5

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.expand_image, self.rect)