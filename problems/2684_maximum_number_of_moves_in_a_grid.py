"""
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/

You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.
"""

def max_moves(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    prev = [1] * m  # use 1 to indicate the cell is reachable
    ans = 0
    for c in range(1, n):
        dp = [0] * m
        for r in range(m):
            if grid[r][c] > grid[r][c - 1] and prev[r] > 0:
                dp[r] = max(dp[r], prev[r] + 1)
            if r > 0 and grid[r][c] > grid[r - 1][c - 1] and prev[r - 1] > 0:
                dp[r] = max(dp[r], prev[r - 1] + 1)
            if r < m - 1 and grid[r][c] > grid[r + 1][c - 1] and prev[r + 1] > 0:
                dp[r] = max(dp[r], prev[r + 1] + 1)
            ans = max(ans, dp[r] - 1)
        prev = dp
    return ans