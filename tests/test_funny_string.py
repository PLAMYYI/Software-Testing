import pytest
from src.funny_string import funnyString

# Normal cases
def test_funny_basic():
    assert funnyString("acxz") == "Funny"

def test_not_funny_basic():
    assert funnyString("bcxz") == "Not Funny"

# Edge cases
def test_single_char():
    assert funnyString("a") == "Funny"

def test_two_chars_equal():
    assert funnyString("aa") == "Funny"

def test_two_chars_different():
    assert funnyString("ab") == "Funny"

# Repeated pattern
def test_repeated_chars():
    assert funnyString("aaaa") == "Funny"

# Large input
def test_long_string():
    s = "abcdefghijklmnopqrstuvwxyz"
    assert funnyString(s) == "Funny"