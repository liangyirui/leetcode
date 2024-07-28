"""
https://leetcode.com/problems/second-minimum-time-to-reach-destination/description/

2045. Second Minimum Time to Reach Destination

A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.
Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.
The second minimum value is defined as the smallest value strictly larger than the minimum value.
For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:
You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
"""

from collections import deque


def second_minimum(n: int, edges: list[list[int]], time: int, change: int) -> int:
    adj = [[] for _ in range(n + 1)]
    for v, w in edges:
        adj[v].append(w)
        adj[w].append(v)
    dist1 = [-1] * (n + 1)
    dist2 = [-1] * (n + 1)
    queue = deque([(1, 1)])
    dist1[1] = 0
    while queue:
        v, freq = queue.popleft()
        time_taken = dist1[v] if freq == 1 else dist2[v]
        if (time_taken // change) % 2 == 1:
            time_taken = change * (time_taken // change + 1) + time
        else:
            time_taken += time
        if not adj[v]:
            continue
        for w in adj[v]:
            if dist1[w] == -1:
                dist1[w] = time_taken
                queue.append((w, 1))
            elif dist2[w] == -1 and dist1[w] != time_taken:
                if w == n:
                    return time_taken
                dist2[w] = time_taken
                queue.append((w, 2))
    return 0


if __name__ == "__main__":
    n = 2
    edges = [[1, 2]]
    time = 3
    change = 2
    print(second_minimum(n, edges, time, change))
