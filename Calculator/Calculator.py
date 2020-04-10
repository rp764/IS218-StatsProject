
from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Division import Division
from MathOperations.Multiplication import Multiplication
from MathOperations.Exponentiation import Exponentiation
from MathOperations.Root import Root
from MathOperations.Logarithm import Logarithm

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def subtract(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def multiply(self, a, b):
        self.Result = Multiplication.multiply(a, b)
        return self.Result

    def divide(self, a, b):
        self.Result = Division.divide(a, b)
        return self.Result

    def exponent(self, a, b):
        self.Result = Exponentiation.exponent(a, b)
        return self.Result

    def root(self, a, b):
        self.Result = Root.root(a, b)
        return self.Result

    def log(self, a, b):
        self.Result = Logarithm.log(a, b)
        return self.Result