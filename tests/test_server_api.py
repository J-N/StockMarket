#!/usr/bin/env python

"""
Unit tests for the Stock Market Server API.
"""
import unittest

def fun(x):
    return x + 1

class TestServerAPI(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main()
