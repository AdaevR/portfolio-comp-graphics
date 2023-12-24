class Entity:
    def __init__(self, entitys, position):
        self.position = position
        self.is_visable = True
        self.renderer = None
        self.subentitys = []
        entitys.append(self)
    
    def handle_event(self, event):
        for entity in self.subentitys:
            entity.handle_event(event)
    
    def update(self):
        for entity in self.subentitys:
            entity.update()

    def render(self):
        for entity in self.subentitys:
            entity.render()
        
        if self.renderer is not None and self.is_visable:
            self.renderer.render(self.position)

    def add_subentity(self, subentity):
        self.subentitys.append(subentity)
        
    def set_renderer(self, renderer):
        self.renderer = renderer
