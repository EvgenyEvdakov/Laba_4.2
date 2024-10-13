#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав имеющиеся в Python средства
# перегрузки операторов.

class Pair:
    def __init__(self, first=None, second=None):
        """Инициализация полей first (калорийность) и second (масса продукта)"""
        if first is not None and (not isinstance(first, int) or first <= 0):
            raise ValueError("Поле 'first' должно быть целым положительным числом (калорийность 100 г продукта).")
        if second is not None and (not isinstance(second, (int, float)) or second <= 0):
            raise ValueError("Поле 'second' должно быть положительным числом (масса продукта в килограммах).")

        self.first = first
        self.second = second

    def read(self):
        """Ввод значений с клавиатуры с проверкой"""
        try:
            self.first = int(input("Введите калорийность 100 г продукта (целое положительное число): "))
            if self.first <= 0:
                raise ValueError
        except ValueError:
            print("Ошибка: значение калорийности должно быть целым положительным числом.")
            return

        try:
            self.second = float(input("Введите массу продукта в килограммах (положительное число): "))
            if self.second <= 0:
                raise ValueError
        except ValueError:
            print("Ошибка: значение массы должно быть положительным числом.")

    def display(self):
        """Вывод значений на экран"""
        if self.first is None or self.second is None:
            print("Данные не заполнены.")
        else:
            print(f"Калорийность 100 г продукта: {self.first} ккал")
            print(f"Масса продукта: {self.second} кг")

    def power(self):
        """Вычисление общей калорийности продукта"""
        if self.first is None or self.second is None:
            print("Невозможно вычислить общую калорийность. Данные не заполнены.")
            return None
        return self.first * self.second * 10  # 100 г = 0.1 кг, поэтому умножаем на 10

    def __add__(self, other):
        """Перегрузка оператора сложения для объектов Pair"""
        if isinstance(other, Pair):
            return Pair(self.first + other.first, self.second + other.second)
        raise TypeError("Операнд должен быть объектом Pair.")

    def __sub__(self, other):
        """Перегрузка оператора вычитания для объектов Pair"""
        if isinstance(other, Pair):
            return Pair(max(0, self.first - other.first), max(0, self.second - other.second))
        raise TypeError("Операнд должен быть объектом Pair.")

    def __eq__(self, other):
        """Перегрузка оператора равенства (==)"""
        if isinstance(other, Pair):
            return self.first == other.first and self.second == other.second
        return False

    def __ne__(self, other):
        """Перегрузка оператора неравенства (!=)"""
        return not self.__eq__(other)

    def __repr__(self):
        """Представление объекта для вывода (print)"""
        return f"Pair(first={self.first}, second={self.second})"


# Внешняя функция создания объекта Pair
def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка при создании объекта: {e}")
        return None


if __name__ == '__main__':
    # Демонстрация возможностей класса с перегрузкой операторов

    # Создание двух объектов Pair
    pair1 = make_pair(250, 1.5)  # Калорийность 100 г = 250 ккал, масса = 1.5 кг
    pair2 = make_pair(150, 0.8)  # Калорийность 100 г = 150 ккал, масса = 0.8 кг

    if pair1 and pair2:
        print("Созданные объекты:")
        print(pair1)
        print(pair2)

        # Сложение объектов Pair
        print("\nСложение двух объектов Pair:")
        pair_sum = pair1 + pair2
        print(pair_sum)
        print(f"Общая калорийность продуктов после сложения: {pair_sum.power()} ккал")

        # Вычитание объектов Pair
        print("\nВычитание двух объектов Pair:")
        pair_diff = pair1 - pair2
        print(pair_diff)
        print(f"Общая калорийность продуктов после вычитания: {pair_diff.power()} ккал")

        # Сравнение объектов на равенство
        print("\nСравнение объектов на равенство:")
        if pair1 == pair2:
            print("Объекты равны.")
        else:
            print("Объекты не равны.")

        # Ввод нового значения с клавиатуры
        print("\nВвод данных вручную для первого объекта:")
        pair1.read()
        pair1.display()
        print(f"Общая калорийность продукта: {pair1.power()} ккал")
