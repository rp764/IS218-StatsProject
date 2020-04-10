from scipy.stats import sem, t

from PopulationSamples.ConfidenceInterv import ConfidenceInterv
from PopulationSamples.SimpleSample import SimpleSample


class ConfidenceInterval(ConfidenceInterv):
    @staticmethod
    def confidenceInterval(conf, data, sd, higher):
        sample = SimpleSample.generateSampling(sd, data, higher)
        return ConfidenceInterv.confidenceIntervalPop(conf, sample)