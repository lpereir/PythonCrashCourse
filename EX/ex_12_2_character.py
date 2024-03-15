#Blue Sky: Make a Pygame window with a blue background.
import pygame

class Ship:
    def __init__(self,gc_game):
        '''initialize the character and set its starting position'''
        self.screen = gc_game.screen
        self.screen_rect = gc_game.screen.get_rect()

        #load the image and get its rect
        self.image = pygame.image.load('EX/images/ship_16.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)




