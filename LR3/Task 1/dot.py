import numpy as np

from kernel.entity import Entity
from kernel.renderers.circleRenderer import CircleRenderer
from lable import Label


class Dot(Entity):

    def __init__(self, entitys, screen, position, radius = 2, color = (0,0,0), labled = True):
        super().__init__(entitys, position)
        self.screen = screen
        self.entitys = entitys
        self.local_position = position
        
        circle_renderer = CircleRenderer(screen, color, radius)
        self.set_renderer(circle_renderer)

        label_pos = [p + 5 for p in position]
        self.pos_label = Label(self.subentitys, self.screen, label_pos, str(np.round(position,2)), 20, color)
        self.pos_label.is_visable = labled
    
    def set_position(self, position):
        self.local_position = position
    
    def set_text(self, text):
        self.pos_label.renderer.set_text(str(text))
    
