import pygame
from kernel.entity import Entity
from kernel.utility import to_pygame
from renderers.rectRenderer import RectRenderer
from renderers.textRenderer import TextRenderer

class InputBox(Entity):

    def __init__(self, entitys, screen, position, size, text=''):
        super().__init__(entitys, position)
        self.screen = screen
        self.active = False
        self.color_inactive = (220,220,220)
        self.color_active = (190,190,220)
        self.color = self.color_inactive
        self.minSize = size
        self.rect = pygame.Rect(position, size)
        self.text = text
        self.textPadding = (size[1]/8, size[1]/8)
        self.on_value_change = None

        rectRenderer = RectRenderer(screen, self.color_inactive, self.rect.size, int(size[1]/15), int(size[1]/5))
        self.rectEntity = Entity(self.subentitys, position)
        self.rectEntity.set_renderer(rectRenderer)

        textRenderer = TextRenderer(screen, (0,0,0), text, self.rect.size[1])
        self.textEntity = Entity(
            self.subentitys, 
            (position[0]+self.textPadding[0], position[1]+self.textPadding[1])
        )
        self.textEntity.set_renderer(textRenderer)

        self.recalc_props()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(to_pygame(event.pos, self.screen.get_size()[1])):
                self.active = True
            else:
                self.active = False

            self.color = self.color_active if self.active else self.color_inactive
            self.rectEntity.renderer.color = self.color
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.textEntity.renderer.set_text(self.text)
                self.recalc_props()
                if self.on_value_change is not None: self.on_value_change(self.text)
    
    def recalc_props(self):
        (self.rect.x, self.rect.y) = self.position
        self.textPadding = (self.rect.size[1]/8, self.rect.size[1]/8)
        width = max(self.minSize[0], self.textEntity.renderer.lable.get_width() + self.textPadding[1]*2)
        self.rect.w = width
        self.rectEntity.renderer.size = self.rect.size


