class Entity:
    def __init__(self, entitys, position):
        self.local_position = position
        self.world_position = position
        self.is_visable = True
        self.renderer = None
        self.subentitys = []
        entitys.append(self)
    
    def handle_event(self, event):
        for entity in self.subentitys:
            entity.handle_event(event)
    
    def update(self):
        for entity in self.subentitys:
            subentity_world_position = [sum(x) for x in zip(entity.local_position, self.world_position)]
            entity.world_position = subentity_world_position
            entity.update()

    def render(self):
        for entity in self.subentitys:
            entity.render()
        
        if self.renderer is not None and self.is_visable:
            self.renderer.render(self.world_position)

    def add_subentity(self, subentity):
        self.subentitys.append(subentity)
        
    def set_renderer(self, renderer):
        self.renderer = renderer
