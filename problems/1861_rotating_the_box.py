"""
https://leetcode.com/problems/rotating-the-box/description/

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.
"""

from _utils import print_matrix


def rotate_the_box(box: list[list[str]]) -> list[list[str]]:
    m = len(box)
    n = len(box[0])
    ret = [[""] * m for _ in range(n)]
    # transpose
    for i in range(n):
        for j in range(m):
            ret[i][j] = box[j][i]
    # reverse rows
    for i in range(n):
        ret[i].reverse()
    # apply gravity
    for col in range(m):
        empty_ptr = n - 1
        for row in range(n - 1, -1, -1):
            if ret[row][col] == "#":
                ret[row][col] = "."
                ret[empty_ptr][col] = "#"
                empty_ptr -= 1
            if ret[row][col] == "*":
                empty_ptr = row - 1
    return ret


if __name__ == "__main__":
    box = [
        ["#", "#", "*", ".", "*", "."],
        ["#", "#", "#", "*", ".", "."],
        ["#", "#", "#", ".", "#", "."],
    ]
    print_matrix(box)
    rotated = rotate_the_box(box)
    print_matrix(rotated)
