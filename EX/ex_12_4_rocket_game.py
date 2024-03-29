'''12-4. Rocket: Make a game that begins with a rocket in the center of the screen. 
Allow the player to move the rocket up, down, left, or right using the four arrow 
keys. Make sure the rocket never moves beyond any edge of the screen.'''

import sys, pygame
from ex_12_4_rocket_screensettings import Settings
from ex_12_4_rocket_ship import Ship

class Rocketgame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Rocket Game Exercise')
        self.ship = Ship(self)

    def run_screen(self):
        '''Starting the screen'''
        while True:
            #Make the most recently drawn screen visible
            #pygame.display.flip()
            #self.screen.fill(self.settings.bg_color)
            #self.character.blitme()
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.clock.tick(60)


    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT:
            #Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            #Move the ship to the UP
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            #Move the ship to the DOWN
            self.ship.moving_down = True
        
        #Press Q to quit
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    sc = Rocketgame()
    sc.run_screen()