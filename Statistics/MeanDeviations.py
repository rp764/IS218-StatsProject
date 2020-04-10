from Statistics.Mean import Mean
from numpy import absolute

class MeanDeviation:
    def __init__(self):
        pass

    @staticmethod
    def meanDeviation(data):
        b = Mean.mean(data)
        total = 0
        v = len(data)
        for i in data:
            total = total + absolute(i-b)
        return total / v