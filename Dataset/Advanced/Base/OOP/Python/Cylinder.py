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


class TestCylinder:
    @staticmethod
    def main():
        c1 = Cylinder()
        print(f"Cylinder: radius={c1.radius} height={c1.height} base area={c1.get_area()} volume={c1.get_volume()}")

        c2 = Cylinder(10.0)
        print(f"Cylinder: radius={c2.radius} height={c2.height} base area={c2.get_area()} volume={c2.get_volume()}")

        c3 = Cylinder(2.0, 10.0)
        print(f"Cylinder: radius={c3.radius} height={c3.height} base area={c3.get_area()} volume={c3.get_volume()}")


if __name__ == "__main__":
    TestCylinder.main()