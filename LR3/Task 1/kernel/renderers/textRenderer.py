import pygame
from kernel.utility import to_pygame

class TextRenderer:

    def __init__(self, screen, color, text, size):
        self.screen = screen
        self.color = color
        self.size = size
        self.text = text
        self.font = pygame.font.SysFont('freesanbold.ttf', size)
        self.lable = self.font.render((self.text), True, self.color)

    def render(self, position):
        
        lableRect = self.lable.get_rect()
        position = to_pygame(position, self.screen.get_size()[1], lableRect.height)
        
        self.screen.blit(self.lable, position )
    
    def set_text(self, text):
        self.text = text
        self.lable = self.font.render((self.text), True, self.color)
