"""
https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/

1605. Find Valid Matrix Given Row and Column Sums

You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.
Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.
Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
"""

from utils import print_matrix


def restore_matrix(row_sum: list[int], col_sum: list[int]) -> list[list[int]]:
    m, n = len(row_sum), len(col_sum)
    mat = [[0] * n for _ in range(m)]
    i = j = 0
    while i < m and j < n:
        mat[i][j] = min(row_sum[i], col_sum[j])
        row_sum[i] -= mat[i][j]
        col_sum[j] -= mat[i][j]
        if row_sum[i] == 0:
            i += 1
        else:
            j += 1
    return mat


if __name__ == "__main__":
    row_sum = [5, 7, 10]
    col_sum = [8, 6, 8]
    print(f"row sum: {row_sum}")
    print(f"col sum: {col_sum}")
    mat = restore_matrix(row_sum, col_sum)
    print_matrix(mat)
