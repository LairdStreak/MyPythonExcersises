from counting_words import count_words
import pytest


def test_countwords():
    assert(count_words('one two',{"one", "two"}) == 2)