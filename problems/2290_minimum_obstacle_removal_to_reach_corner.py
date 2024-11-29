"""
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/

2290. Minimum Obstacle Remval to Reach Corner

You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

1. 0 represents an empty cell,
2. 1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.
Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
"""

import heapq
from collections import deque


def minimum_obstacles(grid: list[list[int]]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    m, n = len(grid), len(grid[0])
    dist = [[float("inf")] * n for _ in range(m)]
    dist[0][0] = grid[0][0]
    pq = deque([(0, 0, 0)])
    while pq:
        obstacles, row, col = pq.popleft()
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if not in_range(grid, new_row, new_col):
                continue
            if dist[new_row][new_col] != float("inf"):
                continue
            if grid[new_row][new_col] == 0:
                pq.appendleft((obstacles, new_row, new_col))
                dist[new_row][new_col] = obstacles
            else:
                pq.append((obstacles + 1, new_row, new_col))
                dist[new_row][new_col] = obstacles + 1
    return dist[m - 1][n - 1]


def djikstra(grid: list[list[int]]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    m, n = len(grid), len(grid[0])
    dist = [[float("inf")] * n for _ in range(m)]
    dist[0][0] = grid[0][0]
    pq = [(dist[0][0], 0, 0)]
    while pq:
        obstacles, row, col = heapq.heappop(pq)
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if new_row == m - 1 and new_col == n - 1:
                return obstacles
            if not in_range(grid, new_row, new_col):
                continue
            new_obstacles = obstacles + grid[new_row][new_col]
            if new_obstacles < dist[new_row][new_col]:
                dist[new_row][new_col] = new_obstacles
                heapq.heappush(pq, (new_obstacles, new_row, new_col))
    return dist[m - 1][n - 1]


def in_range(grid: list[list[int]], i: int, j: int) -> bool:
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])


if __name__ == "__main__":
    grid = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
    print(minimum_obstacles(grid))
    print(djikstra(grid))
