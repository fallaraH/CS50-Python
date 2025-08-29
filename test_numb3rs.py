from numb3rs import validate

def test_validate_format():
    assert validate("123.321") == False
    assert validate("123.") == False

def test_validate_corner_numbers():
    assert validate("000.1.999.23") == False
    assert validate("0.1.2.3") == True
    assert validate("-2.34.24.100") == False
