# main.py
# Консольный интерфейс (Задача 7).

from calculator import add, subtract, multiply, divide, format_number
from history import save_history, show_history
from validators import get_number


def main():
    # Бесконечный цикл для работы меню, пока пользователь не выберет выход
    while True:
        print("\n--- Консольный калькулятор ---")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Просмотр истории")
        print("6. Выход")
        
        choice = input("Выберите пункт меню (1-6): ")
        
        if choice in ['1', '2', '3', '4']:
            # Запрашиваем числа с проверкой на буквы (из validators.py)
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            
            # Выполняем нужную операцию
            if choice == '1':
                result = add(a, b)
                operation = "+"
            elif choice == '2':
                result = subtract(a, b)
                operation = "-"
            elif choice == '3':
                result = multiply(a, b)
                operation = "*"
            elif choice == '4':
                result = divide(a, b)
                operation = "/"
                
            # Если результат - строка (ошибка деления на ноль), не форматируем его
            if isinstance(result, str):
                print(f"\nРезультат: {result}")
                record = f"{a} {operation} {b} = {result}"
            else:
                # Форматируем результат (убираем лишний .0 у целых чисел)
                formatted_result = format_number(result)
                print(f"\nРезультат: {formatted_result}")
                # Записываем в историю
                record = f"{a} {operation} {b} = {formatted_result}"
                
            save_history(record)
            
        elif choice == '5':
            # Показываем историю (из history.py)
            show_history()
            
        elif choice == '6':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Ошибка: неверный пункт меню. Попробуйте снова.")


if __name__ == "__main__":
    main()