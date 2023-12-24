import pygame

class LineRenderer:
    screen = None
    color = (0,0,0)
    start_pos = (0,0)
    end_pos = (0,0)
    width = 1

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
        pygame.draw.line(
            self.screen,
            self.color,
            start_pos,
            end_pos,
            self.width
        )