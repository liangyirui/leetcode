"""
https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/

2192. All Ancestors of a Node in a Directed Acyclic Graph

You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
A node u is an ancestor of another node v if u can reach v via a set of edges.
"""

from collections import deque


def get_ancestors(n: int, edges: list[list[int]]) -> list[list[int]]:
    adj: list[list[int]] = [[] for _ in range(n)]
    ancestors: list[list[int]] = [[] for _ in range(n)]
    for v, w in edges:
        adj[v].append(w)
    for v in range(n):
        dfs(adj, v, v, ancestors)
    return ancestors


def dfs(
    adj: list[list[int]], ancestor: int, curr: int, ancestors: list[list[int]]
) -> None:
    for child in adj[curr]:
        if ancestors[child] and ancestors[child][-1] == ancestor:
            continue
        ancestors[child].append(ancestor)
        dfs(adj, ancestor, child, ancestors)


def bfs(n: int, edges: list[list[int]]) -> list[list[int]]:
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for v, w in edges:
        adj[v].append(w)
        indegree[w] += 1
    queue = deque([i for i in range(n) if indegree[i] == 0])
    topological_order = []
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    ancestors = [[] for _ in range(n)]
    ancestors_set_list = [set() for _ in range(n)]
    for node in topological_order:
        for nei in adj[node]:
            ancestors_set_list[nei].add(node)
            ancestors_set_list[nei].update(ancestors_set_list[node])

    for v in range(n):
        ancestors[v].extend(ancestors_set_list[v])
        ancestors[v].sort()

    return ancestors


if __name__ == "__main__":
    n = 8
    edges = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    print(get_ancestors(n, edges))
    print(bfs(n, edges))
