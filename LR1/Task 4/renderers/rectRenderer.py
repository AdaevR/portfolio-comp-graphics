import pygame
from kernel.utility import to_pygame

class RectRenderer:
    def __init__(self, screen, color, size, border_size = 0, border_radius = 0):
        self.screen = screen
        self.color = color
        self.size = size
        self.border_size = border_size
        self.border_radius = border_radius

    def render(self, position):
        position = to_pygame(position, self.screen.get_size()[1], self.size[1])
        pygame.draw.rect(
            self.screen,
            self.color,
            pygame.Rect(position, self.size),
            self.border_size,
            self.border_radius
        )