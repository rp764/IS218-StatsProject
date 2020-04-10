from numpy.random import seed
from numpy.random import randint
from numpy.random import uniform


class RandList():
    @staticmethod
    def listInt(x, y, length, sd):
        if isinstance(x, float):
            return listDec(x, y, length, sd)
        lst = []
        seed(sd)
        for each in range(length):
            num = randint(x, y)
            lst.append(num)
        return lst

    @staticmethod
    def listDec(x, y, length, sd):
        lst = []
        seed(sd)
        for each in range(length):
            num = uniform(x, y)
            lst.append(num)
        return lst