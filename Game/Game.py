import sys, pygame
from settings import *
from EtcFunctions import *
from Sprites import *
#Versions()
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.clock = pygame.time.Clock()
        self.is_done = False
        self.window = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(TITLE)
        

    def init_start_game(self):
        self.show_start_screen()
        while not self.is_done:
            self.new_game()
            self.show_go_screen()
        self.close()

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = player()
        self.all_sprites.add(self.player)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.moveLeft()
                if event.key == pygame.K_d:
                    self.player.moveRight()
                if event.key == pygame.K_s:
                    self.player.moveDown()
                if event.key == pygame.K_w:
                    self.player.moveUp()
    def update(self):
        #Update game loop 
        self.all_sprites.update()


    def draw(self):
        self.window.fill(BLACK)
        self.all_sprites.draw(self.window)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
        #GameOver

    def close(self):
        sys.exit
        pygame.quit


if __name__ == "__main__":
    g = Game()
    g.init_start_game()