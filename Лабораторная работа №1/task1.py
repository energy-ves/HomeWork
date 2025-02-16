from math import pi
from typing import Union
import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Book:
    """
    Класс, который описывает прочитанные книги.
    """
    def __init__(self, author: str, book_title: str, pages: int):
        """Инициализация экземпляра класса.
        :param author: Имя автора книги.
        :param book_title: Название книги.
        :param pages: Общее количество страниц книги.
        Все указанные параметры присваиваются в качестве атрибутов
        экземпляра класс.
        Атрибут current_page позволяет при необходимости дополнительно добавлять номер
        последней прочитанной страницы книги.
        Example:
        >>> book_1 = Book("М.Ю Лермонтов", "Бородино", 28)
        >>> print(book_1.author, book_1.book_title, book_1.pages)
        М.Ю Лермонтов Бородино 28
        """
        if not isinstance(author, str):
            raise TypeError("Имя автора str")
        self.author = author
        if not isinstance(pages, int):
            raise TypeError("Количество страниц int")
        self.pages = pages
        if not isinstance(book_title, str):
            raise TypeError("Название книги str")
        self.book_title = book_title
        self.current_page = None


    def init_current_page(self, current_page: int):
        """
        Метод позволяет уточнить последнюю прочитанную страницу.
        :param current_page: Фактическое количество прочитанных страниц.
        :raise ValueError: Вызывается ошибка, если номер текущей страницы
        больше количества страниц в книге или номер текущей страницы отрицательный.
        """
        if current_page < 0:
            raise ValueError("Число страниц не может быть отрицательным")
        if self.pages < current_page:
            raise ValueError("Неверно указано количество страниц")
        ...


    def increment_last_read_page(self, read_pages: int):
        """Метод позволяет увеличить количество прочитанных страниц в книге.
        :param read_pages: Количеств страниц, которое прибавляется к уже прочитанным страницам.
        :raise ValueError: Вызывается ошибка, если номер текущей страницы
        больше количества страниц в книге или число прочитанный страниц отрицательно.
        """
        if read_pages < 0:
            raise ValueError("Число страниц не может быть отрицательным")
        ...
        if self.pages < self.current_page:
            raise ValueError("Неверно указано количество страниц")


class VesselVolume:
    """Класс, рассчитывает объем цилиндрического сосуда
     по диаметру и высоте
    """
    def __init__(self, diameter: Union[int, float], height: Union[int, float]):
        """
        Инициализация экземпляра класса.
        :param diameter: Диаметр сосуда.
        :param height: Высота сосуда.
        Все указанные параметры присваиваются в качестве атрибутов
        экземпляра класс.
        Кроме того, атрибут volume содержит значение объема сосуда.
        """
        if not isinstance(diameter, (int, float)):
            raise TypeError("Диаметр только str или float")
        self.diameter = diameter
        if not isinstance(height, (int, float)):
            raise TypeError("Высота только str или float")
        self.height = height
        self.volume = None
        self.init_volume(diameter, height)


    def init_volume(self, diameter: Union[int, float], height: Union[int, float]):
        """
        Метод рассчитывает объем цилиндра и присваивает его в качестве атрибута.
        Объем округляется до 1 знака после запятой.
        В качестве аргументов метод принимает те же параметры, что и в конструкторе.
        Example:
        >>> vessel_1 = VesselVolume(10, 10)
        >>> print (vessel_1.volume)
        785.4
        """
        self.volume = round(pi * diameter ** 2 / 4 * height, 1)


    def init_volume_increment(self, diameter_increment: Union[int, float]=0, height_increment: Union[int, float]=0):
        """
        Метод позволяет рассчитывать объем цилиндра при увеличении или уменьшении его высоты
        или длины, или длины и высоты.
        Объем округляется до 1 знака после запятой.
        :param diameter_increment: Приращение диаметра.
        :param height_increment: Приращение высоты.
        :raise ValueError: Вызывается ошибка, если отрицательное
        приращение диаметра или высоты больше первоначальной высоты или
        диампетра сосуда.
        Example:
        >>> vessel_1 = VesselVolume(10, 10)
        >>> vessel_1.init_volume_increment(5)
        >>> print (vessel_1.volume)
        1767.1
        """
        if not isinstance(diameter_increment, (int, float)):
            raise TypeError("Приращение диаметра только str или float")
        if not isinstance(height_increment, (int, float)):
            raise TypeError("Приращение высоты только str или float")
        new_volume = round(pi * (self.diameter + diameter_increment) ** 2 / 4 * (self.height + height_increment), 1)
        if new_volume < 0:
            raise ValueError("Неправильно заданы изменения высоты или(и) длины")
        self.volume = new_volume


class Calculator:
    """
    Класс для выполнения простейших арифметических операций c двумя
    аргументами.
    """
    def __init__(self, a: Union[int, float], b: Union[int, float]):
        """
        Инициализация экземпляра класса.
        :param a: Первое число.
        :param b: второе число.
        Все указанные параметры присваиваются в качестве атрибутов
        экземпляра класс.
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Число может быть только int или float")
        self.a = a
        if not isinstance(b, (int, float)):
            raise TypeError("Число может быть только int или float")
        self.b = b


    def add(self) -> Union[int, float]:
        """
        Метод реализует сложение двух чисел.
        :return: Сумма a и b.
        Example:
        >>> calc = Calculator(5, 4)
        >>> calc.add()
        9
        """
        return self.a + self.b


    def subtract(self) -> Union[int, float]:
        """
        Метод реализует вычитание второго числа из первого.
        :return: Разность a и b.
        Example:
        >>> calc = Calculator(5, 4)
        >>> calc.subtract()
        1
        """
        return self.a - self.b


    def multiply(self) -> Union[int, float]:
        """
        Метод реализует умножение двух чисел.
        :return: Произведение a и b.
        Example:
        >>> calc = Calculator(5, 4)
        >>> calc.multiply()
        20
        """
        return self.a * self.b


    def divide(self) -> Union[int, float]:
        """
        Метод реализуеи деление первого числа на второе.
        :return: Частное a и b.
        :raise ValueError: если b равно 0, то выдается сообщение об ошибке.
        Example:
        >>> calc = Calculator(8, 4)
        >>> calc.divide()
        2.0
        """
        if self.b == 0:
            raise ValueError("Ошибка: деление на ноль.")
        return self.a / self.b


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest