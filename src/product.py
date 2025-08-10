from abc import ABC, abstractmethod


class ZeroQuantityError(ValueError):
    """Пользовательское исключение для товаров с нулевым количеством"""
    pass


class BaseProduct(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def quantity(self):
        pass


class CreationLoggerMixin:
    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args}, {kwargs}")
        # Не вызываем super().__init__() здесь, так как это миксин


class Product(CreationLoggerMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        # Валидация параметров
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

        # Вызов миксина после инициализации атрибутов
        super().__init__(name, description, price, quantity)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (f"Smartphone('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
                f"{self.efficiency}, '{self.model}', {self.memory}, '{self.color}')")


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (f"LawnGrass('{self.name}', '{self.description}', {self.price}, {self.quantity}, "
                f"'{self.country}', '{self.germination_period}', '{self.color}')")
