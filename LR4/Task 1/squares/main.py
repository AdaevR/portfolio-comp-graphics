import sys
import math as m
import pygame
import numpy as np
from pygame.locals import *
import graphics as g
import transform as t

def main():
    O = g.Origin(30, 30)
    UX = g.Unit(60)
    UY = g.Unit(60)
    rframe = g.ReferenceFrame(O, UX, UY)

    drawer = g.Drawer(800, 600, rframe)
    drawer.initialize("Lab3")
    drawer.font = "freesanbold.ttf"

    square_data = np.array([
        [ 2, 0.5, 1],
        [ 8, 0.5, 1],
        [ 8, 6.5, 1],
        [ 2, 6.5, 1],
    ])

    FPS = 30
    clock = pygame.time.Clock()
    while True:
        drawer.screen.fill((255,255,255))

        drawer.color = (0, 0, 0)
        drawer.draw_axes(rframe, -1.0, 15.0, -1.0, 10.0)
        drawer.color = (50, 150, 50)
        drawer.draw_polygon(rframe,square_data,2)
        new_square_data = square_data
        for i in range(50):
            x_center = sum([p[0] for p in square_data])/4
            y_center = sum([p[1] for p in square_data])/4
            new_square_data = np.matmul(new_square_data, t.translate(-x_center, -y_center))
            new_square_data = np.matmul(new_square_data, t.scale(0.95,0.95))
            new_square_data = np.matmul(new_square_data, t.rotate(m.pi/64))
            new_square_data = np.matmul(new_square_data, t.translate(x_center, y_center))
            drawer.draw_polygon(rframe,new_square_data,2)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)
        pygame.display.update()

if __name__=="__main__":
    main()