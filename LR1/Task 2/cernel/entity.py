class Entity:
    position = [0,0]
    renderer = None

    def __init__(self, entitys, position, renderer):
        self.position = position
        self.renderer = renderer
        entitys.append(self)
    
    def input_update(self):
        pass
    
    def logic_update(self):
        pass

    def render_update(self):
        self.renderer.render(self.position)
    

    def set_renderer(self, renderer):
        self.renderer = renderer
