"""
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/

You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.
"""

from collections import defaultdict


def max_equal_rows_after_flips(matrix: list[list[int]]) -> int:
    pattern = defaultdict(int)
    max_count = 0
    for row in matrix:
        key = build_key(row)
        pattern[key] += 1
        max_count = max(max_count, pattern[key])
    return max_count


def build_key(arr: list[int]) -> str:
    n = len(arr)
    sb = ["T"]
    for i in range(1, n):
        if arr[i] == arr[0]:
            sb.append("T")
        else:
            sb.append("F")
    return "".join(sb)


if __name__ == "__main__":
    matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
    print(max_equal_rows_after_flips(matrix))
