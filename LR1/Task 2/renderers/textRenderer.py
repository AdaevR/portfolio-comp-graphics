import pygame

class TextRenderer:
    screen = None
    color = (0,0,0)
    font = None
    text = ""
    size = 1

    def __init__(self, screen, color, text, size):
        self.screen = screen
        self.color = color
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('freesanbold.ttf', size)

    def render(self, position):
        lable = self.font.render((self.text), True, self.color)
        self.screen.blit(lable, position )
    
