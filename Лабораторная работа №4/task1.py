from math import pi


class Parallelepiped:
    """
    Данный класс предназначен для определения
    объема и массы параллелепипеда
    """

    def __init__(self, length: float, width: float, height: float):
        """
        Инициализация параллелепипеда.
        :param length: Длина основания.
        :param width: Ширина основания.
        :param height: Высота параллелепипеда.
         """
        self.length = length
        self.width = width
        self.height = height


    @property
    def volume(self) -> float:
        """
        Атрибут "объем", который вычисляется
        на основе других атрибутов(длины, ширины и высоты).
        :return: Возвращает объем параллелепипеда.
        """
        return self.length * self.width * self.height


    def __str__(self) -> str:
        """
        Строковое представление параллелепипеда.
        :return: Строка с информацией о сторонах параллелепипеда.
        """
        return f"Параллелепипед со сторонами a = {self.length}, b = {self.width}, c = {self.height} и объемом v = {self.volume}"


    def __repr__(self) -> str:
        """
        Официальное строковое представление параллелепипеда.
        :return: Строка, позволяющая воспроизвести экземпляр класса.
        """
        return f"{self.__class__.__name__}(length={self.length!r}, width={self.width!r}, height={self.height!r})"


    def mass(self, den: float) -> float:
        """Метод, который вычисляет массу фигуры.
        :param den: Плотность фигуры.
        :return: Возвращает массу фигуры.
        """
        return den * self.volume


class Sphere(Parallelepiped):
    """
    Данный класс предназначен для определения
    объема и массы шара. Для класса применяется наследование от базового
    класса Parallelepiped для сокращения одинаковых строчек кода.
    """


    def __init__(self, radius: float):
        """
        Инициализация шара.
        :param radius: Радиус шара.
        """
        self.radius = radius


    @property
    def volume(self) -> float:
        """
        Перегрузка атрибута "объем" для расчёта объема шара по своей формуле.
        :return: Возвращает объем шара.
        """
        return 4 / 3 * pi * self.radius ** 3


    def __str__(self) -> str:
        """
        Строковое представление шара.
        :return: Строка с информацией о радиусе шара.
        """
        return f"Сфера с радиусом r = {self.radius} и объемом v = {self.volume}"


    def __repr__(self) -> str:
        """
        Официальное строковое представление шара.
        :return: Строка, позволяющая воспроизвести экземпляр класса.
        """
        return f"{self.__class__.__name__}(radius={self.radius!r})"


if __name__ == "__main__":
    # Write your solution here
    pass

