"""
https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/

2976. Minimum Cost to Convert String I

You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].
You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
"""

import heapq


def minimum_cost(
    source: str, target: str, original: list[str], changed: list[str], cost: list[int]
) -> int:
    adj: list[list[tuple]] = [[] for _ in range(26)]
    for s, t, weight in zip(original, changed, cost):
        v, w = ord(s) - ord("a"), ord(t) - ord("a")
        adj[v].append((w, weight))

    dist_matrix = [[float("inf")] * 26 for _ in range(26)]
    for i in range(26):
        dist_matrix[i][i] = 0
    for i in range(26):
        dijkstra(adj, dist_matrix[i], i)

    total_cost = 0
    for s, t in zip(source, target):
        if s == t:
            continue
        v, w = ord(s) - ord("a"), ord(t) - ord("a")
        if dist_matrix[v][w] == float("inf"):
            return -1
        total_cost += dist_matrix[v][w]
    return total_cost


def dijkstra(adj: list[list[tuple]], dist_to: list[int], s: int) -> None:
    pq = [(0, s)]
    while pq:
        dist, v = heapq.heappop(pq)
        if dist > dist_to[v]:
            continue
        for w, weight in adj[v]:
            if dist_to[w] > dist_to[v] + weight:
                dist_to[w] = dist_to[v] + weight
                heapq.heappush(pq, (dist_to[w], w))


def floyd_warshall(
    source: str, target: str, original: list[str], changed: list[str], cost: list[int]
) -> int:
    dist_matrix = [[float("inf")] * 26 for _ in range(26)]
    for i in range(26):
        dist_matrix[i][i] = 0
    for s, t, weight in zip(original, changed, cost):
        v, w = ord(s) - ord("a"), ord(t) - ord("a")
        dist_matrix[v][w] = min(dist_matrix[v][w], weight)

    for k in range(26):
        for i in range(26):
            for j in range(26):
                dist_matrix[i][j] = min(
                    dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j]
                )

    total_cost = 0
    for s, t in zip(source, target):
        if s == t:
            continue
        v, w = ord(s) - ord("a"), ord(t) - ord("a")
        if dist_matrix[v][w] == float("inf"):
            return -1
        total_cost += dist_matrix[v][w]
    return total_cost


if __name__ == "__main__":
    source = "abcd"
    target = "acbe"
    original = ["a", "b", "c", "c", "e", "d"]
    changed = ["b", "c", "b", "e", "b", "e"]
    cost = [2, 5, 5, 1, 2, 20]
    print(minimum_cost(source, target, original, changed, cost))
    print(floyd_warshall(source, target, original, changed, cost))
