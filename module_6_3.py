class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь как атрибут экземпляра
        self.sound = 'Frrr'  # Звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденную дистанцию
        return self.x_distance  # Возвращаем текущую дистанцию.


class Eagle:
    def __init__(self):
        self.y_distance = 0  # - высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # - звук, который издаёт орёл (отсылка)

    def fly(self, dy):
        self.y_distance += dy  # - изменение высоты полёта
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):          # Вызываем конструкторы родителей
        # super().__init__()  # выдает ошибку
        Horse.__init__(self)  # Инициализация атрибутов Horse
        Eagle.__init__(self)  # Инициализация атрибутов Eagle

    def move(self, dx, dy):
        self.run(dx)  # Увеличиваем пройденную дистанцию
        self.fly(dy)  # Увеличиваем высоту полета

    def get_pos(self):
        # Возвращает текущее положение пегаса в виде кортежа (x_distance, y_distance)
        return self.x_distance, self.y_distance

    def voice(self):
        # Выводим звук, который унаследован от родителя
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
