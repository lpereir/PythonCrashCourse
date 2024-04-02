'''12-6. Sideways Shooter: Write a game that places a ship on the left side of the 
screen and allows the player to move the ship up and down. Make the ship fire 
a bullet that travels right across the screen when the player presses the spacebar. Make sure bullets are deleted once they disappear off the screen'''

import sys
import pygame
from ex_12_6_settings import Settings
from ex_12_6_ship import Ship
from ex_12_6_bullet import Bullet

class SidewaysShooter:
    '''Overall class to manage game assets and behavior'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        #creating a class Clock from pygame
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #Setup as Full Screen
        #self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Sideways Shooter')

        self.ship=Ship(self)
        #l create the group that holds the bullets in __init__():
        self.bullets = pygame.sprite.Group()

        #set the background color
        #self.bg_color = (0,0,0)
    
    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            #Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            #Redraw the screen during each pass 
            #through the loop
            self._update_screen()
            #tick method takes one argument as frame rate
            #Pygame will do the best to make the loop run exactly 
            #60 times per second
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
        if event.key == pygame.K_UP:
            #Move the ship to the UP
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            #Move the ship to the DOWN
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            #Fire a bullet
            self._fire_bullet()
        #Press Q to quit
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''Respond to key releases.'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _update_bullets(self):
        #o update the position of the bullets on each pass through
        self.bullets.update()
        #get rid of bullets that have disapeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >=self.screen.get_height():
                self.bullets.remove(bullet)
            #print(len(self.bullets))


    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        #limiting bullets
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()
        
if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = SidewaysShooter()
    ai.run_game()
