from func1 import find_substring
from func2 import count_words


def main():
    print("Запуск проекта...")
    
    text = "Hello, world! This is an educational project in Python."

    # Тест первой функции
    query = "educational"
    position = find_substring(query, text)
    print(f"Ищем '{query}' в строке: '{text}'")
    print(f"Позиция: {position}")
    
    # Тест второй функции
    word_count = count_words(text)
    print(f"Количество слов в строке:  {word_count}")


if __name__ == "__main__":
    main()
