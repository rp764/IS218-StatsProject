from Statistics.Zscore import Zscore
from PopulationSamples.MarginError import MarginError
from MathOperations.Exponentiation import Exponentiation

class SampleSizeUnkownPop():
    @staticmethod

    def sampleSize(sd, data, percentage):
        z = Zscore.zscore(sd, data)
        e = MarginError.marginError(sd, data)
        p = percentage
        q = 1 - p
        val = z/e
        sample = Exponentiation.exponent(val, 2) * p * q

        return sample