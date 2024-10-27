"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""

def count_squares(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                continue
            dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i][j])
            count += dp[i + 1][j + 1]
    return count