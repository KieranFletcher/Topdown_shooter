import sys, pygame
print("Commit V0.1")
class Game:
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255) 
    WEIRD1 = (255, 153, 89)
    TITLE = "Test game indev"
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        clock = pygame.time.Clock()
        is_running = True
        window = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(TITLE)

    def init_start_game(self):
        self.show_start_screen()
        while not self.is_done:
            self.new_game()
            self.show_go_screen()

    def new_game(self):
        self.run()

    def run(self):
        while not self.is_done:
            self.clock.tick(settings.FPS)

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
