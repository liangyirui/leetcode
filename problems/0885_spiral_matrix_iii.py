"""
https://leetcode.com/problems/spiral-matrix-iii/description/

885. Spiral Matrix III

You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
Return an array of coordinates representing the positions of the grid in the order you visited them.
"""


def spiral_matrix(rows: int, cols: int, r_start: int, c_start: int) -> list[list[int]]:
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    traversed = []
    step = 1
    direction = 0
    while len(traversed) < rows * cols:
        for _ in range(2):
            for _ in range(step):
                if r_start >= 0 and r_start < rows and c_start >= 0 and c_start < cols:
                    traversed.append([r_start, c_start])
                r_start += dirs[direction][0]
                c_start += dirs[direction][1]
            direction = (direction + 1) % 4
        step += 1
    return traversed


if __name__ == "__main__":
    rows = 5
    cols = 6
    r_start = 1
    c_start = 4
    print(spiral_matrix(rows, cols, r_start, c_start))
