'''12-5. Keys: Make a Pygame file that creates an empty screen. In the event loop, 
print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run 
the program and press various keys to see how Pygame responds'''

import sys, pygame
from ex_12_5_keys_screensettings import Settings

class Keys:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('KEYS Exercise')

    def run_screen(self):
        '''Starting the screen'''
        while True:
            #Check events
            self._check_events()
            self.clock.tick(60)


    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        #Press Q to quit
        if event.key == pygame.K_q:
            sys.exit()
        # Set up the font
        font = pygame.font.Font(None, 48)
        # Get the name of the key
        key_name=''
        if key_name != pygame.key.name(event.key):
            self._update_screen()
            key_name = pygame.key.name(event.key)
        # Render the text onto the surface
        text_surface = font.render(key_name, True, (120, 120, 120))
        # Get the rectangle of the text surface
        text_rect = text_surface.get_rect(center=(800 // 2, 400 // 2))
        # Blit the text surface onto the screen
        self.screen.blit(text_surface, text_rect)
        # Update the display
        pygame.display.flip()
              
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        #Make the most recently drawn screen visible.
        #self.screen.blit(self.text_surface, self.text_rect)
        pygame.display.flip()


if __name__ == '__main__':
    sc = Keys()
    sc.run_screen()