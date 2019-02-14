from counting_words.count_wordsmodule import count_words
import unittest

class TestCountWords(unittest.TestCase):
    def test_countwords_two(self):
        self.assertEqual(count_words('one two',{"one", "two"}), 2)

    def test_countwords_three(self):
        self.assertEqual(count_words('one two three',{"one", "two", "three"}), 3)    

if __name__ == '__main__':
    unittest.main()    