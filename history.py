# history.py
# Сохранение и просмотр истории (Задачи 3 и 4).

# Задача 3: Сохранение истории в файл
def save_history(record):
    # Открываем файл history.txt в режиме добавления ('a')
    with open('history.txt', 'a', encoding='utf-8') as file:
        # Записываем строку с операцией и переходим на новую строку
        file.write(record + '\n')


# Задача 4: Просмотр истории вычислений
def show_history():
    try:
        # Открываем файл только для чтения ('r')
        with open('history.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # Если файл есть, но он пустой
            if not lines:
                print("\nИстория пока пуста.")
            else:
                print("\n--- История операций ---")
                for line in lines:
                    # strip() убирает лишние пробелы и переносы строк
                    print(line.strip())
                print("------------------------")

    except FileNotFoundError:
        # Если файла еще нет (ни одной операции не делали), не выдаем ошибку
        print("\nИстория пока пуста.")