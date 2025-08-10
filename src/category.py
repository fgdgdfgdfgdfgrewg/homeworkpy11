from .product import BaseProduct, Product


class Category:
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        # Считаем только валидные продукты
        valid_products = [p for p in products if isinstance(p, BaseProduct)]
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

    def middle_price(self):
        """
        Рассчитывает среднюю цену товаров в категории
        Возвращает 0, если в категории нет товаров
        """
        try:
            # Суммируем цены всех товаров
            total_price = sum(product.price for product in self.__products)
            # Делим сумму на количество товаров
            return total_price / len(self.__products)
        except ZeroDivisionError:
            # Обрабатываем случай пустой категории
            return 0
