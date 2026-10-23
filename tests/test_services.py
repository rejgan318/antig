import pytest

from func1 import find_substring
from func2 import count_words

TEXT = "Это учебный проект"


# --- find_substring ---

@pytest.mark.parametrize("query, expected", [
    ("учебный", 4),
    ("Это", 0),
    ("проект", 12),
])
def test_find_substring_found(query, expected):
    assert find_substring(query, TEXT) == expected


@pytest.mark.parametrize("query, text", [
    ("тесты", TEXT),
    ("тесты", ""),
])
def test_find_substring_not_found(query, text):
    assert find_substring(query, text) == -1


def test_find_substring_returns_first_occurrence():
    assert find_substring("ab", "xxabyyab") == 2


def test_find_substring_case_sensitive():
    assert find_substring("это", TEXT) == -1


@pytest.mark.parametrize("text", [TEXT, ""])
def test_find_substring_empty_query(text):
    # Пустая подстрока находится в начале любой строки
    assert find_substring("", text) == 0


# --- count_words ---

@pytest.mark.parametrize("text, expected", [
    ("Привет мир это проект", 4),
    ("Привет", 1),
    ("Привет   мир", 2),            # несколько пробелов
    ("   Привет мир   ", 2),        # пробелы по краям
    ("", 0),
    ("   ", 0),
    ("один\tдва\nтри", 3),          # табуляция и перевод строки
    ("Привет, мир!", 2),            # знаки препинания прилипают к словам
    ("a - b", 3),                   # отдельное тире считается словом
])
def test_count_words(text, expected):
    assert count_words(text) == expected
