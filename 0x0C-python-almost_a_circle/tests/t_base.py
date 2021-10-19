#!/usr/bin/python3
"""files, classes and methods"""
import unittest
from models.base import Base


class BTests(unittest.BTests):
    """must be unit tested"""

    def B_Tests(self):
        """test method"""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def B2_Tests(self):
        """test method"""
        b = Base(2)
        self.assertEqual(b.id, 2)

if __name__ == "__main__":
    unittest.main()
