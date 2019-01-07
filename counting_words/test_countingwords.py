from counting_words.count_wordsmodule import count_words
import unittest

class TestCountWords(unittest.TestCase):
    def test_countwords(self):
        self.assertEqual(count_words('one two',{"one", "two"}),2)

if __name__ == '__main__':
    unittest.main()    