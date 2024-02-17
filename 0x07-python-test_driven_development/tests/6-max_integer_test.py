#!/usr/bin/python3
"""
    This is a python script and test a python file
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestingMaxInteger(unittest.TestCase):


    "run the test with python3 -m unittest -v tests.6-max_integer_test"""

    def test_module_doctring(self):
        moduleDc = __import__('6-max_integer').__doc__
        self.assertTrue(len(noduleDoc) > 1)

    def test_function_doctstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_signed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

