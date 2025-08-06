from .product import Product


class Category:
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        # Считаем только валидные продукты
        valid_products = [p for p in products if isinstance(p, Product)]
        Category.product_count += len(valid_products)

    @classmethod
    def reset_counter(cls):
        """Сброс счетчика для тестирования"""
        cls.product_count = 0

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)
        if isinstance(product, Product):
            Category.product_count += 1
