def find_substring(query: str, text: str) -> int:
    """
    Ищет подстроку query в строке text.
    Возвращает индекс первого вхождения (0-indexed) или -1, если подстрока не найдена.
    """
    return text.find(query)
