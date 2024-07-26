"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
"""

import heapq


def find_city(n: int, edges: list[list[int]], distance_threshold: int) -> int:
    adj = [[] for _ in range(n)]
    for v, w, weight in edges:
        adj[v].append((w, weight))
        adj[w].append((v, weight))

    distances = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0

    for i in range(n):
        dijkstra(adj, distances[i], i)

    city = -1
    smallest = n
    for i in range(n):
        count = 0
        for j in range(n):
            if i == j or distances[i][j] > distance_threshold:
                continue
            count += 1
        if count <= smallest:
            smallest = count
            city = i
    return city


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


def floyd_warshall(n: int, edges: list[list[int]], distance_threshold: int) -> int:
    dist_matrix = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        dist_matrix[i][i] = 0
    for v, w, weight in edges:
        dist_matrix[v][w] = dist_matrix[w][v] = weight
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist_matrix[i][j] = min(
                    dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j]
                )
    city = -1
    smallest = n
    for i in range(n):
        count = 0
        for j in range(n):
            if i == j or dist_matrix[i][j] > distance_threshold:
                continue
            count += 1
        if count <= smallest:
            smallest = count
            city = i
    return city


if __name__ == "__main__":
    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    threshold = 4
    print(find_city(n, edges, threshold))
    print(floyd_warshall(n, edges, threshold))
