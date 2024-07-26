
def calculate_structure_sum(structure):
    sum_ = 0

    if isinstance(structure, int):  # Если элемент является числом, возвращаем его значение.
        return structure

    elif isinstance(structure, str):  # Если элемент является строкой, возвращаем его длину.
        return len(structure)

    elif isinstance(structure, (list, tuple, set)):  # Для этих коллекций проходим по каждому элементу и рекурсивно
        # вычисляем их суммы.
        for item in structure:
            sum_ += calculate_structure_sum(item)

    elif isinstance(structure, dict):  # Для словарей проходим по каждому ключу и значению, прибавляя их суммы.
        for key, value in structure.items():
            sum_ += calculate_structure_sum(value)
            sum_ += calculate_structure_sum(key)

    return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)