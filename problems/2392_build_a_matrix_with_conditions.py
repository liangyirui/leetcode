"""
https://leetcode.com/problems/build-a-matrix-with-conditions/description/

2392. Build a Matrix with Conditions

You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
"""

from collections import deque

from _utils import print_matrix


def build_matrix(
    k: int, row_conditions: list[list[int]], col_conditions: list[list[int]]
) -> list[list[int]]:
    ordered_rows = topological_sort_dfs(k, row_conditions)
    ordered_cols = topological_sort_dfs(k, col_conditions)
    if not ordered_rows or not ordered_cols:
        return []
    matrix = [[0] * k for _ in range(k)]
    row_index = {num: i for i, num in enumerate(ordered_rows)}
    col_index = {num: i for i, num in enumerate(ordered_cols)}
    for num in range(1, k + 1):
        if num in row_index and num in col_index:
            r, c = row_index[num], col_index[num]
            matrix[r][c] = num
    return matrix


def topological_sort_dfs(n: int, conditions: list[list[int]]) -> list[int]:
    """Postorder dfs, use on_stack array to detect if there is a cycle (backward edge)"""
    adj: list[list[int]] = [[] for _ in range(n + 1)]
    for v, w in conditions:
        adj[v].append(w)
    order = []
    marked = [False] * (n + 1)
    on_stack = [False] * (n + 1)
    for v in range(1, n + 1):
        if not dfs(adj, v, order, marked, on_stack):
            return []
    return order[::-1]


def dfs(
    adj: list[list[int]],
    v: int,
    order: list[int],
    marked: list[bool],
    on_stack: list[bool],
) -> bool:
    if on_stack[v]:
        return False
    if marked[v]:
        return True
    marked[v] = True
    on_stack[v] = True
    for w in adj[v]:
        if not dfs(adj, w, order, marked, on_stack):
            return False
    order.append(v)
    on_stack[v] = False
    return True


def topological_sort_bfs(n: int, conditions: list[list[int]]) -> list[int]:
    """Khan's Algorithm"""
    adj: list[list[int]] = [[] for _ in range(n + 1)]
    indegree: list[int] = [0] * (n + 1)
    for v, w in conditions:
        adj[v].append(w)
        indegree[w] += 1
    order = []
    queue = deque()
    for v in range(1, n + 1):
        if indegree[v] == 0:
            queue.append(v)
    while queue:
        v = queue.popleft()
        order.append(v)
        for w in adj[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    if len(order) != n:
        return []
    return order


if __name__ == "__main__":
    k = 3
    row_conditions = [[1, 2], [3, 2]]
    col_conditions = [[2, 1], [3, 2]]
    matrix = build_matrix(k, row_conditions, col_conditions)
    print_matrix(matrix)
