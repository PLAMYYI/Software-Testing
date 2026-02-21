def funnyString(s: str) -> str:
    n = len(s)

    for i in range(1, n):
        forward = abs(ord(s[i]) - ord(s[i - 1]))
        backward = abs(ord(s[n - i]) - ord(s[n - i - 1]))

        if forward != backward:
            return "Not Funny"

    return "Funny"


if __name__ == "__main__":  # pragma: no cover
    print(funnyString("acxz"))