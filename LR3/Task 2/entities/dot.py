import numpy as np

from kernel.entity import Entity
from renderers.circleRenderer import CircleRenderer
from entities.lable import Label


class Dot(Entity):

    def __init__(self, parent, position, radius = 2, color = (0,0,0)):
        super().__init__(parent, position)
        self.local_position = position
        
        circle_renderer = CircleRenderer(self.screen, color, radius)
        self.set_renderer(circle_renderer)

        label_pos = [p + 5 for p in position]
        self.pos_label = Label(self, label_pos, str(np.round(position,2)), 20, color)
    
    def set_position(self, position):
        self.local_position = position
    
    def set_text(self, text):
        self.pos_label.renderer.set_text(str(text))
    
