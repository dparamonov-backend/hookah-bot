import pytest
from comma.money import KITS, Kit

class TestKitModel:
    def test_kit_creation(self) -> None:
        kit = Kit(code = "test", name = "Test", price = 100)
        assert kit.code == "test"
        assert kit.price == 100

    @pytest.mark.parametrize("code, expected_price",
                             [
                                 ('standart',1990),
                                 ('premium',2390)
                             ],
                             )
    def test_kit_price(self, code: str, expected_price: int|float) -> None:
        assert KITS[code].price == expected_price
