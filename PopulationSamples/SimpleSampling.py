from Random.SelectWithSeed import SelectWithSeed

from numpy.random import seed


class SimpleSampling(SelectWithSeed):
    @staticmethod

    def generateSampling(sd, lst, rnge):
        seed(sd)
        return SelectWithSeed.pickItem(sd, lst, rnge)