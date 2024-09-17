class Animal:
    """
    # Класс животного
    """
    def __init__(self, name, alive=True, fed=False ):
        """

        :type name: object
        """
        self.name = name
        self.alive = alive
        self.fed = fed

class Plant:
    """
    # Класс растений
    """
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    """
    # Класс млекопитающего (унаследован от Animal)
    """

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}, это не растение.")

class Predator (Animal):
    """
    # Класс хищника (унаследован от Animal)
    """

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не может есть {food}, это не растение.")

class Flower(Plant):
    """
    # Класс цветка (унаследован от Plant)
    """
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    """
    # Класс фрукта  (унаследован от Plant)
    """
    def __init__(self, name):
        super().__init__(name)
        self.edible = True   # Переопределяем edible для фруктов


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)