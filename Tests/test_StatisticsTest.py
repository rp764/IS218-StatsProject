import unittest

from PopSamplingFunctions import SampleSizeKnown, SampleSizeUnknownPop
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [1, 2, 3, 4]
        self.testData2 = [1, 2, 2, 3, 4]
        self.testData3 = [1, 2, 3, 4]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        m = self.statistics.mean(self.testData)
        self.assertEqual(m, 2.5)

    def test_median_calculator(self):
        med = self.statistics.median(self.testData)
        self.assertEqual(med, 2.5)

    def test_mode_calculator(self):
        theMode = self.statistics.mode(self.testData2)
        self.assertEqual(theMode, 2)

    def test_variance_calculator(self):
        v = self.statistics.var(self.testData)
        self.assertEqual(v, 1.25)

    def test_stdDev_calculator(self):
        std = self.statistics.stdDev(self.testData)
        self.assertEqual(std, 1.118033988749895)

    def test_meanDeviation_calculator(self):
        meanDev = self.statistics.meandeviation(self.testData)
        self.assertEqual(meanDev, 1)

    def test_PopulationCorrelation_calculator(self):
        popCo = self.statistics.popCo(PopulationCorrelation.popCor(self.testData, self.testData3))
        self.assertEqual(popCo, -0.22499088742463133)

    def test_RandomNoSeed_Int(self):
        num = self.statistics.randomNoSeedInt(0, 10)
        self.assertEqual(isinstance(num, int), True)

    def test_RandomNoSeed_Dec(self):
        num = self.statistics.randomNoSeedDec(0, 10)
        self.assertEqual(isinstance(num, float), True)

    def test_RandomSeed_Int(self):
        result = self.statistics.randomWithSeedInt(4, 0, 10)
        result2 = self.statistics.randomWithSeedInt(4, 0, 10)
        self.assertEqual(result, result2)

    def test_RandomSeed_Dec(self):
        result = self.statistics.randomWithSeedDec(4, 0, 10)
        result2 = self.statistics.randomWithSeedDec(4, 0, 10)
        self.assertEqual(result, result2)

    def test_RandomListInt(self):
        result = self.statistics.randomListInt(0, 10, 5, 4)
        self.assertEqual(result, [7, 5, 1, 8, 7])

    def test_RandomListDec(self):
        result = self.statistics.randomListDec(0, 10, 5, 4)
        self.assertEqual(result, [9.670298390136766, 5.4723224917572235,
                                  9.726843599648843, 7.148159936743647,
                                  6.977288245972709])

    def test_SimpleRandSampling(self):
        result = self.statistics.SimpleSampling(3, self.testData, 5)
        self.assertEqual(result, [3, 1, 2, 1, 1])

    def test_SystematicRandSampling(self):
        result = self.statistics.SystematicSampling(self.testData)
        self.assertEqual(result, [3, 21, 43, 21, 20])

    def test_ConfidenceInterval(self):
        result = self.statistics.SystematicSampling(.90, self.testData)
        self.assertEqual(result, (0.8046719486285641, 3.9953280513714358))

    def test_Margin_Error(self):
        result = self.statistics.MarginError(3, self.testData)
        self.assertEqual(result, -14.133333333333335)

    def test_Cochran(self):
        result = self.statistics.Cochran(3, self.testData, 4)
        self.assertEqual(result, 0.0010094984628091588)

    def test_sample_size_unknown(self):
        result = SampleSizeUnknownPop.sampleSize(3 , self.testData, 0.41)
        self.assertEqual(result, 0.0012487381269214882)

    def test_sample_size_known(self):
        result = SampleSizeKnown.sampleSize(3, self.testData)
        self.assertEqual(result, 1.0)