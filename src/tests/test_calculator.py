from src.calculator import Calculator

def test_initial_answer_is_zero():
    c = Calculator()
    assert c.get_answer() == 0

