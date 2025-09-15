# tests/test_calculator.py
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
    # subtract from 0 => -3
    c.subtract(3)
    assert c.get_answer() == -3

def test_multiply_updates_answer_isolated():
    c = Calculator()
    # set up a non-zero internal state without relying on add()
    c.answer = 2
    c.multiply(3)
    assert c.get_answer() == 6

def test_power_updates_answer_isolated():
    c = Calculator()
    # set up internal state then power
    c.answer = 2
    c.power(3)  # 2**3 = 8
    assert c.get_answer() == 8

def test_reset_sets_answer_to_zero():
    c = Calculator()
    c.answer = 10
    c.reset()
    assert c.get_answer() == 0

def test_method_chaining_integration():
    c = Calculator()
    # integration test that uses multiple methods together
    c.add(1).multiply(4).subtract(1)  # (0+1)*4 - 1 = 3
    assert c.get_answer() == 3

def test_methods_return_self_for_chaining():
    c = Calculator()
    assert c.add(1) is c
    assert c.subtract(1) is c
    assert c.multiply(1) is c
    assert c.power(1) is c
    assert c.reset() is c





