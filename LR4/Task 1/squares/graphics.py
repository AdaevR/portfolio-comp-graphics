import numpy as np
import pygame


class Origin:
    def __init__(self, x0: float, y0: float) -> None:
        self.x0 = x0
        self.y0 = y0

class Unit:
    def __init__(self, pixels: int) -> None:
        self.pixels = pixels

class ReferenceFrame:
    def __init__(self, O: Origin, UX: Unit, UY: Unit) -> None:
        self.O = O
        self.UX = UX
        self.UY = UY

class Drawer:
    def __init__(self, res_x: int, res_y: int, rf: ReferenceFrame):
        self.screen_size = (res_x, res_y)
    
    def initialize(self, caption: str):
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(self.screen_size)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: tuple):
        self.__color = color
    
    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, name: str):
        self.__font = pygame.font.SysFont(name, 25)
    
    def draw_text(self, rframe: ReferenceFrame, x: float, y: float, text: str):
        lable = self.font.render(text, True, self.color)
        x = self.get_X(rframe, x)
        y = self.get_Y(rframe, y)
        self.screen.blit(lable, (x,y))

    def draw_line(self, rframe: ReferenceFrame, x1: float, y1: float, x2: float, y2: float, width: int):
        x1 = self.get_X(rframe, x1)
        y1 = self.get_Y(rframe, y1)
        
        x2 = self.get_X(rframe, x2)
        y2 = self.get_Y(rframe, y2)
        pygame.draw.line(
            self.screen,
            self.color,
            (x1,y1),
            (x2,y2),
            width
        )

    def draw_polygon(self, rframe: ReferenceFrame, points: np.array, width: int):
        points = [(self.get_X(rframe, p[0]), self.get_Y(rframe, p[1])) for p in points]
        pygame.draw.polygon(self.screen, self.color, points, width)

    def draw_axes(self, rframe: ReferenceFrame, x_min: float, x_max: float, y_min: float, y_max: float):
        self.draw_line(rframe, x_min, 0.0, x_max, 0.0, 1)
        self.draw_line(rframe, 0.0, y_min, 0.0, y_max, 1)
        self.draw_text(rframe, 0.0, 0.0, "O")

    def get_X(self, rframe: ReferenceFrame, x: float):
        scale_x = rframe.UX.pixels
        x0 = rframe.O.x0
        raw_x = int(scale_x * x + x0)
        return raw_x
    
    def get_Y(self, rframe: ReferenceFrame, y: float):
        scale_y = rframe.UY.pixels
        y0 = rframe.O.y0
        raw_y = int(scale_y * y + y0)
        return self.to_pygame(raw_y, self.screen.get_size()[1])
    
    def get_length(unit: Unit, dl: float):
        return int(dl * unit.pixels)
    
    def to_pygame(self, y, height, obj_height = 0):
        return  height - y - obj_height