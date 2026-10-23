import unittest
from func1 import find_substring
from func2 import count_words

class TestServiceFunctions(unittest.TestCase):

    def test_find_substring_success(self):
        # Обычный случай: подстрока найдена в середине
        self.assertEqual(find_substring("учебный", "Это учебный проект"), 4)
        
        # Подстрока в самом начале
        self.assertEqual(find_substring("Это", "Это учебный проект"), 0)
        
        # Подстрока в самом конце
        self.assertEqual(find_substring("проект", "Это учебный проект"), 12)

    def test_find_substring_not_found(self):
        # Подстрока отсутствует в тексте
        self.assertEqual(find_substring("тесты", "Это учебный проект"), -1)
        
        # Поиск в пустой строке
        self.assertEqual(find_substring("тесты", ""), -1)

    def test_count_words_standard(self):
        # Обычный текст
        self.assertEqual(count_words("Привет мир это проект"), 4)
        
        # Одно слово
        self.assertEqual(count_words("Привет"), 1)

    def test_count_words_spaces(self):
        # Несколько пробелов подряд
        self.assertEqual(count_words("Привет   мир"), 2)
        
        # Пробелы в начале и в конце строки
        self.assertEqual(count_words("   Привет мир   "), 2)
        
        # Пустая строка или строка только из пробелов
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("   "), 0)

if __name__ == "__main__":
    unittest.main()
