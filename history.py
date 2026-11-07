# history.py
# Сохранение и просмотр истории (Задачи 3 и 4).

# Задача 3: Сохранение истории в файл
def save_history(record):
    # Открываем файл history.txt в режиме добавления ('a')
    with open('history.txt', 'a', encoding='utf-8') as file:
        # Записываем строку с операцией и переходим на новую строку
        file.write(record + '\n')