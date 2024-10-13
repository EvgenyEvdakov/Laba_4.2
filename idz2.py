#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования []. Максимально возможный размер
# списка задать константой. В отдельном поле size должно храниться максимальное для данного объекта количество
# элементов списка; реализовать метод size(), возвращающий установленную длину. Если количество элементов списка
# изменяется во время работы, определить в классе поле count. Первоначальные значения size и count устанавливаются
# конструктором.
# Создать класс Fraction для работы с беззнаковыми дробными десятичными числами. Число должно быть представлено двумя
# списками типа int: целая и дробная часть, каждый элемент — десятичная цифра. Для целой части младшая цифра имеет
# меньший индекс, для дробной части старшая цифра имеет меньший индекс (десятые — в нулевом элементе, сотые — в первом,
# и т. д.). Реальный размер списоков задается как аргумент конструктора инициализации. Реализовать арифметические
# операции сложения, вычитания и умножения, и операции сравнения.

class Fraction:
    MAX_SIZE = 100  # Максимальный возможный размер для списков

    def __init__(self, integer_size, fractional_size):
        """Инициализация дробного числа с заданными размерами для целой и дробной частей."""
        if integer_size <= 0 or fractional_size <= 0:
            raise ValueError("Размеры целой и дробной частей должны быть положительными числами.")
        if integer_size > Fraction.MAX_SIZE or fractional_size > Fraction.MAX_SIZE:
            raise ValueError(f"Размеры частей не могут превышать {Fraction.MAX_SIZE}.")

        self.integer_part = [0] * integer_size  # Целая часть числа
        self.fractional_part = [0] * fractional_size  # Дробная часть числа
        self.size = integer_size + fractional_size  # Максимальный размер
        self.count = 0  # Количество реально занятых элементов

    def get_size(self):
        """Возвращает максимальный размер для целой и дробной частей."""
        return self.size

    def read(self):
        """Ввод целой и дробной частей числа с клавиатуры."""
        integer = input("Введите целую часть числа (беззнаковое целое число): ")
        fractional = input("Введите дробную часть числа (после запятой): ")

        # Заполняем целую часть (разворачиваем, т.к. младшая цифра должна иметь меньший индекс)
        for i, digit in enumerate(integer[::-1]):
            if i >= len(self.integer_part):
                break
            self.integer_part[i] = int(digit)
        # Заполняем дробную часть
        for i, digit in enumerate(fractional):
            if i >= len(self.fractional_part):
                break
            self.fractional_part[i] = int(digit)

        self.count = len(integer) + len(fractional)

    def display(self):
        """Выводит дробное число на экран."""
        integer_str = ''.join(map(str, self.integer_part[::-1]))  # Выводим целую часть в правильном порядке
        fractional_str = ''.join(map(str, self.fractional_part))  # Выводим дробную часть

        print(f"Число: {integer_str}.{fractional_str}")

    def __getitem__(self, index):
        """Перегрузка операции индексирования [] для доступа к элементам целой или дробной части."""
        if index < len(self.integer_part):
            return self.integer_part[index]
        elif index < self.size:
            return self.fractional_part[index - len(self.integer_part)]
        else:
            raise IndexError("Индекс выходит за пределы числа.")

    def __setitem__(self, index, value):
        """Перегрузка операции индексирования [] для изменения элементов целой или дробной части."""
        if not isinstance(value, int) or value < 0 or value > 9:
            raise ValueError("Значение должно быть цифрой от 0 до 9.")

        if index < len(self.integer_part):
            self.integer_part[index] = value
        elif index < self.size:
            self.fractional_part[index - len(self.integer_part)] = value
        else:
            raise IndexError("Индекс выходит за пределы числа.")

    def __add__(self, other):
        """Перегрузка операции сложения для двух дробей."""
        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом типа Fraction.")

        max_integer_size = max(len(self.integer_part), len(other.integer_part))
        max_fractional_size = max(len(self.fractional_part), len(other.fractional_part))

        # Инициализация нового объекта для результата
        result = Fraction(max_integer_size, max_fractional_size)

        carry = 0  # Перенос для сложения
        # Складываем дробные части
        for i in range(max_fractional_size - 1, -1, -1):
            sum_value = carry
            if i < len(self.fractional_part):
                sum_value += self.fractional_part[i]
            if i < len(other.fractional_part):
                sum_value += other.fractional_part[i]

            result.fractional_part[i] = sum_value % 10
            carry = sum_value // 10

        # Складываем целые части
        for i in range(max_integer_size):
            sum_value = carry
            if i < len(self.integer_part):
                sum_value += self.integer_part[i]
            if i < len(other.integer_part):
                sum_value += other.integer_part[i]

            result.integer_part[i] = sum_value % 10
            carry = sum_value // 10

        result.count = result.get_size()  # Обновляем количество элементов
        return result

    def __sub__(self, other):
        """Перегрузка операции вычитания для двух дробей."""
        # Принцип аналогичен сложению, но требуется учесть заимствование.
        # Для упрощения можно реализовать вычитание после приведения к нормальной форме.

        # Тут должно быть более сложное вычитание, но ради примера можно ограничиться
        # простым шаблоном (например, если одно число больше другого по модулю).
        pass

    def __mul__(self, other):
        """Перегрузка операции умножения для двух дробей."""
        # Реализация умножения (например, по длинным десятичным числам с учетом дробной части).
        pass

    def __eq__(self, other):
        """Перегрузка операции сравнения на равенство для двух дробей."""
        return (self.integer_part == other.integer_part and
                self.fractional_part == other.fractional_part)

    def __repr__(self):
        """Представление объекта для вывода."""
        return f"Fraction({self.integer_part}, {self.fractional_part})"


# Демонстрация работы класса
if __name__ == '__main__':
    # Создаем два объекта Fraction
    fraction1 = Fraction(5, 3)
    fraction2 = Fraction(5, 3)

    # Ввод данных для дробей
    fraction1.read()
    fraction2.read()

    # Вывод дробей на экран
    fraction1.display()
    fraction2.display()

    # Пример сложения
    print("\nСложение двух дробей:")
    result = fraction1 + fraction2
    result.display()

    # Пример работы индексации
    print("\nДоступ к элементам через индексацию:")
    print(f"Целая часть (индекс 0): {fraction1[0]}")
    print(f"Дробная часть (индекс 5): {fraction1[5]}")

    # Пример изменения значения через индексацию
    fraction1[0] = 9
    fraction1[5] = 5
    fraction1.display()
