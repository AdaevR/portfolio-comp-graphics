import numpy as np

from kernel.entity import Entity
from kernel.renderers.lineRenderer import LineRenderer
from dot import Dot


class LineSegment(Entity):

    def __init__(self, entitys, screen, position, pix_per_unit, line_start, line_end, color = (0,0,0), labled = True):
        super().__init__(entitys, position)
        self.screen = screen
        self.entitys = entitys
        self.position = position
        self.pix_per_unit = pix_per_unit
        self.line_start = line_start
        self.line_end = line_end
        
        line_renderer = LineRenderer(self.screen, color, [0,0], [0,0], 2)
        self.set_renderer(line_renderer)

        self.start_dot = Dot(self.subentitys, screen, [0,0], 2, color, labled)
        self.end_dot = Dot(self.subentitys, screen, [0,0], 2, color, labled)

        self.set_line_pos(line_start, line_end)


    def update(self):
        super().update()
    
    def set_line_pos(self, line_start, line_end):
        self.line_start = line_start
        self.line_end = line_end

        screen_line_start = [p * self.pix_per_unit for p in line_start]
        screen_line_end = [p * self.pix_per_unit for p in line_end]

        self.renderer.start_pos = screen_line_start
        self.renderer.end_pos = screen_line_end

        self.start_dot.set_position(screen_line_start)
        self.start_dot.set_text(np.round(line_start,2))
        self.end_dot.set_position(screen_line_end)
        self.end_dot.set_text(np.round(line_end,2))
