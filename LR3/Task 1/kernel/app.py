import sys, pygame
from myCanvas import MyCanvas

class App:
    def __init__(self):
        self.is_running = True
        self.screen = None
        self.canvas = None

    def init(self, name, screen_size):
        pygame.init()
        pygame.display.set_caption(name)
        self.screen = pygame.display.set_mode(screen_size)
        self.canvas = MyCanvas(self.screen)


    def run(self):
        self.canvas.start()
        clock = pygame.time.Clock()

        while self.is_running:
            self.handle_event()
            self.canvas.update()
            self.canvas.render()
            clock.tick(30)
            pygame.display.flip()
                            
        pygame.quit()
        sys.exit()
    
    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.is_running = False
            self.canvas.handle_event(event)