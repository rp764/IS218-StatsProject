import numpy


class Covariance():
    def __init__(self):
        pass

    @staticmethod
    def covariance(a, b):
        return numpy.cov(a, b)[0, 1]
