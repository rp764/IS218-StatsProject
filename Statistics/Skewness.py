import scipy.stats
class Skewness:
    @staticmethod
    def skewness(data):
        return scipy.stats.skew(data)