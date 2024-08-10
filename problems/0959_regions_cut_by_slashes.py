"""
https://leetcode.com/problems/regions-cut-by-slashes/description/

959. Regions Cut by Slashes

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
Given the grid grid represented as a string array, return the number of regions.
Note that backslash characters are escaped, so a '\' is represented as '\\'.
"""


def regions_by_slashes(grid: list[str]) -> int:
    n = len(grid)
    expanded = [[0] * 3 * n for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "/":
                expanded[3 * i + 2][3 * j] = expanded[3 * i + 1][3 * j + 1] = expanded[
                    3 * i
                ][3 * j + 2] = 1
            elif grid[i][j] == "\\":
                expanded[3 * i][3 * j] = expanded[3 * i + 1][3 * j + 1] = expanded[
                    3 * i + 2
                ][3 * j + 2] = 1

    count = 0
    for i in range(3 * n):
        for j in range(3 * n):
            if expanded[i][j] == 0:
                dfs(expanded, i, j)
                count += 1
    return count


def dfs(grid: list[list[int]], i: int, j: int):
    if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] != 0:
        return
    grid[i][j] = 1
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)


if __name__ == "__main__":
    grid = ["/\\", "\\/"]
    print(regions_by_slashes(grid))
