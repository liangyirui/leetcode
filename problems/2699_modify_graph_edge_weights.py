"""
https://leetcode.com/problems/modify-graph-edge-weights/description/

2699. Modify Graph Edge Weights

You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.
Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).
Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.
Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.
Note: You are not allowed to modify the weights of edges with initial positive weights.
"""

import heapq


def modified_graph_edges(
    n: int, edges: list[list[int]], source: int, destination: int, target: int
) -> list[list[int]]:
    INF = int(2e9)
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        if w == -1:
            continue
        adj[u].append((v, w))
        adj[v].append((u, w))

    curr_dist = dijkstra(adj, source, destination)
    if curr_dist < target:
        return []
    if curr_dist == target:
        for edge in edges:
            if edge[2] == -1:
                edge[2] = INF
        return edges

    for i, (u, v, w) in enumerate(edges):
        if w != -1:
            continue
        edges[i][2] = 1
        adj[u].append((v, 1))
        adj[v].append((w, 1))
        new_dist = dijkstra(adj, source, destination)
        if new_dist <= target:
            edges[i][2] += target - new_dist
            for j in range(i + 1, len(edges)):
                if edges[j][2] == -1:
                    edges[j][2] = INF
            return edges

    return []


def dijkstra(adj: list[list[int]], src: int, dst: int) -> int:
    dist_to = [float("inf")] * len(adj)
    dist_to[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_to[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist_to[v]:
                dist_to[v] = d + w
                heapq.heappush(pq, (dist_to[v], v))
    return dist_to[dst]


if __name__ == "__main__":
    n = 5
    edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
    source = 0
    destination = 1
    target = 5
    print(modified_graph_edges(n, edges, source, destination, target))
