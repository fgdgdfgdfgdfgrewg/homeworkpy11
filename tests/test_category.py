import pytest
from src.category import Category
from src.product import Product, Smartphone, LawnGrass


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


def test_add_valid_product(sample_category, sample_smartphone):
    initial_count = len(sample_category.products)
    initial_total = Category.product_count

    sample_category.add_product(sample_smartphone)

    assert len(sample_category.products) == initial_count + 1
    assert sample_smartphone in sample_category.products
    assert Category.product_count == initial_total + 1


def test_add_invalid_product(sample_category):
    initial_count = len(sample_category.products)
    initial_total = Category.product_count

    with pytest.raises(TypeError) as excinfo:
        sample_category.add_product("Not a product")

    assert "Можно добавлять только объекты Product или его наследников" in str(excinfo.value)
    assert len(sample_category.products) == initial_count
    assert Category.product_count == initial_total


def test_products_property(sample_category, sample_product, sample_grass):
    sample_category.add_product(sample_grass)

    products = sample_category.products
    assert len(products) == 2
    assert sample_product in products
    assert sample_grass in products


def test_static_product_count(sample_product, sample_smartphone):
    # Сброс статической переменной перед тестом
    Category.product_count = 0

    cat1 = Category("Cat1", "Desc1", [sample_product])
    assert Category.product_count == 1

    cat2 = Category("Cat2", "Desc2", [sample_smartphone, sample_product])
    assert Category.product_count == 3

    cat1.add_product(sample_smartphone)
    assert Category.product_count == 4


def test_add_multiple_valid_products(sample_category, sample_product, sample_smartphone, sample_grass):
    initial_count = len(sample_category.products)
    initial_total = Category.product_count

    sample_category.add_product(sample_smartphone)
    sample_category.add_product(sample_grass)

    assert len(sample_category.products) == initial_count + 2
    assert sample_smartphone in sample_category.products
    assert sample_grass in sample_category.products
    assert Category.product_count == initial_total + 2


def test_initialization_with_empty_products():
    category = Category("Empty", "No products", [])

    assert category.name == "Empty"
    assert category.description == "No products"
    assert category.products == []
    assert Category.product_count == 0
