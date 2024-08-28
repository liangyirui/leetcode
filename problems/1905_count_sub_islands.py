"""
https://leetcode.com/problems/count-sub-islands/description/

1905. Count Sub Islands

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.
"""


def count_sub_islands(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    m = len(grid1)
    n = len(grid1[0])
    marked = [[False] * n for _ in range(m)]
    count = 0
    # Prefill disqualified sub-islands
    for i in range(m):
        for j in range(n):
            if not marked[i][j] and grid1[i][j] == 0 and grid2[i][j] == 1:
                dfs(grid2, i, j, marked)

    # Count sub-islands
    for i in range(m):
        for j in range(n):
            if not marked[i][j] and grid2[i][j] == 1:
                dfs(grid2, i, j, marked)
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
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        dfs(grid, row + dx, col + dy, marked)


if __name__ == "__main__":
    grid1 = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
    ]
    grid2 = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    print(count_sub_islands(grid1, grid2))
