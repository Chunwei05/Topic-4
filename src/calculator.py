class Calculator:
    """
    A simple calculator that maintains an internal answer.
    Supports method chaining by returning self for operations.
    """

    def __init__(self):
        self.answer = 0

    def get_answer(self):
        """Return the current internal value of the calculator."""
        return self.answer

    def reset(self):
        """Reset the internal value to zero."""
        self.answer = 0
        return self

    def add(self, num):
        """Add a number to the current answer."""
        self.answer += num
        return self

    def subtract(self, num):
        """Subtract a number from the current answer."""
        self.answer -= num
        return self

    def multiply(self, num):
        """Multiply the current answer by a number."""
        self.answer *= num
        return self

    def power(self, num):
        """Raise the current answer to the power of num."""
        self.answer **= num
        return self
