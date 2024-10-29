#!/usr/bin/env python3
from math import pi

debug_flag = False
def d_print(s):
    if (debug_flag):
        print(s)


class Shape:
    """Геометрические фигуры"""
    name = 'геометрическая фигура'

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"{self.name} по координатам ({self.__x}, {self.__y})"


class Rectangle(Shape):
    """Прямоугольники"""
    name = 'прямоугольник'

    @property
    def width(self):
        d_print("Rectangle.width_getter")
        return self._width

    @property
    def height(self):
        d_print("Rectangle.height_getter")
        return self._height

    @height.setter
    def height(self, x):
        d_print("Rectangle.height_setter")
        self._height = x

    @width.setter
    def width(self, x):
        d_print("Rectangle.width_setter")
        self._width = x

    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, со сторонами {self.width} и {self.height},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")


class Square(Rectangle):
    """Квадраты"""
    name = 'квадрат'

    @property
    def width(self):
        d_print("Square.width_getter")
        return self._side

    @property
    def height(self):
        d_print("Square.height_getter")
        return self._side

    @height.setter
    def height(self, x):
        d_print("Square.height_setter")
        self._side = x

    @width.setter
    def width(self, x):
        d_print("Square.width_setter")
        self._side = x

    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, со стороной {self.width},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")


class Circle(Shape):
    name = 'круг'

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.r = radius

    def area(self):
        return pi * self.r**2

    def perimeter(self):
        return 2 * pi * self.r

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, с радиусом {self.r},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")


if __name__ == '__main__':
    figures = [Rectangle(2, 3), Square(2, 1, 1), Circle(1)]
    for figure in figures:
        print(figure)
    # a = Square(2, 1, 1)
    # print(a.area())
