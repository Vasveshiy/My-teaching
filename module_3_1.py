import random

calls = 0


def count_calls(a=1):
    global calls
    calls += 1


def string_info(string):
    string_length = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    string = string_length, upper_string, lower_string
    count_calls()
    print(f' Ваша строка проанализирована: {string}')
    return string


def is_contains(string, list_to_search):
    if string in list_to_search:
        count_calls()
        print(True)
        return True
    else:
        count_calls()
        print(False)
        return False


random_int = random.randint(1, 3)  # Получение случайного целого числа от 1 до 3

for i in range(random_int):
    print(f'Попытка: {i + 1} из {random_int}')
    string_info(input(str("Введите строку для анализа: ")))

list_input = input("Введите список (разделенный запятыми): ")
search_string = input("Введите искомую строку: ")
is_contains(search_string, list_input)

# is_contains(input(str("Введите ИСКОМУЮ строку: ")), input(list["Введите СПИСОК для поиска: "]))

print(f' Функция вызывалась: {calls} раз(а)')
