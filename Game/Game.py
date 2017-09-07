#TOPDOWN_SHOOTER - Tutorial game 1.
import sys, pygame
def main():
    SCREEN_WIDTH = 1080
    SCREEN_HEIGHT = 720
    FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255) 
    TITLE = "Minecraft"
    pygame.init()
    pygame.mixer.init()
    screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    clock = pygame.time.Clock()
    is_running = True
    window = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(TITLE)
    while is_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        window.fill(BLUE)
        #DRAWING CODE GOES HERE BTW M8
        pygame.display.flip()
    pygame.quit()
    sys.exit()
main()