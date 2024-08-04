"""
https://leetcode.com/problems/bus-routes/description/

815. Bus Routes

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.
Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""

from collections import defaultdict, deque


def num_buses_to_destination(routes: list[list[int]], source: int, target: int) -> int:
    if source == target:
        return 0
    adj = defaultdict(list)
    for bus_number, route in enumerate(routes):
        for stop in route:
            adj[stop].append(bus_number)
    queue = deque()
    visited = set()
    for bus_number in adj[source]:
        queue.append(bus_number)
        visited.add(bus_number)
    count = 1
    while queue:
        size = len(queue)
        for _ in range(size):
            bus = queue.popleft()
            for stop in routes[bus]:
                if stop == target:
                    return count
                for next_bus in adj[stop]:
                    if next_bus in visited:
                        continue
                    queue.append(next_bus)
                    visited.add(next_bus)
        count += 1
    return -1


if __name__ == "__main__":
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6
    print(num_buses_to_destination(routes, source, target))
