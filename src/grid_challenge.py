def gridChallenge(grid: list[str]) -> str:
    sorted_grid = []

    for row in grid:
        sorted_grid.append("".join(sorted(row)))

    for col in range(len(sorted_grid[0])):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"

    return "YES"


if __name__ == "__main__":  # pragma: no cover
    sample = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
    print(gridChallenge(sample))