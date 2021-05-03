import unittest
from water_jugs import WaterJugs


class TestWaterJugs(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = WaterJugs()

    def test_find_sequence(self):
        result = self.instance.find_sequence(2, [4, 3, 3, 2])
        expected_result = [[0, 0, 0, 0], [4, 0, 0, 0], [4, 3, 0, 0], [4, 3, 3, 0], [4, 3, 3, 2]]

        self.assertListEqual(result, expected_result)

    def test_die_hard(self):
        result = self.instance.find_sequence(4, [3, 5])
        expected_result = [[0, 0], [3, 0], [3, 5], [0, 5], [3, 2], [0, 2], [2, 0], [2, 5], [3, 4]]

        self.assertListEqual(result, expected_result)

    def test_None(self):
        result = self.instance.find_sequence(7, [3, 5])

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()