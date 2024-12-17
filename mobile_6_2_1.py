class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = False
        self.__set_sides(sides)

    @property
    def sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all([isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b)])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):
        return len(new_sides) == self.sides_count and all([isinstance(side, int) and side > 0 for side in new_sides])

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def __set_sides(self, sides):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

import math

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius=1):
        super().__init__(color, radius)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * self.radius**2
def heron_formula(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.sides
        return heron_formula(a, b, c)
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length=1):
        super().__init__(color, *(edge_length,) * self.sides_count)

    def get_volume(self):
        edge_length = self.sides[0]
        return edge_length**3
if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())     # [55, 66, 77]

    cube1.set_color(300, 70, 15)   # Не изменится
    print(cube1.get_color())       # [222, 35, 130]

    # Проверка на изменение сторон
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())        # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

    circle1.set_sides(15)           # Изменится
    print(circle1.get_sides())      # [15]

    # Проверка периметра (круга), это и есть длина
    print(len(circle1))             # 15

    # Проверка объема (куба)
    print(cube1.get_volume())       # 216
