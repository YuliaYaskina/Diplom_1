from unittest.mock import Mock
import pytest
import data


@pytest.fixture(scope='function')
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = data.MockBun.NAME
    bun.get_price.return_value = data.MockBun.PRICE

    return bun

@pytest.fixture(scope='function')
def mock_ingredient1():
    ingredient1 = Mock()
    ingredient1.get_price.return_value = data.MockIngredient1.INGREDIETN1_PRICE
    ingredient1.get_name.return_value = data.MockIngredient1.INGREDIETN1_NAME
    ingredient1.get_type.return_value = data.MockIngredient1.INGREDIETN1_TYPE

    return ingredient1

@pytest.fixture(scope='function')
def mock_ingredient2():
    ingredient2 = Mock()
    ingredient2.get_price.return_value = data.MockIngredient2.INGREDIETN2_PRICE
    ingredient2.get_name.return_value = data.MockIngredient2.INGREDIETN2_NAME
    ingredient2.get_type.return_value = data.MockIngredient2.INGREDIETN2_TYPE

    return ingredient2




