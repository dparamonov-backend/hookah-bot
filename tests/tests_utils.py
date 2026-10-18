import pytest
from comma.utils import validate_phone

class TestPhoneValidation:
    @pytest.mark.parametrize("phone, expected",[
        ('+7 (999) 123-45-67',True),
        ('89993947915',True),
        ('8-999-394-79-15',True),
        ("abc", False),
        ("123",False),
        ("", False),
    ],)
    def test_validate_phone(self, phone:str, expected: bool) -> None:
        assert validate_phone(phone) == expected
