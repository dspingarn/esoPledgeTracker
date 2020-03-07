"""Test the ability of the argument parser to make the correct method calls"""
import unittest
from unittest.mock import patch
from eso_pledge_tracker import ept


class TestParser(unittest.TestCase):
    @patch('eso_pledge_tracker.ept.handle_date')
    @patch('sys.argv', ['ept'])
    def test_default(self, mock_handle_date):
        ept.main()
        mock_handle_date.assert_called_once_with(0, False)

    @patch('eso_pledge_tracker.ept.handle_date')
    @patch('sys.argv', ['ept', '-d', '1', '-v'])
    def test_date_and_verbose(self, mock_handle_date):
        ept.main()
        mock_handle_date.assert_called_once_with(1, True)

    @patch('eso_pledge_tracker.ept.handle_list')
    @patch('sys.argv', ['ept', '-l'])
    def test_list(self, mock_handle_list):
        ept.main()
        mock_handle_list.assert_called_once_with(False)

    @patch('eso_pledge_tracker.ept.handle_list')
    @patch('sys.argv', ['ept', '-lv'])
    def test_list_and_verbose(self, mock_handle_list):
        ept.main()
        mock_handle_list.assert_called_once_with(True)

    @patch('eso_pledge_tracker.ept.handle_next')
    @patch('sys.argv', ['ept', '-n', 'ebon'])
    def test_next(self, mock_handle_next):
        ept.main()
        mock_handle_next.assert_called_once_with('ebon', False)


if __name__ == '__main__':
    unittest.main()
