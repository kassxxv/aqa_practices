from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side * self.__side

    def get_perimeter(self):
        return 4 * self.__side

    @property
    def name(self):
        return "Квадрат"


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 3.14 * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * 3.14 * self.__radius

    @property
    def name(self):
        return "Коло"


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    @property
    def name(self):
        return "Прямокутник"

figures = [Circle(10), Rectangle(5, 8), Square(10)]
for figure in figures:
    print(f'Фігура {figure.name}, площа = {figure.get_area()}, перимететр = {figure.get_perimeter()}.')