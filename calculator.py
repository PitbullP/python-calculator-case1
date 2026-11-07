# calculator.py
# Математические операции (Задачи 1 и 2).

# Задача 1: Математические операции
def add(a, b):
    # Сложение
    return a + b


def subtract(a, b):
    # Вычитание
    return a - b


def multiply(a, b):
    # Умножение
    return a * b


def divide(a, b):
    # Деление
    return a / b


# Задача 2: Работа с целыми и десятичными числами
def format_number(result):
    # Если число целое (например, 5.0), убираем точку и возвращаем 5
    if result.is_integer():
        return int(result)
    # Если число дробное (например, 5.5), оставляем как есть
    return result
