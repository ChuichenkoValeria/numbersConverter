# Выполнила Чуйченко Валерия Дмитриевна. Группа . Вариант 17


import unittest
from functions import convert_number, convert_numbers


class TestConvertNumber(unittest.TestCase):
    def test_less_0_2(self):
        """
        тестируем первое условие -- меньше -0.2

        в этом случае мы вне области определения (т.к. берется корень),
        поэтому должны получить строку "<передано число не из области определения>"
        """
        result = convert_number(-1)
        self.assertEqual(result, "<передано число не из области определения>")

    def test_zero(self):
        """
        тестируем второе условие -- больше или равен -0.2.
        проще всего проверить для нуля
        """
        result = convert_number(0)
        self.assertEqual(result, 1.0)

    def test_not_number(self):
        """
        тестируем, что при передаче не числа получаем строку
        "<передано не число>"
        """
        result = convert_number("hello")
        self.assertEqual(result, "<передано не число>")

class TestConvertNumbers(unittest.TestCase):
    def test(self):
        """
        проверим, что для трех условий из тестов функции одного
        аргумента получим строку из
        их результатов через запятую
        """
        result = convert_numbers(-1, 0, "hello")
        self.assertEqual(result, "<передано число не из области определения>, 1.0, <передано не число>")


if __name__ == "__main__":
    unittest.main()
