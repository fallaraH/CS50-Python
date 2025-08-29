import pytest
from seasons import minutes_since_birth

def test_minutes_since_birth():
    assert minutes_since_birth("2024-05-23") == "Five hundred twenty-five thousand, six hundred"

def test_minutes_since_birth_format():
    with pytest.raises(SystemExit):
        minutes_since_birth("2024/05/23")
