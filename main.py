from src.product import Product, Smartphone, LawnGrass
from src.category import Category
from src.exceptions import ZeroQuantityError

if __name__ == '__main__':
    # Демонстрация обработки нулевого количества товара
    print("\n=== Тест создания товара с нулевым количеством ===")
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ZeroQuantityError as e:
        print(f"Ошибка при создании товара: {e}")
    else:
        print("Товар успешно создан")
    finally:
        print("Обработка создания товара завершена")

    # Создание корректных товаров
    print("\n=== Создание корректных товаров ===")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    print("Товары успешно созданы")

    # Демонстрация обработки нулевого количества для смартфона
    print("\n=== Тест создания смартфона с нулевым количеством ===")
    try:
        smartphone_invalid = Smartphone(
            "Неудачный смартфон", "Бракованная партия", 50000.0, 0, 80.0, "Defect", 64, "Черный"
        )
    except ZeroQuantityError as e:
        print(f"Ошибка при создании смартфона: {e}")
    else:
        print("Смартфон успешно создан")
    finally:
        print("Обработка создания смартфона завершена")

    # Создание корректных смартфонов
    print("\n=== Создание корректных смартфонов ===")
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    print("Смартфоны успешно созданы")

    # Демонстрация обработки нулевого количества для газонной травы
    print("\n=== Тест создания газонной травы с нулевым количеством ===")
    try:
        grass_invalid = LawnGrass(
            "Просроченная трава", "Истек срок годности", 500.0, 0, "Китай", "0 дней", "Желтый"
        )
    except ZeroQuantityError as e:
        print(f"Ошибка при создании газонной травы: {e}")
    else:
        print("Газонная трава успешно создана")
    finally:
        print("Обработка создания газонной травы завершена")

    # Создание корректной газонной травы
    print("\n=== Создание корректной газонной травы ===")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    print("Газонная трава успешно создана")

    # Тестирование сложения товаров
    print("\n=== Тестирование сложения товаров ===")
    smartphone_sum = smartphone1 + smartphone2
    print(f"Суммарная стоимость смартфонов: {smartphone_sum}")

    grass_sum = grass1 + grass2
    print(f"Суммарная стоимость газонной травы: {grass_sum}")

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError as e:
        print(f"Ошибка при сложении разных типов товаров: {e}")
    else:
        print("Сложение разных типов товаров выполнено успешно")

    # Создание категорий
    print("\n=== Создание категорий товаров ===")
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    # Добавление третьего смартфона в категорию
    category_smartphones.add_product(smartphone3)
    print(f"Товары в категории смартфонов: {category_smartphones.products}")

    # Тестирование добавления невалидного товара
    print("\n=== Тест добавления невалидного товара ===")
    try:
        category_smartphones.add_product("Not a product")
    except TypeError as e:
        print(f"Ошибка при добавлении невалидного товара: {e}")
    else:
        print("Невалидный товар успешно добавлен")

    # Демонстрация подсчета средней цены
    print("\n=== Подсчет средней цены товаров в категориях ===")
    print(f"Средняя цена смартфонов: {category_smartphones.middle_price():.2f}")
    print(f"Средняя цена газонной травы: {category_grass.middle_price():.2f}")

    # Создание пустой категории
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена пустой категории: {category_empty.middle_price()}")

    # Тестирование добавления товара с нулевым количеством в категорию
    print("\n=== Тест добавления товара с нулевым количеством в категорию ===")
    try:
        zero_product = Product("Товар с нулем", "Нельзя добавить", 100.0, 0)
    except ZeroQuantityError as e:
        print(f"Ошибка при создании товара: {e}")
        print("Товар не был создан, поэтому не может быть добавлен в категорию")

    # Попытка добавить в категорию товар, который не был создан из-за ошибки
    if 'zero_product' not in locals():
        try:
            # Попытка обратиться к несуществующей переменной
            category_smartphones.add_product(zero_product)
        except NameError:
            print("Ошибка: переменная zero_product не определена")

    # Итоговая статистика
    print("\n=== Итоговая статистика ===")
    print(f"Общее количество товаров во всех категориях: {Category.product_count}")
    print("Программа завершена успешно")
