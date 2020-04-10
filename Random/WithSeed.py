from numpy.random import seed
from numpy.random import uniform
from numpy.random import randint

class WithSeed():
    @staticmethod
    def randomInt(sd, x, y):
        seed(sd)
        num = randint(x, y)
        if isinstance(x, float):
            return WithSeed.randomDec(sd, x, y)

        return num

    @staticmethod
    def randomDec(sd, x, y):
        seed(sd)
        num = uniform(x, y)

        return num