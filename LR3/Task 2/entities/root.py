from kernel.entity import Entity

class Root(Entity):

    def __init__(self, screen):
        self.local_position = [0,0]
        self.world_position = [0,0]

        self.local_rotation = 0
        self.local_scale = (1, 1)
        
        self.is_visable = False
        self.subentitys = []
        self.screen = screen

    def get_world_position(self):
        return self.local_position

    def get_world_scale(self):
        return self.local_scale

    def get_transformed_position(self):
        return self.local_position
