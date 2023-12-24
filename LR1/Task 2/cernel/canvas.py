class Canvas:
    screen = None
    entitys = []

    def __init__(self, screen):
        self.screen = screen

    def start(self):
        pass

    def update(self):
        self.input_update()
        self.logic_update()
        self.render_update()
    
    def input_update(self):        
        for entity in self.entitys:
            entity.input_update()
    
    def logic_update(self):
        for entity in self.entitys:
            entity.logic_update()

    def render_update(self):
        for entity in self.entitys:
            entity.render_update()

