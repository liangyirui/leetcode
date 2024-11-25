"""
https://leetcode.com/problems/maximum-matrix-sum/description/

You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
"""


def max_matrix_sum(matrix: list[list[int]]) -> int:
    total_sum = 0
    min_abs = 100001
    negative_count = 0
    for row in matrix:
        for val in row:
            total_sum += abs(val)
            min_abs = min(min_abs, abs(val))
            negative_count += val < 0
    if negative_count % 2 != 0:
        total_sum -= 2 * min_abs
    return total_sum


if __name__ == "__main__":
    matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
    print(max_matrix_sum(matrix))
