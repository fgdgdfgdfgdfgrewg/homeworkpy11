class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price  # Используем защищенный атрибут
        self.quantity = quantity

        # Валидация при инициализации
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

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
