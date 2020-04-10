import unittest
from random import randint, seed

from PopulationSamples.Cochran import Cochran
from PopulationSamples.SimpleSampling import SimpleSampling
from PopulationSamples.SystematicSampling import SystematicSampling
from PopulationSamples.ConfidenceInterval import ConfidenceInterval
from PopulationSamples.MarginError import MarginError
from PopulationSamples.SampleSizeKnown import SampleSizeKnownPop
from PopulationSamples.SampleSizeUnknownPop import SampleSizeUnkownPop

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        seed(4)
        self.testData = randint(0, 50)

    def test_generate_sample(self):
        result = SimpleSampling.generateSampling(3, self.testData, 5)
        self.assertEqual(result, [3, 1, 2, 1, 1])

    def test_SystematicSampling(self):
        result = SystematicSampling.systematicSampling(self.testData)
        self.assertEqual(result, [3, 21, 43, 21, 20])

    def test_ConfidenceInterval(self):
        result = ConfidenceInterval.confidenceInterval(.90, 1, 5, self.testData)
        self.assertEqual(result, (0.8046719486285641, 3.9953280513714358))

    def test_Margin_Error(self):
        result = MarginError.marginError(self.testData, 3)
        self.assertEqual(result, -14.133333333333335)

    def test_Cochran(self):
        result = Cochran.cochran(3, self.testData, 4)
        self.assertEqual(result, 0.0010094984628091588)

    def test_SampleSizeUnKnownPop(self):
        result = SampleSizeUnkownPop.sampleSize(3, self.testData, .5)
        self.assertEqual(result, 0.0010094984628091588)

    def test_SampleSizeKnownPop(self):
        result = SampleSizeKnownPop.sampleSize(3, self.testData)
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()