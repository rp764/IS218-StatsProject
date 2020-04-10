from MathOperations.Addition import Addition
from MathOperations.Division import Division

class Mean:
    @staticmethod
    def mean(data):
        num_values = len(data)
        total = 0
        for num in data:
            total = Addition.sum(total, num)
        return Division.divide(total, num_values)

