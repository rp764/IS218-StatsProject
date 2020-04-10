from Random.SelectWithSeed import SelectWithSeed


class PopulationProportion():
    def __init__(self):
        pass

    @staticmethod
    def proportion(sd, data, range):
        data2 = SelectWithSeed.pickItem(sd, data, range)
        proportion = len(data2) / len(data)
        return proportion
