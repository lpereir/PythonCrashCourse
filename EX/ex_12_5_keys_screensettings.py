'''12-5. Keys: Make a Pygame file that creates an empty screen. In the event loop, 
print the event.key attribute whenever a pygame.KEYDOWN event is detected. Run 
the program and press various keys to see how Pygame responds'''

class Settings:
    '''A Class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's settings.'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (0,0,0)