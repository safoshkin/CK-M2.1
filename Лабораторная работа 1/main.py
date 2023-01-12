import doctest


class BoxOfSweets:
    """
    Документация на класс.
    Класс описывает модель коробки конфет.
    """
    def __init__(self, quantity_sweets: int, cost: (int, float)):
        """
        Создание и подготовка объекта "Коробка конфет".

        :param quantity_sweets: Количество конфет
        :param cost: Стоимость одной конфеты

        Пример инициализации экземпляра класса:
        >>> box = BoxOfSweets(15, 20)
        """
        if not isinstance(quantity_sweets, int):
            raise TypeError('Количество конфет должно быть типа int')
        if quantity_sweets <= 0:
            raise ValueError('Количество конфет должно быть положительным числом')
        if not isinstance(cost, (int, float)):
            raise TypeError('Стоимость конфеты должна быть типа int или float')
        if cost <= 0:
            raise ValueError('Стоимость конфеты должна быть положительным числом')
        self.quantity_sweets = quantity_sweets
        self.cost = cost
        self.cost_of_box = None
        self.cost_of_box_()

    def sweets_left(self, eaten_sweets: int):
        """
        Метод вычитает количество конфет из их общего числа.

        :param eaten_sweets: Количество съеденных конфет

        Пример:
        >>> box = BoxOfSweets(15, 20)
        >>> box.sweets_left(3)
        """
        if not isinstance(eaten_sweets, int):
            raise TypeError('Количество съеденных конфет должно быть типа int')
        if eaten_sweets <= 0:
            raise ValueError('Количество съеденных конфет должно быть положительным числом')
        self.quantity_sweets -= eaten_sweets

    def cost_of_box_(self):
        """
        Метод вычисляет стоимость коробки конфет.

        Пример:
        >>> box = BoxOfSweets(15, 20)
        >>> box.cost_of_box_()
        """
        self.cost_of_box = self.quantity_sweets * self.cost


class BagOfCement:
    """
    Документация на класс.
    Класс описывает модель мешка цемента.
    """
    def __init__(self, weight_kg: (int, float), cost_kg: (int, float)):
        """
        Создание и подготовка объекта "Мешок цемента".

        :param weight_kg: Вес мешка в кг
        :param cost_kg: Стоимость одного кг цемента

        Пример инициализации экземпляра класса:
        >>> bag = BagOfCement(25, 50)
        """
        if not isinstance(weight_kg, (int, float)):
            raise TypeError('Вес мешка цемента должен быть типа int или float')
        if weight_kg <= 0:
            raise ValueError('Вес мешка цемента должен быть положительным числом')
        if not isinstance(cost_kg, (int, float)):
            raise TypeError('Стоимость 1 кг цемента должна быть типа int или float')
        if cost_kg <= 0:
            raise ValueError('Стоимость 1 кг цемента должна быть положительным числом')
        self.weight_kg = weight_kg
        self.cost_kg = cost_kg
        self.cost_of_bag = None
        self.cost_of_bag_()
        self.water_liter = None
        self.water_liter_()

    def cost_of_bag_(self):
        """
        Метод вычисляет стоимость мешка цемента.

        Пример:
        >>> bag = BagOfCement(25, 50)
        >>> bag.cost_of_bag_()
        """
        self.cost_of_bag = self.weight_kg * self.cost_kg

    def water_liter_(self):
        """
        Метод вычисляет минимальное количество воды для затворения цемента (водоцементное отношение принимаем 60%).

        Пример:
        >>> bag = BagOfCement(25, 50)
        >>> bag.water_liter_()
        """
        self.water_liter = self.weight_kg * 0.6


class AcademicGroup:
    """
    Документация на класс.
    Класс описывает модель академической группы.
    """
    def __init__(self, students: int, scholar: int):
        """
        Создание и подготовка объекта "Академической группа".

        :param students: Количество студентов в группе
        :param scholar: Количество стипендиатов в группе

        Пример инициализации экземпляра класса:
        >>> group = AcademicGroup(25, 5)
        """
        if not isinstance(students, int):
            raise TypeError('Количество студентов должно быть типа int')
        if students <= 0:
            raise ValueError('Количество студентов должно быть положительным числом')
        if not isinstance(scholar, int):
            raise TypeError('Количество стипендиатов должно быть типа int')
        if scholar <= 0:
            raise ValueError('Количество стипендиатов должно быть положительным числом')
        if scholar > students:
            raise ValueError('Количество стипендиатов не должно превышать количество студентов')
        self.students = students
        self.scholar = scholar
        self.percent_of_scholar = None
        self.percent_of_scholar_()

    def percent_of_scholar_(self):
        """
        Метод вычисляет процент стипендиатов от общего количества студентов.

        Пример:
        >>> group = AcademicGroup(25, 5)
        >>> group.percent_of_scholar_()
        """
        self.percent_of_scholar = (self.scholar // self.students) * 100

    def left_after_the_session(self, expelled):
        """
        Метод вычисляет количество студентов, продолжающих обучение после сессии.

        :param expelled: Количество отчисленных студентов

        Пример:
        >>> group = AcademicGroup(25, 5)
        >>> group.left_after_the_session(3)
        """
        if not isinstance(expelled, int):
            raise TypeError('Количество отчисленных студентов должно быть типа int')
        if expelled < 0:
            raise ValueError('Количество отчисленных студентов должно быть неотрицательным числом')
        if expelled > self.students:
            raise ValueError('Количество отчисленных студентов не должно превышать общее количество студентов')
        self.students -= expelled

    if __name__ == "__main__":
        doctest.testmod()
