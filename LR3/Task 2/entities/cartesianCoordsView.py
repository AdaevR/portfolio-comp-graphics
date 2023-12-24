from entities.lable import Label
from kernel.entity import Entity
from renderers.lineRenderer import LineRenderer

class CartesianCoordsView(Entity):

    def __init__(self, parent, position):
        super().__init__(parent, position)
        self.pix_to_unit = None
        self.size = None
        self.mesureStep = 1

    def setup(self, color, grid_color, pix_per_unit, size, mesureStep = 1):
        self.pix_to_unit = pix_per_unit
        self.size = size
        self.mesureStep = mesureStep
        self.sizeInPix = (self.size[0] * self.pix_to_unit, self.size[1] * self.pix_to_unit)

        self.create_grid(grid_color, 1)
        self.create_axis(color, 3)
        self.create_mesure_points(color, 3)

    def create_grid(self, color, width):
        for ix in range(-self.size[0], self.size[0],self.mesureStep):
            mesureLineRenderer = LineRenderer(
                self.screen,
                color, 
                (ix * self.pix_to_unit, -self.sizeInPix[1]), 
                (ix * self.pix_to_unit, self.sizeInPix[1]), 
                width
            )
            mesure = Entity(self, [0,0])
            mesure.set_renderer(mesureLineRenderer)
        
        for iy in range(-self.size[1], self.size[1],self.mesureStep):
            mesureLineRenderer = LineRenderer(
                self.screen,
                color, 
                (-self.sizeInPix[0], iy * self.pix_to_unit), 
                (self.sizeInPix[0], iy * self.pix_to_unit), 
                width
            )
            mesure = Entity(self, [0,0])
            mesure.set_renderer(mesureLineRenderer)

    def create_axis(self, color, width):
        lineRendererY = LineRenderer(
            self.screen,
            color, 
            (0, -self.sizeInPix[1]), 
            (0, self.sizeInPix[1]), 
            width
        )
        self.lineY = Entity(self, [0,0])
        self.lineY.set_renderer(lineRendererY)

        lineRendererX = LineRenderer(
            self.screen,
            color, 
            (-self.sizeInPix[0], 0), 
            (self.sizeInPix[0], 0), 
            width
        )
        lineX = Entity(self, [0,0])
        lineX.set_renderer(lineRendererX)

    def create_mesure_points(self, color, width):
        
        for ix in range(-self.size[0], self.size[0],self.mesureStep):
            mesureLineRenderer = LineRenderer(
                self.screen,
                color, 
                (ix * self.pix_to_unit, -5), 
                (ix * self.pix_to_unit, 5), 
                width
            )
            mesure = Entity(self, [0,0])
            mesure.set_renderer(mesureLineRenderer)

            labelPos = [ix * self.pix_to_unit + 5, - 20]
            label = Label(self, labelPos, str(ix), 20, color)
        
        for iy in range(-self.size[1], self.size[1],self.mesureStep):
            mesureLineRenderer = LineRenderer(
                self.screen,
                color, 
                (-5, iy * self.pix_to_unit), 
                (5, iy * self.pix_to_unit), 
                width
            )
            mesure = Entity(self, [0,0])
            mesure.set_renderer(mesureLineRenderer)

            labelPos = [-20, iy * self.pix_to_unit]
            label = Label(self, labelPos, str(iy), 20, color)
