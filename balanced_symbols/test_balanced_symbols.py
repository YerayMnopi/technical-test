import unittest
from balanced_symbols import BalancedSymbols


class TestBalancedSymbols(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = BalancedSymbols()

    def test_none(self):
        result = self.instance.check_str_is_balanced(None)

        self.assertTrue(result)

    def test_empty(self):
        result = self.instance.check_str_is_balanced('')

        self.assertTrue(result)

    def test_balanced(self):
        string_to_check = '( { [ () [] ] } )'

        result = self.instance.check_str_is_balanced(string_to_check)

        self.assertTrue(result)

    def test_unbalanced(self):
        string_to_check = '( ]'

        result = self.instance.check_str_is_balanced(string_to_check)

        self.assertFalse(result)

    def test_second_unbalanced_example(self):
        string_to_check = '( [ ) ]'

        result = self.instance.check_str_is_balanced(string_to_check)

        self.assertFalse(result)

    def test_str_with_comment(self):
        string_to_check = '/* abcd( /* ]efgh */ ijkl */'

        result = self.instance.check_str_is_balanced(string_to_check)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()