from lable import Label
from kernel.entity import Entity
from renderers.lineRenderer import LineRenderer
from renderers.textRenderer import TextRenderer

class CartesianCoordsView(Entity):

    def __init__(self, entitys, screen, position):
        super().__init__(entitys, position)
        self.screen = screen
        self.pix_to_unit = None
        self.size = None

    def setup(self, color, grid_color, pix_per_unit, size):
        self.pix_to_unit = pix_per_unit
        self.size = size
        self.sizeInPix = (self.size[0] * self.pix_to_unit, self.size[1] * self.pix_to_unit)

        self.create_grid(grid_color, 1)
        self.create_axis(color, 3)
        self.create_mesure_points(color, 3)


    def create_grid(self, color, width):
        for ix in range(-self.size[0], self.size[0]):
            mesureLineRenderer = LineRenderer(
                self.screen,
                color, 
                (ix * self.pix_to_unit, -self.sizeInPix[1]), 
                (ix * self.pix_to_unit, self.sizeInPix[1]), 
                width
            )
            mesure = Entity(self.subentitys, self.position)
            mesure.set_renderer(mesureLineRenderer)
        
        for iy in range(-self.size[1], self.size[1]):
            mesureLineRenderer = LineRenderer(
                self.screen,
                color, 
                (-self.sizeInPix[0], iy * self.pix_to_unit), 
                (self.sizeInPix[0], iy * self.pix_to_unit), 
                width
            )
            mesure = Entity(self.subentitys, self.position)
            mesure.set_renderer(mesureLineRenderer)

    def create_axis(self, color, width):
        lineRendererY = LineRenderer(
            self.screen,
            color, 
            (0, -self.sizeInPix[1]), 
            (0, self.sizeInPix[1]), 
            width
        )
        lineY = Entity(self.subentitys, self.position)
        lineY.set_renderer(lineRendererY)

        lineRendererX = LineRenderer(
            self.screen,
            color, 
            (-self.sizeInPix[0], 0), 
            (self.sizeInPix[0], 0), 
            width
        )
        lineX = Entity(self.subentitys, self.position)
        lineX.set_renderer(lineRendererX)

    def create_mesure_points(self, color, width):
        
        for ix in range(-self.size[0], self.size[0]):
            mesureLineRenderer = LineRenderer(
                self.screen,
                color, 
                (ix * self.pix_to_unit, -5), 
                (ix * self.pix_to_unit, 5), 
                width
            )
            mesure = Entity(self.subentitys, self.position)
            mesure.set_renderer(mesureLineRenderer)

            labelPos = [ix * self.pix_to_unit + self.position[0]+5, self.position[1] - 20]
            label = Label(self.subentitys, self.screen, labelPos, str(ix), 20, color)
        
        for iy in range(-self.size[1], self.size[1]):
            mesureLineRenderer = LineRenderer(
                self.screen,
                color, 
                (-5, iy * self.pix_to_unit), 
                (5, iy * self.pix_to_unit), 
                width
            )
            mesure = Entity(self.subentitys, self.position)
            mesure.set_renderer(mesureLineRenderer)

            labelPos = [self.position[0] - 20, iy * self.pix_to_unit + self.position[1]]
            label = Label(self.subentitys, self.screen, labelPos, str(iy), 20, color)
