import pygame
from kernel.utility import to_pygame

class LineRenderer:
    def __init__(self, screen, color, start_pos, end_pos, width):
        self.screen = screen
        self.color = color
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width

    def render(self, position):
        start_pos = (
            self.start_pos[0] + position[0],
            self.start_pos[1] + position[1],
        )
        end_pos = (
            self.end_pos[0] + position[0],
            self.end_pos[1] + position[1],
        )
        start_pos = to_pygame(start_pos, self.screen.get_size()[1])
        end_pos = to_pygame(end_pos, self.screen.get_size()[1])

        pygame.draw.line(
            self.screen,
            self.color,
            start_pos,
            end_pos,
            self.width
        )