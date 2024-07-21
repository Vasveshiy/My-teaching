# 1. Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1,2,3])
print_params()
print_params(0, 1, 2)
print_params('', '', '')

#  2. Распаковка параметров:
values_list = [1, 'Hello!', (1, 2, 3)]
values_dict = {'a':0, 'b':'строка', 'c':True}

print_params(values_list)
print_params(*values_list)
print_params('', '', '')
print_params(values_dict)
print_params(**values_dict)
print_params('', '', '')

# 3. Распаковка + отдельные параметры:
values_list_2 = ['Vasyan', 2.1]
print_params(*values_list_2, 42)

