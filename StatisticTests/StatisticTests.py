from Calculator.Calculator import Calculator
from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.PopulationCorrelation import PopulationCorrelation
from Statistics.Quartiles import Quartiles
from Statistics.Skewness import Skewness
from Statistics.Variance import Variance
from Statistics.StandardDeviation import StandardDeviation
from Statistics.MeanDeviation import MeanDeviation
from Random.NoSeed import NoSeed
from Random.WithSeed import WithSeed
from Random.RandLst import RandLst
from PopulationSamples.SimpleSampling import SimpleSampling
from PopulationSamples.SystematicSample import SystematicSample
from PopulationSamples.ConfidenceInterv import ConfidenceInterv
from PopulationSamples.MarginError import MarginError
from PopulationSamples.ConfidenceInterv import ConfidenceInterv
from PopulationSamples import SampleSzKnown, SampleSzUnkown


class Statistics(Calculator):

    def __init__(self):
        self.result = Mean.mean(data)

    def mean(self, data):
        return self.result

    def median(self, data):
        self.result = Median.median(data)
        return self.result

    def mode(self, data):
        self.result = Mode.mode(data)
        return self.result

    def var(self, data):
        self.result = Variance.variance(data)
        return self.result

    def std(self, data):
        self.result = StandardDeviation.standardDeviation(data)
        return self.result

    def mean_deviation(self, data):
        self.result = MeanDeviation.meanDeviation(data)
        return self.result

    def quart(self, data):
        self.result = Quartiles.quartiles(data)
        return self.result

    def skew(self, data):
        self.result = Skewness.skewness(data)
        return self.result

    def popCo(self, data, data2):
        self.result = PopulationCorrelation.popCor(data, data2)
        return self.result

    def randomNoSeedInt(self, a, b):
        self.result = NoSeed.randomInt(a, b)
        return self.result

    def randomNoSeedDec(self, a, b):
        self.result = NoSeed.randomDec(a, b)
        return self.result

    def randomWithSeedInt(self, sd, a, b):
        self.result = WithSeed.randomInt(sd, a, b)
        return self.result

    def randomWithSeedDec(self, sd, a, b):
        self.result = WithSeed.randomDec(sd, a, b)
        return self.result

    def randomListInt(self, a, b, lngth, sd):
        self.result = RandLst.listInt(a, b, lngth, sd)
        return self.result

    def randomListDec(self, a, b, lngth, sd):
        self.result = RandLst.listDec(a, b, lngth, sd)
        return self.result

    def SimpleSampling(self, sd, lst, rnge):
        self.result = SimpleSampling.generateSampling(sd, lst, rnge)
        return self.result

    def SystematicSampling(self, lst):
        self.result = SystematicSample.systematicSampling(lst)
        return self.result

    def ConfidenceIntervalSample(self, conf, data, sd, higher):
        self.result = ConfidenceInterv.ConfidenceInterv(conf, data, sd, higher)
        return self.result

    def MarginError(self, data, n):
        self.result = MarginError.marginError(data, n)
        return self.result

    def test_Cochran(self, sd, data, rnge):
        self.result = ConfidenceInterv.cochran(sd, data, rnge)
        return self.result

    def test_SampleSizeUnknown(self, sd, data, percentage):
        self.result = SampleSzUnkown.SampleSizeUnkownPop(sd, data, percentage)
        return self.result

    def test_SampleSizeknown(self, sd, data):
        self.result = SampleSzKnown.SampleSzKnownPop(sd, data)
        return self.result