import math
import numpy as np


class Entity:
    def __init__(self, parent, position):
        self.parent = parent

        self.local_position = position

        self.local_rotation = 0
        self.local_scale = (1, 1)
        
        self.is_visable = True
        self.renderer = None
        self.subentitys = []
        self.screen = None
        parent.add_entity(self)
    
    def handle_event(self, event):
        for entity in self.subentitys:
            entity.handle_event(event)
    
    def update(self):
        for entity in self.subentitys:
            entity.update()

    def render(self):
        if self.renderer is not None and self.is_visable:
            self.renderer.render(self.get_transformed_position())
            
        for entity in self.subentitys:
            entity.render()
    
    def get_world_position(self):
        return np.array(self.local_position) + self.parent.get_transformed_position()

    def get_world_scale(self):
        scale_transform = np.array([[self.local_scale[0], 0], [0, self.local_scale[1]]])
        return np.matmul(scale_transform, self.parent.get_world_scale())

    def get_transformed_position(self):
        transform = np.matmul(
                np.array([[self.local_scale[0], 0], [0, self.local_scale[1]]]),
                np.array(
                    [[math.cos(self.local_rotation), -math.sin(self.local_rotation)], 
                    [math.sin(self.local_rotation), math.cos(self.local_rotation)]]))
        without_translation = np.array(self.get_world_position()) - self.local_position
        transformed = np.transpose(np.matmul(transform, np.transpose(without_translation)))
        return transformed + self.local_position

    def add_entity(self, subentity):
        subentity.screen = self.screen
        self.subentitys.append(subentity)
        
    def set_renderer(self, renderer):
        self.renderer = renderer

    def set_scale(self, x, y):
        self.local_scale = (x,y)
    
    def set_rotation(self, alpha):
        self.local_rotation = alpha
