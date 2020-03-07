"""Tests the ept functions"""
import io
import unittest
from unittest.mock import MagicMock, patch
from eso_pledge_tracker import ept_functions

MOCKED_TIME = MagicMock(return_value=1582524000)


class TestHandleDate(unittest.TestCase):
    """Test the handle date method, where the current date is the beginning of the cycle"""
    @patch('time.time', MOCKED_TIME)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cycle_start(self, mock_stdout):
        ept_functions.handle_date(0, False)
        expected = "Today's Undaunted Pledges are: Fungal Grotto I, Selene's Web, and Moongrave Fane\n"
        self.assertEqual(expected, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
