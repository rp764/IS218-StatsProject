from scipy.stats import sem, t
from Statistics.Mean import Mean


class ConfidenceInterv():
    @staticmethod
    def confidenceInterv(conf, data):
        lngth = len(data)
        mean = Mean.mean(data)
        std_err = sem(data)
        high = std_err * t.ppf((1 + conf) / 2, lngth - 1)

        start = mean - high
        end = mean + high

        return start, end
