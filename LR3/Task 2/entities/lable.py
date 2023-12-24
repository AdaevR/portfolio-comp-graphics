from kernel.entity import Entity
from renderers.textRenderer import TextRenderer

class Label(Entity):

    def __init__(self, parent, position, text, size, color = (0,0,0)):
        super().__init__(parent, position)
        self.set_renderer(TextRenderer(self.screen, color, text, size))