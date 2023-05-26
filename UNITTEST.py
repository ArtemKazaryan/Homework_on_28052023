# Домашняя работа на 28.05.2023

# Модуль 15. Модульное тестирование
# Тема: Модульное тестирование

# Задание 1
# Создайте класс для числа.
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

# Решение:
class IntegerSet:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def mean(self):
        return sum(self.numbers)/len(self.numbers)

    def max(self):
        return max(self.numbers)

    def min(self):
        return min(self.numbers)

import unittest

class TestIntegerSet(unittest.TestCase):
    def test_sum(self):
        integer_set = IntegerSet([1, 2, 3, 4, 5])
        self.assertEqual(integer_set.sum(),15)

    def test_mean(self):
        integer_set = IntegerSet([1, 2, 3, 4, 5])
        self.assertEqual(integer_set.mean(), 3)

    def test_max(self):
        integer_set = IntegerSet([1, 2, 3, 4, 5])
        self.assertEqual(integer_set.max(), 5)

    def test_min(self):
        integer_set = IntegerSet([1, 2, 3, 4, 5])
        self.assertEqual(integer_set.min(), 1)

if __name__ == '__main__':
    unittest.main()




# Задание 2
# Создайте класс для числа.
# В классе должна быть реализована следующая функциональность:
# ■ Запись и чтение значения.
# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчисления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

# Решение:
class IntegerSet:
    def __init__(self, numbers):
        self.numbers = numbers

    def write(self, number):
        self.numbers.append(number)

    def read(self, index):
        return self.numbers[index]

    def to_octal(self, index):
        return oct(self.numbers[index])

    def to_hex(self, index):
        return hex(self.numbers[index])

    def to_binary(self, index):
        return bin(self.numbers[index])

import unittest

class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        self.integer_set = IntegerSet([1, 2, 3, 4, 5])

    def test_write(self):
        self.integer_set.write(6)
        self.assertEqual(self.integer_set.read(5), 6)

    def test_read(self):
        self.assertEqual(self.integer_set.read(3), 4)

    def test_to_octal(self):
        self.assertEqual(self.integer_set.to_octal(2), '0o3')

    def test_to_hex(self):
        self.assertEqual(self.integer_set.to_hex(4), '0x5')

    def test_to_binary(self):
        self.assertEqual(self.integer_set.to_binary(1), '0b10')

if __name__ == '__main__':
    unittest.main()