class Settings:
    '''A Class to store all settings for Alien Invasion.'''

    def __init__(self):
        '''Initialize the game's settings.'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230,230,230)
        #Ship settings(Adjuting Ship speed)
        self.ship_speed = 5.0
        #Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

