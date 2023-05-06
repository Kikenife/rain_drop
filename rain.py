import sys
import pygame

from settings import Settings
from rain_drop import Rain_drop

class Rain:
    """Overall class to manage the rain game"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop Game")
        self.raindrop = pygame.sprite.Group()

        self._create_raindrop()


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_event()
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

    def _screen_update(self):
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.raindrop.draw(self.screen)

        #Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_raindrop(self):
        """Create the fleet of raindrop"""
        #Create a raindrop and keep adding raindrop until there is no room left.
        #Spacing between raindrop is one raindrop width
        raindrops = Rain_drop(self)
        raindrop_width = raindrops.rect.width

        current_x = raindrop_width
        while current_x < (self.settings.screen_width - 2 * raindrop_width):
            new_raindrop = Rain_drop(self)
            new_raindrop.x = current_x
            new_raindrop.rect.x = current_x
            self.raindrop.add(new_raindrop)
            current_x += 2 * raindrop_width

if __name__ == '__main__':
    #Make a game instance, and run the game.
    rain = Rain()
    rain.run_game()
            
