import pygame

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        #Load background images

        self.bg_image1 = [pygame.image.load(f'images/BackGround 1 Frames/tile00{i}.png') for i in range(9)]
        self.bg_image2 = [pygame.image.load(f'images/BackGround 2 Frames/tile00{i}.png') for i in range(9)]
        self.bg_image3 = [pygame.image.load(f'images/BackGround 3 Frames/tile00{i}.png') for i in range(9)]

        #Resize background image scale
        self.bg_expand_image1 = [pygame.transform.scale_by(x, 2.25) for x in self.bg_image1]
        self.bg_expand_image2 = [pygame.transform.scale_by(x, 2.25) for x in self.bg_image2]
        self.bg_expand_image3 = [pygame.transform.scale_by(x, 2.25) for x in self.bg_image3]

        #Ship settings
        self.ship_speed = 1.5
        #This value or field was what set the initial purple background color when I started
        #self. bg_color = (41, 3, 54)