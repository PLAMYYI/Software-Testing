from src.caesar_cipher import caesarCipher

# lowercase
def test_lowercase_shift():
    assert caesarCipher("abc", 2) == "cde"

# uppercase
def test_uppercase_shift():
    assert caesarCipher("ABC", 2) == "CDE"

# wrap around
def test_wrap_around():
    assert caesarCipher("xyz", 3) == "abc"

# mixed
def test_mixed():
    assert caesarCipher("AbC", 1) == "BcD"

# symbols
def test_symbols():
    assert caesarCipher("abc-123", 2) == "cde-123"

# zero shift
def test_zero_shift():
    assert caesarCipher("abc", 0) == "abc"

# large shift
def test_large_shift():
    assert caesarCipher("abc", 1000) == caesarCipher("abc", 1000 % 26)

# empty string
def test_empty():
    assert caesarCipher("", 5) == ""