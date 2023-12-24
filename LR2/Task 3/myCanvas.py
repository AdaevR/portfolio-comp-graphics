import numpy as np
import pygame

from kernel.canvas import Canvas
from cartesianCoordsView import CartesianCoordsView
from lable import Label
from lineSegment import LineSegment

class MyCanvas(Canvas):
    def __init__(self, screen):
        super().__init__(screen)
        self.is_mouse_down = False
        self.mouse_move_speed = 1
        self.pix_per_unit = 30 # <= 50
        self.coords_origin = (100,100)

    def start(self):
        self.coords_view = CartesianCoordsView(self.entitys, self.screen, self.coords_origin)
        self.coords_view.setup((100,100,100), (190,190,190), self.pix_per_unit, (60,20), int(50/self.pix_per_unit))

        line_data = np.array([[-1/2, 3/2], [3, -2], [-1, -1], [3, 5/3]])
        transform = np.array([[1, 2], [1, -3]])
        result_line_data = np.matmul(line_data, transform)
        
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, line_data[0], line_data[1], (80,100,80))
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, line_data[2], line_data[3], (80,100,80))
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, result_line_data[0], result_line_data[1],(100,150,100))
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, result_line_data[2], result_line_data[3],(100,150,100))
        
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