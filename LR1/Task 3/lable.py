from kernel.entity import Entity
from renderers.textRenderer import TextRenderer

class Label(Entity):

    def __init__(self, entitys, screen, position, text, size, color = (0,0,0)):
        super().__init__(entitys, position)
        self.set_renderer(TextRenderer(screen, color, text, size))