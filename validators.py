# validators.py
# Валидация ввода, сделанная с помощью ИИ (Задачи 5 и 6).


# Задача 5: Код проверки ввода сгенерирован с помощью веб-версии DeepSeek.
def get_number(prompt: str) -> float | int:
    """Запрашивает у пользователя число и возвращает его.

    Функция повторяет запрос до тех пор, пока пользователь не введёт
    корректное целое или дробное число.

    Args:
        prompt: Текст приглашения ко вводу.

    Returns:
        Введённое пользователем число (int или float).
    """
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            try:
                return float(user_input)
            except ValueError:
                print("Ошибка: введите число (целое или дробное).")


if __name__ == "__main__":
    number = get_number("Введите число: ")
    print(f"Вы ввели: {number} ({type(number).__name__})")