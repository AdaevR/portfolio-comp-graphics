import numpy as np

from kernel.canvas import Canvas
from cartesianCoordsView import CartesianCoordsView
from inputBox import InputBox
from kernel.entity import Entity
from lable import Label
from renderers.circleRenderer import CircleRenderer

class MyCanvas(Canvas):
    def start(self):
        self.pix_per_unit = 50
        self.coords_origin = (100,100)
        coords_view = CartesianCoordsView(self.entitys, self.screen, self.coords_origin)
        coords_view.setup((50,50,50), (150,150,150), self.pix_per_unit, (22,9))

        label_x = Label(self.entitys, self.screen, [50, 650], "Enter X: ", 30)
        label_y = Label(self.entitys, self.screen, [50, 600], "Enter Y: ", 30)
        self.label_error = Label(self.entitys, self.screen, [250, 630], "Error", 30, (200,0,0))
        self.label_error.is_visable = False

        input_box_x = InputBox(self.entitys, self.screen, (150,650),(80,30), "0")
        input_box_x.on_value_change = self.set_input_vec_x
        input_box_y = InputBox(self.entitys, self.screen, (150,600),(80,30), "0")
        input_box_y.on_value_change = self.set_input_vec_y
        
        self.input_vec = [0,0]
        self.create_dots(self.input_vec, self.calc_task())


    def update(self):
        super().update()
    
    def set_input_vec_x(self, value):
        try:
            self.input_vec[0] = float(value)
        except ValueError:
            self.label_error.is_visable = True
        else:
            self.label_error.is_visable = False
            out = self.calc_task()
            self.set_dots(self.input_vec, out)
    
    def set_input_vec_y(self, value):
        try:
            self.input_vec[1] = float(value)
        except ValueError:
            self.label_error.is_visable = True
        else:
            self.label_error.is_visable = False
            out = self.calc_task()
            self.set_dots(self.input_vec, out)

    def calc_task(self):

        user_input = np.array(self.input_vec)
        transform = np.array([[1, 3], [4, 1]])
        output = np.matmul(user_input, transform)

        print("User input", user_input)
        print("Transform", transform)
        print("Output", output)

        return output
    
    def create_dots(self, user_input, output):
        user_input = np.array(user_input)

        user_input_pos = user_input * self.pix_per_unit + self.coords_origin 
        user_output_pos = output * self.pix_per_unit + self.coords_origin

        self.label_input_dot = Label(self.entitys, self.screen, user_input_pos + 5, np.array2string(user_input), 20)
        self.label_otput_dot = Label(self.entitys, self.screen, user_output_pos + 5, np.array2string(output), 20)

        circleRendererIn = CircleRenderer(self.screen, (100,0,0),5)
        self.input_circle = Entity(self.entitys, user_input_pos)
        self.input_circle.set_renderer(circleRendererIn)

        circleRendererOut = CircleRenderer(self.screen, (200,0,0),5)
        self.output_circle = Entity(self.entitys, user_input_pos)
        self.output_circle.set_renderer(circleRendererOut)


    def set_dots(self, user_input, output):
        user_input = np.array(user_input)

        user_input_pos = user_input * self.pix_per_unit + self.coords_origin 
        user_output_pos = output * self.pix_per_unit + self.coords_origin
        
        self.label_input_dot.position = user_input_pos + 5
        self.label_otput_dot.position = user_output_pos + 5
        self.label_input_dot.renderer.set_text(np.array2string(user_input))
        self.label_otput_dot.renderer.set_text(np.array2string(output))

        self.input_circle.position = user_input_pos
        self.output_circle.position = user_output_pos
