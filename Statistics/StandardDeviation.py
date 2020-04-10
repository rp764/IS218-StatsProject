from MathOperations.Root import Root
from Statistics.Variance import Variance


class StandardDeviation:
    def __init__(self):
        pass

    @staticmethod
    def standardDeviation(data):
        return Root.root(Variance.variance(data), 2)
