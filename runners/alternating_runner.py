from src.alternating_characters import alternatingCharacters

if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        print(alternatingCharacters(s))