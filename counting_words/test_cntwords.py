import pytest
from counting_words.count_wordsmodule import count_words

def test_countwords_two():
    assert count_words('one two',{"one", "two"}) == 2

def test_countwords_three():
    assert count_words('one two three',{"one", "two", "three"}) == 3