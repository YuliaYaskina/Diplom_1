from praktikum.bun import Bun
class TestBun:
    def test_get_name_valid_name(self):
        bun = Bun(name='Ржаная', price=100)
        assert bun.get_name() == 'Ржаная'

    def test_get_price_valid_price(self):
        bun = Bun(name='Ржаная', price=100)
        assert bun.get_price() == 100

