class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return False

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        if isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print("h1: ", h1)
print("h2: ", h2)

print("Равенство: ", h1 == h2) # __eq__
print("Равенство: ", h1 == 2) # __eq__

h1 = h1 + 11 # __add__
print(h1)
print("Равенство: ", h1 == h2) # __eq__

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 + h2)

print("Больше: ", h1 > h2) # __gt__
print("Больше или равно: ", h1 >= h2) # __ge__
print("Меньше: ", h1 < h2) # __lt__
print("Меньше или равно: ", h1 <= h2) # __le__
print("Не равно: ", h1 != h2) # __ne__