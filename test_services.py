import unittest
from func1 import find_substring
from func2 import count_words

TEXT = "Это учебный проект"


class TestFindSubstring(unittest.TestCase):

    def test_found(self):
        cases = [("учебный", 4), ("Это", 0), ("проект", 12)]
        for query, expected in cases:
            with self.subTest(query=query):
                self.assertEqual(find_substring(query, TEXT), expected)

    def test_not_found(self):
        self.assertEqual(find_substring("тесты", TEXT), -1)
        self.assertEqual(find_substring("тесты", ""), -1)

    def test_returns_first_occurrence(self):
        self.assertEqual(find_substring("ab", "xxabyyab"), 2)

    def test_case_sensitive(self):
        self.assertEqual(find_substring("это", TEXT), -1)

    def test_empty_query(self):
        # Пустая подстрока находится в начале любой строки
        self.assertEqual(find_substring("", TEXT), 0)
        self.assertEqual(find_substring("", ""), 0)


class TestCountWords(unittest.TestCase):

    def test_counts(self):
        cases = [
            ("Привет мир это проект", 4),
            ("Привет", 1),
            ("Привет   мир", 2),            # несколько пробелов
            ("   Привет мир   ", 2),        # пробелы по краям
            ("", 0),
            ("   ", 0),
            ("один\tдва\nтри", 3),          # табуляция и перевод строки
            ("Привет, мир!", 2),            # знаки препинания прилипают к словам
            ("a - b", 3),                   # отдельное тире считается словом
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(count_words(text), expected)


if __name__ == "__main__":
    unittest.main()
