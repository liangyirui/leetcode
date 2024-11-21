"""
https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
Return the number of unoccupied cells that are not guarded.
"""


def count_unguarded(
    m: int, n: int, guards: list[list[int]], walls: list[list[int]]
) -> int:
    mat = [[0] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i, j in guards:
        mat[i][j] = 1
    for i, j in walls:
        mat[i][j] = 1
    for i, j in guards:
        for dx, dy in directions:
            curr_x, curr_y = i, j
            while (
                0 <= curr_x + dx < m
                and 0 <= curr_y + dy < n
                and mat[curr_x + dx][curr_y + dy] != 1
            ):
                curr_x += dx
                curr_y += dy
                mat[curr_x][curr_y] = 2
    count = 0
    for i in range(m):
        for j in range(n):
            count += mat[i][j] == 0
    return count


if __name__ == "__main__":
    m = 3
    n = 3
    guards = [[1, 1]]
    walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
    print(count_unguarded(m, n, guards, walls))
