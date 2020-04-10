from PopulationSamples.MarginError import MarginError
from Statistics.StandardDeviation import StandardDeviation
from MathOperations.Exponentiation import Exponentiation

class SampleSzKnown():
    @staticmethod

    def sampleSize(sd, data):

        e = MarginError.marginError(sd, data)
        stdDev = StandardDeviation.standardDeviation(data)
        val = (1.96 * stdDev) / e
        sample = Exponentiation.exponent(val, 2)

        return sample