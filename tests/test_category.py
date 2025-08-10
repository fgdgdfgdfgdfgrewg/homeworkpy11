import pytest
from src.category import Category
from src.product import Product, Smartphone, LawnGrass
from src.exceptions import ZeroQuantityError


# Фикстуры для создания тестовых данных
@pytest.fixture
def sample_product():
    return Product("Test Product", "Description", 100.0, 5)


@pytest.fixture
def sample_smartphone():
    return Smartphone("Smartphone", "Desc", 500.0, 3, 90.0, "ModelX", 128, "Black")


@pytest.fixture
def sample_grass():
    return LawnGrass("Grass", "Desc", 50.0, 10, "Russia", "7 days", "Green")


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Category Description", [sample_product])


@pytest.fixture
def empty_category():
    return Category("Empty Category", "No products", [])


@pytest.fixture(autouse=True)
def reset_counter():
    Category.reset_counter()


# Тесты для класса Category
def test_category_initialization(sample_product):
    category = Category("Electronics", "Tech products", [sample_product])

    assert category.name == "Electronics"
    assert category.description == "Tech products"
    assert category.products == [sample_product]
    assert Category.product_count == 1


def test_initialization_with_empty_products():
    category = Category("Empty", "No products", [])

    assert category.name == "Empty"
    assert category.description == "No products"
    assert category.products == []
    assert Category.product_count == 0


# Новые тесты для метода middle_price
def test_middle_price_single_product(sample_category, sample_product):
    """Тест средней цены с одним товаром"""
    assert sample_category.middle_price() == 100.0


def test_middle_price_multiple_products(sample_category, sample_product):
    """Тест средней цены с несколькими товарами"""
    product2 = Product("Test Product 2", "Description 2", 200.0, 2)
    sample_category.add_product(product2)

    # (100 + 200) / 2 = 150
    assert sample_category.middle_price() == 150.0


def test_middle_price_empty_category(empty_category):
    """Тест средней цены для пустой категории"""
    assert empty_category.middle_price() == 0


def test_middle_price_after_adding_products(empty_category):
    """Тест средней цены после добавления товаров"""
    # Начинаем с пустой категории
    assert empty_category.middle_price() == 0

    # Добавляем первый товар
    product1 = Product("Product 1", "Desc", 100.0, 5)
    empty_category.add_product(product1)
    assert empty_category.middle_price() == 100.0

    # Добавляем второй товар
    product2 = Product("Product 2", "Desc", 300.0, 2)
    empty_category.add_product(product2)
    assert empty_category.middle_price() == 200.0  # (100 + 300) / 2


def test_middle_price_with_different_product_types(sample_category):
    """Тест средней цены с разными типами товаров"""
    smartphone = Smartphone("S", "Desc", 500.0, 3, 90.0, "Model", 128, "Black")
    grass = LawnGrass("G", "Desc", 50.0, 10, "Russia", "7 days", "Green")

    sample_category.add_product(smartphone)
    sample_category.add_product(grass)

    # Цены: 100 (первый товар) + 500 + 50 = 650
    # Среднее: 650 / 3 ≈ 216.67
    assert round(sample_category.middle_price(), 2) == 216.67


def test_middle_price_with_zero_price_products(sample_category):
    """Тест средней цены с товарами по нулевой цене"""
    zero_price_product = Product("Free", "Description", 0.0, 10)
    sample_category.add_product(zero_price_product)

    # Цены: 100 + 0 = 100
    # Среднее: 100 / 2 = 50
    assert sample_category.middle_price() == 50.0


def test_middle_price_after_removing_products(sample_category, sample_product):
    """Тест средней цены после удаления товаров (косвенно)"""
    # Добавляем второй товар
    product2 = Product("Product 2", "Desc", 300.0, 2)
    sample_category.add_product(product2)
    assert sample_category.middle_price() == 200.0

    # "Удаляем" первый товар, создавая новую категорию без него
    # (В текущей реализации класса нет метода удаления, поэтому имитируем)
    new_category = Category("New", "Desc", [product2])
    assert new_category.middle_price() == 300.0


def test_category_product_count_with_invalid_addition(sample_category):
    """Тест счетчика товаров при попытке добавить невалидный продукт"""
    initial_count = Category.product_count

    # Пытаемся добавить не продукт
    with pytest.raises(TypeError):
        sample_category.add_product("invalid")

    # Счетчик не должен измениться
    assert Category.product_count == initial_count
