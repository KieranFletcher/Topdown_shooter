import sys, pygame
from settings import *
from EtcFunctions import *
from Sprites import *
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.clock = pygame.time.Clock()
        self.is_done = False
        self.window = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(TITLE)
        Versions()

    def init_start_game(self):
        self.show_start_screen()
        while not self.is_done:
            self.new_game()
            self.show_go_screen()

    def new_game(self):
        self.run()

    def run(self):
        while not self.is_done:
            self.clock.tick(FPS)

            self.events()

            self.update()

            self.draw()

    def events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_done = True
        

    def update(self):
        pass

    def draw(self):

        self.window.fill(BLACK)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
        #GameOver

    def close(self):
        sys.quit
        pygame.quit

from Game import Game

if __name__ == "__main__":
    g = Game()
    g.init_start_game()