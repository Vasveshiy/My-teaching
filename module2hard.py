def check():
    while True:
        num = int(input('Введите число от 3 до 20: '))
        if 3 <= num <= 20:
            return num
        else:
            print("Вы ввели некорректное число, повторите попытку.")


number = check()
unique_pairs = set()  # Множество для отслеживания уникальных пар
list = []

print('Ваше число:', number)

for i in range(1, number + 1):
    for j in range(1, number + 1):
        if i != j:  # Исключаем сумму числа с самим собой
            total_sum = i + j
            if total_sum % number == 0:
                pair = (min(i, j), max(i, j))  # Создаем отсортированный кортеж
                if pair not in unique_pairs:
                    unique_pairs.add(pair)
                    list.append(pair)

# Преобразование списка кортежей в строку и удаление скобок
list_str = (str(list).replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace(' ', ''))

print('Ваш шифр:', list_str)
