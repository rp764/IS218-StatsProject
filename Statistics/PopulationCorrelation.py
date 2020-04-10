from Statistics.Covariance import Covariance
from Statistics.StandardDeviation import StandardDeviation


class PopulationCorrelation:
    def __init__(self):
        pass

    @staticmethod
    def populationCorrelation(a, b):
        cov = Covariance.covariance(a, b)
        std1 = StandardDeviation.standardDeviation(a)
        std2 = StandardDeviation.standardDeviation(b)
        return cov / (std1 * std2)
