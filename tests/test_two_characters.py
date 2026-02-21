from src.two_characters import alternate

def test_valid_pair():
    assert alternate("beabeefeab") == 5

def test_no_valid_pair():
    assert alternate("aaaa") == 0

def test_single_char():
    assert alternate("a") == 0

def test_two_valid():
    assert alternate("ab") == 2

def test_invalid_alternation():
    assert alternate("aabb") == 0

def test_multiple_pairs():
    assert alternate("abcabcabc") >= 0