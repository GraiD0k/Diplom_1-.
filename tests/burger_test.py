import pytest
from praktikum.burger import Burger


class TestBurger:

    # Тесты инициализации
    def test_burger_initialization(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    # Тесты работы с булочкой
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тесты добавления ингредиентов
    def test_add_ingredient(self, burger, mock_ingredients):
        burger.add_ingredient(mock_ingredients[0])
        assert len(burger.ingredients) == 1
        assert mock_ingredients[0] in burger.ingredients

    # Тесты удаления ингредиентов
    def test_remove_ingredient(self, burger, mock_ingredients):
        burger.ingredients = mock_ingredients.copy()
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert mock_ingredients[0] not in burger.ingredients

    def test_remove_invalid_ingredient_index(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    # Тесты перемещения ингредиентов
    def test_move_ingredient(self, burger, mock_ingredients):
        burger.ingredients = mock_ingredients.copy()
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredients[1], mock_ingredients[0]]

    # Тесты расчета цены
    def test_get_price_with_bun_and_ingredients(self, burger, mock_bun, mock_ingredients):
        burger.set_buns(mock_bun)
        burger.ingredients = mock_ingredients
        assert burger.get_price() == 100.0 * 2 + 50.0 + 200.0

    def test_get_price_without_bun_raises_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()

    # Тесты генерации чека
    def test_get_receipt(self, burger, mock_bun, mock_ingredients):
        burger.set_buns(mock_bun)
        burger.ingredients = mock_ingredients

        expected_receipt = (
            "(==== Красная булочка ====)\n"
            "= sauce Чили =\n"
            "= filling Говядина =\n"
            "(==== Красная булочка ====)\n\n"
            "Price: 450.0"
        )

        assert burger.get_receipt() == expected_receipt