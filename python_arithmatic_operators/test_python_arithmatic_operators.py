#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from python_arithmatic_operators import arithmatic_operators as ao

class Arithmatic_operators_Tests(unittest.TestCase):

    def test_add_two_numbers(self):
        result = ao.add_two_numbers(1,1)
        self.assertEqual(result,2)

    def test_multiply_two_numbers(self):
        result = ao.multiply_two_numbers(2,2)
        self.assertEqual(result,4)

    def test_modulus_two_numbers(self):
        result = ao.modulus_two_numbers(22,8)
        self.assertEqual(result,6)

if __name__ == '__main__':
    unittest.main()
