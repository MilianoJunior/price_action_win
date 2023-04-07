# -*- coding: utf-8 -*-
import unittest
from is_pin_bar import is_pin_bar
import pandas as pd

class TestIsPinBar(unittest.TestCase):
    def test_is_pin_bar(self):
        data = {
            'Open': [1.0, 1.1, 1.2, 1.15, 1.25],
            'High': [1.2, 1.3, 1.4, 1.35, 1.45],
            'Low': [0.9, 1.0, 1.1, 0.95, 1.05],
            'Close': [1.1, 1.2, 1.1, 1.25, 1.15]
        }

        df = pd.DataFrame(data)

        self.assertEqual(is_pin_bar(df.iloc[0]), False)
        self.assertEqual(is_pin_bar(df.iloc[1]), False)
        self.assertEqual(is_pin_bar(df.iloc[2]), 'bearish')
        self.assertEqual(is_pin_bar(df.iloc[3]), False)
        self.assertEqual(is_pin_bar(df.iloc[4]), False)

if __name__ == '__main__':
    unittest.main()
