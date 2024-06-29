import pytest

from unittest.mock import Mock


class MockBun:
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Булочка с кунжутом'
    mock_bun.get_price.return_value = 1000


class MockIngredientSauce:
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_name.return_value = 'Соус сырный'
    mock_ingredient_sauce.get_price.return_value = 3000
    mock_ingredient_sauce.get_type.return_value = 'SAUCE'


class MockIngredientFilling:
    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_name.return_value = 'Говяжья котлета'
    mock_ingredient_filling.get_price.return_value = 5000
    mock_ingredient_filling.get_type.return_value = 'FILLING'


class TestBurger:

    def test_burger_set_buns(self, burger):
        assert burger.get_price() == 2000, 'Burger price is not equal double price of the bun'

    @pytest.mark.parametrize('ingredient, total_price',
                             [[MockIngredientSauce.mock_ingredient_sauce, 5000],
                              [MockIngredientFilling.mock_ingredient_filling, 7000]])
    def test_burger_add_ingredient(self, burger, ingredient, total_price):
        burger.add_ingredient(ingredient)
        assert burger.get_price() == total_price, 'Wrong burger price'

    def test_burger_remove_ingredient(self, burger):
        burger.add_ingredient(MockIngredientFilling.mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.get_price() == 2000, 'Ingredient was not removed successfully'

    def test_burger_move_ingredient(self, burger):
        burger.add_ingredient(MockIngredientFilling.mock_ingredient_filling)
        burger.add_ingredient(MockIngredientSauce.mock_ingredient_sauce)
        burger.move_ingredient(0, 1)
        assert burger.get_price() == 10000, 'Ingredient was not moved successfully'

    def test_burger_get_receipt(self, burger):
        burger.add_ingredient(MockIngredientFilling.mock_ingredient_filling)
        assert '(==== Булочка с кунжутом ====)' in burger.get_receipt(), \
            'The name of the bun is not included to the receipt of the burger'
        assert burger.get_receipt().count('(==== Булочка с кунжутом ====)') == 2, \
            'The name of the bun is not included twice in the receipt of the burger'
        assert '= filling Говяжья котлета =' in burger.get_receipt(), \
            'The name of the ingredient is not included to the receipt of the burger'
        assert 'Price: 7000' in burger.get_receipt(), 'Wrong burger price'