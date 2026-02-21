from src.funny_string import funnyString

if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(funnyString(s))