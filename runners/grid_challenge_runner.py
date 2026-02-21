from src.grid_challenge import gridChallenge

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid.append(input().strip())
        print(gridChallenge(grid))