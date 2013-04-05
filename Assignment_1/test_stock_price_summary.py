from a1 import *
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_empty_stock_list(self):
        """
        Test for list with no data
        """
        L = []
        gain, loose = stock_price_summary(L)
        expected_gain = expected_loose = 0
        self.assertEqual(gain, expected_gain)
        self.assertEqual(loose, expected_loose)

    def test_no_gain_list(self):
        """
        Test for list without gains (looses or 0 only)
        """
        L = [0, -0.25, -0.1, 0, 0, -5]
        gain, loose = stock_price_summary(L)
        expected_gain = 0
        expected_loose = -5.35
        self.assertEqual(gain, expected_gain)
        self.assertEqual(loose, expected_loose)

    def test_no_loose_list(self):
        """
        Test for list without looses (gains or 0 only)
        """
        L = [0, 0.25, 0.1, 0, 0, 5]
        gain, loose = stock_price_summary(L)
        expected_gain = 5.35
        expected_loose = 0
        self.assertEqual(gain, expected_gain)
        self.assertEqual(loose, expected_loose)

    def test_no_gain_no_loose_list(self):
        """
        Test for list without looses and gains
        """
        L = [0, 0, 0, 0, 0, 0]
        gain, loose = stock_price_summary(L)
        expected_gain = 0
        expected_loose = 0
        self.assertEqual(gain, expected_gain)
        self.assertEqual(loose, expected_loose)

    def test_gains_looses_list(self):
        """
        Test for list with gains and looses
        """
        L = [-2.4, 0, -1, 0.25, 0.1, 0, 0, -1.645, 5]
        gain, loose = stock_price_summary(L)
        expected_gain = 5.35
        expected_loose = -5.045
        self.assertEqual(gain, expected_gain)
        self.assertEqual(loose, expected_loose)


if __name__ == '__main__':
    unittest.main() 
# I remove exit=False because my Python doesn't "like it" (I use Python 2.6)
# with exit=False I have a TypeError: __init__() got an unexpected keyword argument 'exit'
