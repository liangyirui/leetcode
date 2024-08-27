"""
https://leetcode.com/problems/path-with-maximum-probability/description/

1514. Path with Maximum Probability
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
"""

import heapq


def max_probability(
    n: int,
    edges: list[list[int]],
    succ_prob: list[float],
    start_node: int,
    end_node: int,
) -> float:
    adj = [[] for _ in range(n)]
    for (v, w), prob in zip(edges, succ_prob):
        adj[v].append((w, prob))
        adj[w].append((v, prob))
    max_prob = [0] * n
    max_prob[start_node] = 1.0
    pq = [(-1.0, start_node)]
    while pq:
        curr_prob, curr_node = heapq.heappop(pq)
        if curr_node == end_node:
            return -curr_prob
        for next_node, path_prob in adj[curr_node]:
            if -curr_prob * path_prob > max_prob[next_node]:
                max_prob[next_node] = -curr_prob * path_prob
                heapq.heappush(pq, (-max_prob[next_node], next_node))
    return 0.0


if __name__ == "__main__":
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succ_prob = [0.5, 0.5, 0.2]
    start_node = 0
    end_node = 2
    print(max_probability(n, edges, succ_prob, start_node, end_node))
