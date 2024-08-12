"""
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/

1568. Minimum Number of Days to Disconnect Island

You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
In one day, we are allowed to change any single land cell (1) into a water cell (0).
Return the minimum number of days to disconnect the grid.
"""


def min_days(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = count_islands(grid)
    if count > 1:
        return 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 0:
                continue
            grid[row][col] = 0
            new_count = count_islands(grid)
            if new_count > 1:
                return 1
            grid[row][col] = 1
    return 2


def count_islands(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    marked = [[False] * n for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if not marked[row][col] and grid[row][col] == 1:
                dfs(grid, row, col, marked)
                count += 1
    return count


def dfs(grid: list[list[int]], row: int, col: int, marked: list[list[bool]]) -> None:
    if (
        row < 0
        or row == len(grid)
        or col < 0
        or col == len(grid[0])
        or marked[row][col]
        or grid[row][col] == 0
    ):
        return
    marked[row][col] = True
    dfs(grid, row + 1, col, marked)
    dfs(grid, row, col + 1, marked)
    dfs(grid, row - 1, col, marked)
    dfs(grid, row, col - 1, marked)


if __name__ == "__main__":
    grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(min_days(grid))
