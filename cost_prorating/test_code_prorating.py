import unittest
from cost_prorating import CostProrating


class TestCostProrating(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = CostProrating()

    def test_prorate(self):
        result = self.instance.prorate(10, [5, 5])
        expected_result = [5, 5]

        self.assertListEqual(result, expected_result)

    def test_prorate_2(self):
        result = self.instance.prorate(10, [25, 75])
        expected_result = [3, 7]

        self.assertListEqual(result, expected_result)

    def test_prorate_3(self):
        result = self.instance.prorate(1550, [3, 1, 0, 2])
        expected_result = [775, 258, 0, 517]

        self.assertListEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()