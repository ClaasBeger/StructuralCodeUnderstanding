import math

class Circle:
    def __init__(self, radius=1.0, color="red"):
        self._radius = radius
        self._color = color

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def get_area(self):
        return self._radius * self._radius * math.pi

    def __str__(self):
        return f"Circle[radius={self._radius}, color={self._color}]"


class Cylinder(Circle):
    def __init__(self, radius=1.0, height=1.0, color="red"):
        super().__init__(radius, color)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def get_volume(self):
        return self.get_area() * self._height

    def __str__(self):
        return f"Cylinder: subclass of {super().__str__()} height={self._height}"



if __name__ == "__main__":
    circle2 = Circle(3.0, "green")
    circle2.radius = 6.0
    print(circle2)
    print(f"Area of circle2: {circle2.get_area()}")
    c2 = Cylinder(7.0, 2.0)
    print(f"Cylinder: radius={c2.radius} height={c2.height} base area={c2.get_area()} volume={c2.get_volume()}")