def get_multiplied_digits (numbers):
    '''
    Принимает аргумент целое число number и подсчитывает произведение цифр этого числа
    :param numbers: Вводимое число
    :return: Произведение цифр числа
    '''
    str_number = str(numbers)  # Превращает введеное число в строку
    first = int(str_number[0])  # берет первую цифру из числа, превращает ее в интеджер

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
print(get_multiplied_digits(12003))