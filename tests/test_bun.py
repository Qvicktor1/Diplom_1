from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name(self):
        bun = Bun('Сэндвич с курочкой', 1500)
        assert bun.get_name() == 'Сэндвич с курочкой', 'Unable to get bun name'

    def test_bun_get_price(self):
        bun = Bun('Сэндвич с курочкой', 1500)
        assert bun.get_price() == 1500, 'Unable to get bun price'