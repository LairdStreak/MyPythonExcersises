#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class ListTests(unittest.TestCase):
    def test_list_length(self):
        numbers = [4, 5, 10, 20, 34]
        self.assertEqual(numbers.__len__(), 5)

if __name__ == '__main__':
    unittest.main()        
