import math
import random
import numpy as np
import pygame

from kernel.canvas import Canvas
from kernel.utility import to_pygame
from entities.cartesianCoordsView import CartesianCoordsView
from entities.lable import Label
from entities.lineSegment import LineSegment

class MyCanvas(Canvas):
    def __init__(self, screen):
        super().__init__(screen)
        self.is_mouse_down = False
        self.mouse_move_speed = 1
        self.pix_per_unit = 50 # <= 50
        self.coords_origin = (100,100)

    def start(self):
        self.coords_view = CartesianCoordsView(self.root, self.coords_origin)
        self.coords_view.setup((100,100,100), (190,190,190), self.pix_per_unit, (60,40), int(50/self.pix_per_unit))

        self.lines = []
        for i in np.arange(0, 10, 0.1):
            r = 1.5 + 2 * 3 * math.cos(i)
            self.lines.append([r*math.cos(i),r*math.sin(i)])
        print(self.lines)
    
    def render(self):
        super().render()
        lines = [to_pygame(np.array(p)*self.pix_per_unit+self.coords_view.local_position, self.screen.get_size()[1]) for p in self.lines]
        pygame.draw.lines(self.screen, (255, 0, 0), False, np.array(lines), width=3)

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.is_mouse_down = True
            self.pressed_origin = event.pos
            self.coords_pos_origin = self.coords_view.local_position
            
        if event.type == pygame.MOUSEMOTION and self.is_mouse_down:
            mouse_shift = [pos - origin for (origin, pos) in zip(self.pressed_origin, event.pos)]
            mouse_shift[1] = mouse_shift[1]*-1
            self.coords_view.local_position = [origin + shift * self.mouse_move_speed for (origin, shift) in zip(self.coords_pos_origin, mouse_shift)]
            
        if event.type == pygame.MOUSEBUTTONUP:
            self.is_mouse_down = False
    