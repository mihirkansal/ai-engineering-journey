def grid_size(grid):
    total = 1
    for v in grid.values():
        total = total * len(v)
    return total

if __name__ == "__main__":
    print(grid_size({"lr": [0.01, 0.1, 1.0], "depth": [3, 5]}))
    print(grid_size({"a": [1, 2, 3, 4, 5]}))
    print(grid_size({k: [1, 2, 3, 4, 5] for k in "abcdef"}))
    print(grid_size({}))
