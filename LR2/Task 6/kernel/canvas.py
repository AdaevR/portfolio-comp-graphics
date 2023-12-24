class Canvas:
    def __init__(self, screen):
        self.screen = screen
        self.fill_color = (255, 255, 255)
        self.entitys = []

    def start(self):
        pass
    
    def handle_event(self, event):        
        for entity in self.entitys:
            entity.handle_event(event)
    
    def update(self):
        for entity in self.entitys:
            entity.world_position = entity.local_position
            entity.update()

    def render(self):
        self.screen.fill(self.fill_color)
        for entity in self.entitys:
            entity.render()

    def remove_entity(self, entity):
        self.entitys.remove(entity)
