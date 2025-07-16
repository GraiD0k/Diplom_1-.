from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture()
def burger():
    """Фиксура Инициализации бургера"""
    return Burger()


@pytest.fixture()
def mock_bun():
    """Мок для булочки"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Красная булочка"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture()
def mock_ingredients():
    """Мок ингредиентов"""
    sauce = Mock(spec=Ingredient)
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "Чили"
    sauce.get_price.return_value = 50.0

    filling = Mock(spec=Ingredient)
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "Говядина"
    filling.get_price.return_value = 200.0

    return [sauce, filling]
