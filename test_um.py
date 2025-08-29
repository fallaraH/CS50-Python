from um import count

def test_count():
    assert count("Um") == 1

def test_count_between_word():
    assert count("yummy") == 0

def test_count_space():
    assert count(" um ") == 1
