from src.alternating_characters import alternatingCharacters

def test_no_deletion():
    assert alternatingCharacters("ABABAB") == 0

def test_all_same():
    assert alternatingCharacters("AAAA") == 3

def test_partial_duplicates():
    assert alternatingCharacters("AABAAB") == 2

def test_single_char():
    assert alternatingCharacters("A") == 0

def test_empty_string():
    assert alternatingCharacters("") == 0

def test_two_same():
    assert alternatingCharacters("AA") == 1

def test_two_diff():
    assert alternatingCharacters("AB") == 0