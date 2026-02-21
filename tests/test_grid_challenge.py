from src.grid_challenge import gridChallenge

def test_valid_grid():
    grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
    assert gridChallenge(grid) == "YES"

def test_invalid_grid():
    grid = ["mpxz", "abcd", "wlmf"]
    assert gridChallenge(grid) == "NO"

def test_single_cell():
    assert gridChallenge(["a"]) == "YES"

def test_single_row():
    assert gridChallenge(["cba"]) == "YES"

def test_sorted_rows_but_fail_column():
    grid = ["abc", "lmp", "qrt", "xyz"]
    assert gridChallenge(grid) == "YES"

def test_duplicate_letters():
    grid = ["aaa", "aaa", "aaa"]
    assert gridChallenge(grid) == "YES"