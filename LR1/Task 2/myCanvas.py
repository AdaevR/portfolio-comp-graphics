from cernel.canvas import Canvas
from cernel.entity import Entity
from renderers.circleRenderer import CircleRenderer
from renderers.lineRenderer import LineRenderer
from renderers.textRenderer import TextRenderer

class MyCanvas(Canvas):
    def start(self):
        circleRenderer = CircleRenderer(self.screen, (150,0,0), 20)
        circle = Entity(self.entitys, [100, 50], circleRenderer)

        lineRenderer = LineRenderer(self.screen, (0,0,200), (100,0), (200,100), 10)
        line = Entity(self.entitys, [0, 0], lineRenderer)

        textRenderer = TextRenderer(self.screen, (0,150,0), "Bla bla bla", 50)
        text = Entity(self.entitys, [100, 50], textRenderer)


    def update(self):
        super().update()