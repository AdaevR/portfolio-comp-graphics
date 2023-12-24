import pygame
from kernel.utility import to_pygame

class CircleRenderer:
    def __init__(self, screen, color, radius):
        self.screen = screen
        self.color = color
        self.radius = radius

    def render(self, position):
        position = to_pygame(position, self.screen.get_size()[1])
        pygame.draw.circle(
            self.screen,
            self.color,
            position,
            self.radius,
        )