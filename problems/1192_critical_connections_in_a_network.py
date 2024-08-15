"""
https://leetcode.com/problems/critical-connections-in-a-network/description/

1192. Critical Connections in a Network

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
Return all critical connections in the network in any order.
"""


def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    adj: list[list[int]] = [[] for _ in range(n)]
    rank = [None] * n
    conn_set = set()
    for v, w in connections:
        adj[v].append(w)
        adj[w].append(v)
        conn_set.add((min(v, w), max(v, w)))
    dfs(adj, conn_set, 0, 0, rank)
    return [list(item) for item in conn_set]


def dfs(
    adj: list[list[int]],
    conns: set[tuple],
    node: int,
    discovery_time: int,
    rank: list[int],
) -> int:
    if rank[node]:
        return rank[node]
    rank[node] = discovery_time
    min_rank = discovery_time + 1
    for neighbor in adj[node]:
        if rank[neighbor] and rank[neighbor] == discovery_time - 1:
            continue
        recursive_rank = dfs(adj, conns, neighbor, discovery_time + 1, rank)
        if recursive_rank <= discovery_time:
            conns.discard((min(node, neighbor), max(node, neighbor)))
        min_rank = min(min_rank, recursive_rank)
    return min_rank


if __name__ == "__main__":
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(critical_connections(n, connections))
