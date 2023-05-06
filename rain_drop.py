import pygame
from pygame.sprite import Sprite

class Rain_drop(Sprite):
    """A class to represent a single rain drop in the game"""

    def __init__(self,rain):
        """initialize the rain drop and set its starting point"""
        super().__init__()
        self.screen = rain.screen

        #Load the rain drop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
