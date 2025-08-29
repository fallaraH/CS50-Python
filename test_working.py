import pytest
from working import convert

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_incorrect_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
