from numpy.random import randint
from numpy.random import uniform


class NoSeed():
    @staticmethod
    def randomInt(x, y):
        if isinstance(x, float):
            return NoSeed.randomDec(x, y)
        return randint(x, y)

    @staticmethod
    def randomDec(x, y):
        return uniform(x, y)