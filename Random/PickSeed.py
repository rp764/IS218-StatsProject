from numpy.random import seed
from Random.ItemLst import ItemLst

class PickSeed():
    @staticmethod

    def pickSeed(sd, lst):
        seed(sd)

        return ItemLst.pickItem(lst)