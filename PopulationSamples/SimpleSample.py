from Statistics.Zscore import Zscore
from PopulationSamples.MarginError import MarginError
from Statistics.PopulationProportion import PopulationProportion
from MathOperations.Exponentiation import Exponentiation


class SimpleSample():
    @staticmethod
    def SimpleSample(sd, data, rnge):


        z = Zscore.zscore(data)
        p = PopulationProportion.proportion(sd, data, rnge)
        e = MarginError.margin(sd, data)
        q = 1 - p

        cochran = (Exponentiation.exponent(z, 2) * p * q)/Exponentiation.exponent(e, 2)

        return SimpleSample