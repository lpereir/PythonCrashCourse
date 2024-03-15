#Blue Sky: Make a Pygame window with a blue background.
import sys, pygame
from ex_12_2_screensettings import Settings
from ex_12_2_character import Ship

class Bluesky:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('BlueSky Exercise')
        self.character = Ship(self)

    def run_screen(self):
        '''Starting the screen'''
        while True:
            #watch keyboard and mouse
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            #Make the most recently drawn screen visible
            pygame.display.flip()
            self.screen.fill(self.settings.bg_color)
            self.character.blitme()
if __name__ == '__main__':
    sc = Bluesky()
    sc.run_screen()