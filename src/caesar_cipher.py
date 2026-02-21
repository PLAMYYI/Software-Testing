def caesarCipher(s: str, k: int) -> str:
    result = ""
    k = k % 26

    for char in s:
        if char.islower():
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result += shifted
        elif char.isupper():
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result += shifted
        else:
            result += char

    return result


if __name__ == "__main__":  # pragma: no cover
    print(caesarCipher("abc", 2))