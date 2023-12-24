import math
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
        self.pix_per_unit = 50 # <= 50
        self.coords_origin = (100,100)

    def start(self):
        self.coords_view = CartesianCoordsView(self.entitys, self.screen, self.coords_origin)
        self.coords_view.setup((100,100,100), (190,190,190), self.pix_per_unit, (60,40), int(50/self.pix_per_unit))

        m = 0.9
        alpha = math.pi/32
        square_data = np.array([[2, 2], [-2, 2], [-2, -2], [2, -2]])
        scale_trans = np.array([[m, 0], [0, m]])
        rotation_trans = np.array([[math.cos(alpha), -math.sin(alpha)], [math.sin(alpha), math.cos(alpha)]])

        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, square_data[0], square_data[1], (80,100,80))
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, square_data[1], square_data[2], (80,100,80))
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, square_data[2], square_data[3], (80,100,80))
        LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, square_data[3], square_data[0], (80,100,80))

        result_square_data = square_data
        transform = np.matmul(rotation_trans,scale_trans)
        for i in range(20):
            result_square_data = np.transpose(np.matmul(transform, np.transpose(result_square_data)))
            LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, result_square_data[0], result_square_data[1],(100,150,100), labled=False)
            LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, result_square_data[1], result_square_data[2],(100,150,100), labled=False)
            LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, result_square_data[2], result_square_data[3],(100,150,100), labled=False)
            LineSegment(self.coords_view.subentitys, self.screen, [0,0], self.pix_per_unit, result_square_data[3], result_square_data[0],(100,150,100), labled=False)
            
    
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