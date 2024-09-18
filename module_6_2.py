class Vehicle():
    # Атрибут класса, содержащий список допустимых цветов
    __COLOR_VARIANTS = ["Красный", "Синий", "Чёрный", "Белый", "Зелёный"]

    def __init__(self, owner, __model, __engine_power, __color):
        """
        :param owner: Инициализация владельца транспорта
        :param __model: модель (марка) транспорта
        :param __engine_power: мощность двигателя
        :param __color: цвет машины
        """
        self.owner = owner  # Инициализация владельца транспорта
        self.__model = __model  # - модель (марка) транспорта.
        self.__engine_power = __engine_power  # - мощность двигателя.
        self.__color = __color  # цвет машины

    def get_model(self):
        """Возвращает строку с названием модели транспорта"""
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        """Печатает информацию о машине"""
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        """
        Замена цвета по каталогу производителя
        :param new_color: новый цвет
        :return: Замена или невозможность замены
        """
        if new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
            print(f'Установлен цвет {new_color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    # Атрибут класса, содержащий максимальное количество пассажиров
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'Синий')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Розовый')
vehicle1.set_color('Чёрный')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


