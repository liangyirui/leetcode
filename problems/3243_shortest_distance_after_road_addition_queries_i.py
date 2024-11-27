"""
https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/

You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.
"""

from collections import deque


def shortest_distance_after_queries(n: int, queries: list[list[int]]) -> list[int]:
    # create adjacency list to represent vertices and edges
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        adj[i].append(i + 1)
    dist = []
    for u, v in queries:
        adj[u].append(v)
        dist.append(bfs(adj, 0, n - 1))
    return dist


def bfs(adj: list[list[int]], src: int, dst: int) -> int:
    n = len(adj)
    marked = [False] * n
    marked[src] = True
    queue = deque([0])
    steps = 0
    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()
            if v == dst:
                return steps
            for w in adj[v]:
                if marked[w]:
                    continue
                marked[w] = True
                queue.append(w)
        steps += 1
    return -1


if __name__ == "__main__":
    n = 5
    queries = [[2, 4], [0, 2], [0, 4]]
    print(shortest_distance_after_queries(n, queries))
