import sys
import pygame
from random import randint

from settings import Settings
from rain_drop import Raindrop

class Rain:
    """Overall class to manage the rain game"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop Game")
        self.raindrops = pygame.sprite.Group()

        self._create_drops()


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_event()
            self._update_raindrops()
            self._screen_update()
            self.clock.tick(60)

    def _check_event(self):
        #Watch out for any key or mouse press.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)

    def _check_keydown_event(self,event):
        if event.key == pygame.K_q:
            sys.exit()

    
    def _create_drops(self):
        """Create a sky full of raindrops."""
        # Create a drop and keep adding drops until there's no room left.
        #   Spacing between drops is one drop width.
        #   Note that the spacing here works reasonably for larger drops.
        #   If you're working with smaller drops, there might be a better
        #   approach to spacing.
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size

        current_x, current_y = drop_width, drop_height
        while current_y < (self.settings.screen_height - 2 * drop_height):
            while current_x < (self.settings.screen_width - 2 * drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width

            # Finished a row; reset x value, and increment y value.
            current_x = drop_width
            current_y += 2 * drop_height

    def _create_drop(self, x_position, y_position):
        """Create a rain drop and place it in a row"""
        new_drop = Raindrop(self)
        new_drop.y = y_position
        new_drop.rect.x = x_position 
        new_drop.rect.y = y_position 
        self.raindrops.add(new_drop)

    def _create_new_row(self):
        """create a new row of raindrops after a row disappears."""
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size

        current_x = drop_width
        current_y = -1 * drop_height
        while current_x < (self.settings.screen_width - 2 * drop_width):
            self._create_drop(current_x, current_y)
            current_x += 2 * drop_width

    def _update_raindrops(self):
        """Update drop position, and look for drops that have disappeared."""
        self.raindrops.update()

        #Assume we won't make new drops
        make_new_drops = False
        for drop in self.raindrops.copy():
            if drop.check_disappeared():
                #Remove this drop, and we'll need to make new drops.
                self.raindrops.remove(drop)
                make_new_drops = True

        #Make a new row of drops if needed.
        if make_new_drops:
            self._create_new_row()


    # def _get_raindrop_offset(self):
    #     """Return a random adjustment to the raindrop position"""
    #     offset_size = 15
    #     return randint(-1 * offset_size, offset_size)

    def _screen_update(self):
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        #Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game.
    rain = Rain()
    rain.run_game()
            
