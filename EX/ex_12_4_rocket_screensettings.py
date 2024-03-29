'''12-4. Rocket: Make a game that begins with a rocket in the center of the screen. 
Allow the player to move the rocket up, down, left, or right using the four arrow 
keys. Make sure the rocket never moves beyond any edge of the screen.'''
class Settings:
    '''A Class to store all settings '''

    def __init__(self):
        '''Initialize the game's settings.'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (0,162,232)
        self.ship_speed = 4.5