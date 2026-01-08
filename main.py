import math

# Base class for operations
class Operation:
    def execute(self, a, b=None):
        raise NotImplementedError("This method should be overridden in subclasses.")

# Binary operations
class Addition(Operation):
    def execute(self, a, b):
        return a + b

class Subtraction(Operation):
    def execute(self, a, b):
        return a - b

class Multiplication(Operation):
    def execute(self, a, b):
        return a * b

class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
      
class Root(Operation):
    def execute(self, a, b=None):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)

class Sine(Operation):
    def execute(self, a, b=None):
        return math.sin(math.radians(a))  # input in degrees

class Cosine(Operation):
    def execute(self, a, b=None):
        return math.cos(math.radians(a))  # input in degrees

