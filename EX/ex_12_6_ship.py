import pygame

class Ship:
    '''A Class to manage the ship.'''
    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect.
        #in pygame you can treat all elements as rectangles(rects)
        self.image = pygame.image.load('EX/images/ship_sideway.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of screen.
        self.rect.midleft = self.screen_rect.midleft

        #Store a float for the ship's exact horizontal position
        self.y =float(self.rect.y)

        #Movement flag; start with a ship that's not moving
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        '''Update the ship's position based on the movement flag.'''
        #update the ship's x value, not the rect.
        #not Transpass top
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        #not Transpass bottom
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        #Update rect object from self.y.
        self.rect.y = self.y
    
    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)