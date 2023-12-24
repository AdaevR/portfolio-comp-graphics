import pygame

class CircleRenderer:
    screen = None
    color = (0,0,0)
    radius = 1

    def __init__(self, screen, color, radius):
        self.screen = screen
        self.color = color
        self.radius = radius

    def render(self, position):
        pygame.draw.circle(
            self.screen,
            self.color,
            position,
            self.radius,
        )