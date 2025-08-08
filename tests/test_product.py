import pytest
from src.product import Product, Smartphone, LawnGrass


# Фикстуры
@pytest.fixture
def sample_product():
    return Product("Test Product", "Description", 100.0, 5)


@pytest.fixture
def sample_smartphone():
    return Smartphone("Smartphone", "Desc", 500.0, 3, 90.0, "ModelX", 128, "Black")


@pytest.fixture
def sample_grass():
    return LawnGrass("Grass", "Desc", 50.0, 10, "Russia", "7 days", "Green")


# Тесты
def test_product_repr(sample_product):
    repr_str = repr(sample_product)
    assert "Test Product" in repr_str
    assert "Description" in repr_str
    assert "100.0" in repr_str
    assert "5" in repr_str
    assert "Product(" in repr_str


def test_smartphone_repr(sample_smartphone):
    repr_str = repr(sample_smartphone)
    assert "Smartphone" in repr_str
    assert "ModelX" in repr_str
    assert "128" in repr_str
    assert "Black" in repr_str


def test_lawn_grass_repr(sample_grass):
    repr_str = repr(sample_grass)
    assert "Grass" in repr_str
    assert "Russia" in repr_str
    assert "7 days" in repr_str
    assert "Green" in repr_str


def test_negative_price():
    with pytest.raises(ValueError) as excinfo:
        Product("P1", "Desc", -100.0, 2)
    assert "Цена не может быть отрицательной" in str(excinfo.value)


def test_negative_quantity():
    with pytest.raises(ValueError) as excinfo:
        Product("P1", "Desc", 100.0, -2)
    assert "Количество не может быть отрицательным" in str(excinfo.value)


# Тесты для функционала сложения
def test_add_same_products(sample_product):
    p1 = sample_product
    p2 = Product("Another Product", "Desc", 200.0, 2)
    total = p1 + p2
    assert total == (100.0 * 5) + (200.0 * 2)


def test_add_same_smartphones(sample_smartphone):
    s1 = sample_smartphone
    s2 = Smartphone("S2", "Desc", 600.0, 2, 95.0, "ModelY", 256, "White")
    total = s1 + s2
    assert total == (500.0 * 3) + (600.0 * 2)


def test_add_same_lawn_grasses(sample_grass):
    g1 = sample_grass
    g2 = LawnGrass("G2", "Desc", 70.0, 5, "USA", "5 days", "Blue")
    total = g1 + g2
    assert total == (50.0 * 10) + (70.0 * 5)


def test_add_different_classes(sample_product, sample_smartphone, sample_grass):
    # Проверяем все возможные комбинации разных классов
    with pytest.raises(TypeError) as excinfo:
        sample_product + sample_smartphone
    assert "Нельзя складывать товары разных классов" in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        sample_smartphone + sample_grass
    assert "Нельзя складывать товары разных классов" in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        sample_grass + sample_product
    assert "Нельзя складывать товары разных классов" in str(excinfo.value)


def test_add_invalid_type(sample_product):
    with pytest.raises(TypeError) as excinfo:
        sample_product + 100
    assert "Нельзя складывать товары разных классов" in str(excinfo.value)


# Тесты для иерархии наследования
def test_inheritance():
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)


def test_instance_types(sample_product, sample_smartphone, sample_grass):
    assert isinstance(sample_product, Product)
    assert isinstance(sample_smartphone, Smartphone)
    assert isinstance(sample_smartphone, Product)
    assert isinstance(sample_grass, LawnGrass)
    assert isinstance(sample_grass, Product)


# Тесты для граничных случаев
def test_zero_quantity_addition():
    p1 = Product("P1", "Desc", 100.0, 0)
    p2 = Product("P2", "Desc", 200.0, 0)
    assert p1 + p2 == 0


def test_large_quantities_addition():
    p1 = Product("P1", "Desc", 10.0, 10000)
    p2 = Product("P2", "Desc", 20.0, 20000)
    assert p1 + p2 == (10.0 * 10000) + (20.0 * 20000)

def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct()

def test_mixin_logging(capsys):
    p = Product("Test", "Desc", 100, 5)
    captured = capsys.readouterr()
    assert "Создан объект класса Product с параметрами: ('Test', 'Desc', 100, 5)" in captured.out

def test_smartphone_mixin_logging(capsys):
    s = Smartphone("S", "Desc", 500, 3, 90.0, "Model", 128, "Black")
    captured = capsys.readouterr()
    assert "Smartphone" in captured.out

def test_grass_mixin_logging(capsys):
    g = LawnGrass("G", "Desc", 50, 10, "Russia", "7 days", "Green")
    captured = capsys.readouterr()
    assert "LawnGrass" in captured.out