# -*- coding: utf-8 -*-
import unittest
from Inheritance.inheritancebasics import Wizard

class InheritanceTest(unittest.TestCase):
    def test_wizard(self):
        w = Wizard("Tom", 666, 130, 100)
        self.assertEqual(w.name, 'Tom')

if __name__ == '__main__':
    unittest.main()        