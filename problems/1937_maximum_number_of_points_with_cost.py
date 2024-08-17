"""
https://leetcode.com/problems/maximum-number-of-points-with-cost/description/


1937. Maximum Number of Points with Cost

You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
Return the maximum number of points you can achieve.
"""


def max_points(points: list[list[int]]) -> int:
    m, n = len(points), len(points[0])
    prev = points[0]
    for row in range(1, m):
        curr = [0] * n
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = prev[0]
        for col in range(1, n):
            left_max[col] = max(prev[col], left_max[col - 1] - 1)

        right_max[-1] = prev[-1]
        for col in range(n - 2, -1, -1):
            right_max[col] = max(prev[col], right_max[col + 1] - 1)

        for col in range(n):
            curr[col] = points[row][col] + max(left_max[col], right_max[col])

        prev = curr

    return max(prev)


if __name__ == "__main__":
    points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    print(max_points(points))
