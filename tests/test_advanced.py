# -*- coding: utf-8 -*-

from context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        # important to remember that '__init__' of pkg 'sample' actually
        # imported the 'hmm' method from 'core.py', otherwise it would not work
        # because 'context.py' module has only 'sample' in its namespace, but
        # does not have anly of the modules in 'sample' into its local
        # namespace
        self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()
