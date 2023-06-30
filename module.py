"""The x,y for Rectangle and Square refer to the
top left-hand corner of the shape."""
import numpy as np
from PIL import Image

class Canvas:
    """Create a canvas to draw rectangles or squares on.
    width and height need to be integers and color needs
    to be a list object containing three values corresponding to
    'RGB'."""
    images_made = 0
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Automatically create 3d nupy array
        self.data = np.zeros((self.height,
                               self.width, 3), dtype=np.uint8)
        # Replace every 3 values of the first dimension
        # with the color you want.

        self.data[:] = self.color

    def make(self,image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
        Canvas.images_made += 1

class Square:

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x+self.side, self.y: self.y+self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x+self.height, self.y: self.y+self.width] = self.color

"""Shape information"""
class Canvas_Info:
    def __init__(self):
        self.width = int(input("What width for the canvas?: "))
        self.height = int(input("What height for the canvas?: "))
        self.R, self.G, self.B = int(input("Red intensity: ")), int(input("Green intensity: ")), \
            int(input("Blue intensity: "))

class Square_Info:
    def __init__(self):
        self.x = int(input("Square point x: "))
        self.y = int(input("Square point y: "))
        self.side = int(input("Square side length: "))
        self.R, self.G, self.B = int(input("Square red intensity: ")), int(input("Square green intensity: ")), \
            int(input("Square blue intensity: "))

class Rectangle_Info:
    def __init__(self):
        self.x = int(input("Rectangle point x: "))
        self.y = int(input("Rectangle point y: "))
        self.width = int(input("Rectangle width: "))
        self.height = int(input("Rectangle height: "))
        self.R, self.G, self.B = int(input("Rectangle red intensity: ")), int(input("Rectangle green intensity: ")), \
            int(input("Rectangle blue intensity: "))

