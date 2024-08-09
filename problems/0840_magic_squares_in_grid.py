"""
https://leetcode.com/problems/magic-squares-in-grid/description/

840. Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
"""


def num_magic_squares_inside(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    for row in range(m - 2):
        for col in range(n - 2):
            if is_magic_square_eager(grid, row, col):
                count += 1
    return count


def is_magic_square(grid: list[list[int]], row: int, col: int) -> bool:
    marked = [False] * 10
    for i in range(3):
        for j in range(3):
            num = grid[row + i][col + j]
            if num < 1 or num > 9:
                return False
            if marked[num]:
                return False
            marked[num] = True

    diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
    diagonal2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
    if diagonal1 != diagonal2:
        return False

    row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
    row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
    row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
    if not (row1 == row2 and row1 == row3 and row1 == row3):
        return False

    col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
    col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
    col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
    if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
        return False

    return True


def is_magic_square_eager(grid: list[list[int]], row: int, col: int) -> bool:
    sequence = "2943816729438167"
    sequence_reversed = sequence[::-1]
    border = []
    indices = [0, 1, 2, 5, 8, 7, 6, 3]
    for i in indices:
        num = grid[row + i // 3][col + (i % 3)]
        border.append(str(num))
    border_string = "".join(border)
    return (
        grid[row][col] % 2 == 0
        and grid[row + 1][col + 1] == 5
        and (
            sequence.find(border_string) != -1
            or sequence_reversed.find(border_string) != -1
        )
    )


if __name__ == "__main__":
    grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
    print(num_magic_squares_inside(grid))
