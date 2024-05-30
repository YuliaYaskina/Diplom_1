from praktikum.ingredient import Ingredient


class TestIngredient():
    def test_get_name(self):
        ingredient = Ingredient('SAUCE', "hot", 500)
        assert ingredient.get_name() == 'hot'

    def test_get_type(self):
        ingredient = Ingredient('SAUCE', "hot", 500)
        assert ingredient.get_type() == 'SAUCE'


    def test_get_price(self):
        ingredient = Ingredient('SAUCE', "hot", 500)
        assert ingredient.get_price() == 500

