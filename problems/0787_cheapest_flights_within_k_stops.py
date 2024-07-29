"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
"""

import heapq
from collections import deque


def find_cheapest_price(
    n: int, flights: list[list[int]], src: int, dst: int, k: int
) -> int:
    dist_to = [float("inf")] * n
    dist_to[src] = 0
    for _ in range(k + 1):
        temp = dist_to[:]
        for v, w, price in flights:
            if dist_to[v] == float("inf"):
                continue
            temp[w] = min(temp[w], dist_to[v] + price)
        dist_to = temp
    return dist_to[dst] if dist_to[dst] != float("inf") else -1


def bfs(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    adj: list[list[tuple]] = [[] for _ in range(n)]
    for v, w, price in flights:
        adj[v].append((w, price))
    dist = [float("inf")] * n
    dist[src] = 0
    queue = deque([(src, 0)])
    stops = 0
    while queue and stops <= k:
        size = len(queue)
        for _ in range(size):
            v, cost = queue.popleft()
            if not adj[v]:
                continue
            for w, price in adj[v]:
                if dist[w] > cost + price:
                    dist[w] = cost + price
                    queue.append((w, dist[w]))
        stops += 1
    return -1 if dist[dst] == float("inf") else dist[dst]


def dijkstra(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    adj: list[list[tuple]] = [[] for _ in range(n)]
    for v, w, price in flights:
        adj[v].append((w, price))
    visited = {}
    pq = [(0, 0, src)]
    while pq:
        cost, stops, node = heapq.heappop(pq)
        if node == dst and stops <= k + 1:
            return cost
        if node not in visited or visited[node] > stops:
            visited[node] = stops
            for nei, price in adj[node]:
                heapq.heappush(pq, (cost + price, stops + 1, nei))
    return -1


if __name__ == "__main__":
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(find_cheapest_price(n, flights, src, dst, k))
    print(bfs(n, flights, src, dst, k))
    print(dijkstra(n, flights, src, dst, k))
