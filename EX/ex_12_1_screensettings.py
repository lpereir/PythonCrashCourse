#Blue Sky: Make a Pygame window with a blue background.
class Settings:
    '''A Class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's settings.'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,0,250)