#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import json

class JsonTests(unittest.TestCase):
    def test_basicJson(self):
        person = '{"name": "Bob", "languages": ["English", "Fench"]}'
        person_dict = json.loads(person)
        self.assertEqual(person_dict['languages'], ['English', 'Fench'])

if __name__ == '__main__':
    unittest.main()          