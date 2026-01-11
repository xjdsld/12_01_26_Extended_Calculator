import math

class Operation:
    def execution(self, a, b=None):
        raise NotImplementedError

class Addition(Operation):
    def execution(self, a, b):
        return a + b

class Substraction(Operation):
    def execution(self, a, b):
        return a - b

class Multiplication(Operation):
    def execution(self, a, b):
        return a * b

class Division(Operation):
    def execution(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError

class Cosine(Operation):
    def execution(self, a, b=None):
        return math.cos(math.radians(a))

class Sine(Operation):
    def execution(self, a, b=None):
        return math.sin(math.radians(a))

class Root(Operation):
    def execution(self, a, b=None):
        if a > 0:
            return math.sqrt(a)
        else:
            raise ValueError
