from src.calculator import Calculator

def test_initial_answer_is_zero():
    c = Calculator()
    assert c.get_answer() == 0

def test_add_updates_answer():
    c = Calculator()
    c.add(5)
    assert c.get_answer() == 5

def test_subtract_updates_answer():
    c = Calculator()
    c.add(10).subtract(4)
    assert c.get_answer() == 6

def test_multiply_updates_answer():
    c = Calculator()
    c.add(2).multiply(3)
    assert c.get_answer() == 6

def test_power_updates_answer():
    c = Calculator()
    c.add(2).power(3)  # 2^3 = 8
    assert c.get_answer() == 8

def test_reset_sets_answer_to_zero():
    c = Calculator()
    c.add(10).reset()
    assert c.get_answer() == 0

def test_chaining_operations():
    c = Calculator()
    c.add(1).multiply(4).subtract(1)
    assert c.get_answer() == 3




