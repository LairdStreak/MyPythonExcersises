#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from python_switchcase.main_module import get_car_color

class SCaseTests(unittest.TestCase):
    def test_carcolor_get(self):
        red = 'red'
        self.assertEqual(get_car_color('volvo'), red)

if __name__ == '__main__':
    unittest.main()        
