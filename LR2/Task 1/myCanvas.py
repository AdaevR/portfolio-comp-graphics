import numpy as np
import pygame

from kernel.canvas import Canvas
from cartesianCoordsView import CartesianCoordsView
from lineSegment import LineSegment

class MyCanvas(Canvas):
    def __init__(self, screen):
        super().__init__(screen)
        self.is_mouse_down = False
        self.mouse_move_speed = 1
        self.pix_per_unit = 0.5 # <= 50
        self.coords_origin = (100,100)

    def start(self):
        self.coords_view = CartesianCoordsView(self.entitys, self.screen, self.coords_origin)
        self.coords_view.setup((50,50,50), (150,150,150), self.pix_per_unit, (3000,2000), int(50/self.pix_per_unit))

        line_data = np.array([[0, 100], [200, 300]])
        transform = np.array([[1, 2], [3, 1]])
        result_line_data = np.matmul(line_data, transform)
        
        line_center = np.array([(end + start)/2 for (start, end) in zip(line_data[0], line_data[1])])
        result_line_center = np.matmul(line_center, transform)

        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, line_data[0], line_data[1], (80,80,80))
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, result_line_data[0], result_line_data[1])
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, line_center, result_line_center, (100,200,100))

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
