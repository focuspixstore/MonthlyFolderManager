import unittest
from unittest.mock import patch
from MonthlyFolderManager import ask

class TestAskFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['y'])
    def test_ask_y(self, mock_input):
        result = ask("Confirm? [y/n]: ", ['y', 'n'])
        self.assertEqual(result, 'y')

    @patch('builtins.input', side_effect=['yes'])
    def test_ask_word_yes_alias(self, mock_input):
        result = ask("Confirm? [y/n]: ", ['y', 'n'])
        self.assertEqual(result, 'y')

    @patch('builtins.input', side_effect=['NO'])
    def test_ask_word_no_alias_uppercase(self, mock_input):
        result = ask("Confirm? [y/n]: ", ['y', 'n'])
        self.assertEqual(result, 'n')

    @patch('builtins.input', side_effect=[''])
    def test_ask_default_fallback(self, mock_input):
        result = ask("Confirm? [Y/n]: ", ['y', 'n'], default='y')
        self.assertEqual(result, 'y')

    @patch('builtins.input', side_effect=['invalid', 'yes'])
    def test_ask_invalid_then_valid(self, mock_input):
        result = ask("Confirm? [y/n]: ", ['y', 'n'])
        self.assertEqual(result, 'y')

if __name__ == '__main__':
    unittest.main()
