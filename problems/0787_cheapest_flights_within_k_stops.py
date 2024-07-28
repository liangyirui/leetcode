"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
"""


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


if __name__ == "__main__":
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(find_cheapest_price(n, flights, src, dst, k))
