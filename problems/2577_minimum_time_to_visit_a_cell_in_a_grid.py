"""
https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/

2577. Minimum Time to Visit a Cell in a Grid

You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.
"""

import heapq


def minimum_time(grid: list[list[int]]) -> int:
    if grid[0][1] > 1 and grid[1][0] > 1:
        return -1
    m, n = len(grid), len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    pq = [(grid[0][0], 0, 0)]
    while pq:
        time, row, col = heapq.heappop(pq)
        if row == m - 1 and col == n - 1:
            return time
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dx, dy in directions:
            next_row, next_col = row + dx, col + dy
            if not is_valid(m, n, visited, next_row, next_col):
                continue
            wait_time = 1 if (grid[next_row][next_col] - time) % 2 == 0 else 0
            next_time = max(wait_time + grid[next_row][next_col], time + 1)
            heapq.heappush(pq, (next_time, next_row, next_col))
    return -1


def is_valid(rows: int, cols: int, visited: set[tuple], i: int, j: int) -> bool:
    return 0 <= i < rows and 0 <= j < cols and (i, j) not in visited


if __name__ == "__main__":
    grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
    print(minimum_time(grid))
