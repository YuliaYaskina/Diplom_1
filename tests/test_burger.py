import data
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
import pytest


class TestBurger:

    names = ['black bun', 'ржаная', 'ПШЕНИЧНАЯ', 'bun_12345']
    @pytest.mark.parametrize('name', 'names')
    def test_set_buns_check_name(self, name):
        bun = Bun(name, 100)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.name == name

    prices = [0, 100, 1000, 9999999999]
    @pytest.mark.parametrize('price', prices)
    def test_set_buns_check_price(self, price):
        bun = Bun("black bun", price)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun.price == price

    def test_get_recipy(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        recipe = burger.get_receipt()
        assert recipe == '''(==== black bun ====)
= sauce hot sauce =
= filling cutlet =
(==== black bun ====)

Price: 800'''
    def test_move_ingredient(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0,1)
        recipe = burger.get_receipt()
        assert recipe == '''(==== black bun ====)
= filling cutlet =
= sauce hot sauce =
(==== black bun ====)

Price: 800'''

    def test_add_ingredient_add_two_ingredients(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 200)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 400)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        recipe = burger.get_receipt()
        assert "cutlet" and "hot sauce" in recipe

    def test_remove_ingredient(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)
        recipe = burger.get_receipt()
        assert "hot sauce" not in recipe

    def test_get_price(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        assert burger.get_price() == data.MockBun.PRICE*2 + data.MockIngredient1.INGREDIETN1_PRICE + data.MockIngredient2.INGREDIETN2_PRICE

