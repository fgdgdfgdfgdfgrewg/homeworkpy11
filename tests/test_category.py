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


def test_initialization_with_empty_products():
    category = Category("Empty", "No products", [])

    assert category.name == "Empty"
    assert category.description == "No products"
    assert category.products == []
    assert Category.product_count == 0
