from itertools import combinations


def is_valid(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True


def alternate(s: str) -> int:
    unique_chars = set(s)
    max_length = 0

    for c1, c2 in combinations(unique_chars, 2):
        filtered = [c for c in s if c == c1 or c == c2]
        candidate = "".join(filtered)

        if is_valid(candidate):
            max_length = max(max_length, len(candidate))

    return max_length


twoCharacters = alternate


if __name__ == "__main__":  # pragma: no cover
    print(alternate("beabeefeab"))