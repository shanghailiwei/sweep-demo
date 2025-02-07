def test_add():
    from src.calculator import add
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    from src.calculator import subtract
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0

def test_multiply():
    from src.calculator import multiply
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6

def test_divide():
    from src.calculator import divide
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
