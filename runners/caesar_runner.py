from src.caesar_cipher import caesarCipher

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    print(caesarCipher(s, k))