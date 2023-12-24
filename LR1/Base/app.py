import sys, pygame
from myCanvas import MyCanvas

class App:
    is_running = True
    screen = None
    canvas = None
    fill_color = (255, 255, 255)

    def __init__(self, name, screen_size):
        pygame.init()
        pygame.display.set_caption(name)
        self.screen = pygame.display.set_mode(screen_size)
        self.canvas = MyCanvas(self.screen)

    def run(self):
        self.canvas.start()

        while self.is_running:
            self.system_input()
            self.screen.fill(self.fill_color)
            self.canvas.update()
            pygame.display.flip()
                            
        pygame.quit()
        sys.exit()
    
    def system_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.is_running = False

    def set_fill_color(self, fill_color):
        self.fill_color = fill_color