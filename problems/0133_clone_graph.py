"""
https://leetcode.com/problems/clone-graph/description/

133. Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list(list[Node]) of its neighbors.
"""

from collections import deque

from classes import GraphNode


def clone_graph(node: GraphNode | None) -> GraphNode | None:
    if node is None:
        return None
    node_copy = GraphNode(node.val)
    marked = [None] * 101
    dfs(node, node_copy, marked)
    return node_copy


def dfs(
    node: GraphNode | None, node_copy: GraphNode | None, marked: list[GraphNode]
) -> None:
    marked[node_copy.val] = node_copy
    for neighbor in node.neighbors:
        if marked[neighbor.val] is None:
            copy = GraphNode(neighbor.val)
            node_copy.neighbors.append(copy)
            dfs(neighbor, copy, marked)
        else:
            node_copy.neighbors.append(marked[neighbor.val])


def bsf(node: GraphNode | None) -> GraphNode | None:
    if node is None:
        return None
    node_map = {}
    node_copy = GraphNode(node.val)
    queue = deque([GraphNode])
    while queue:
        n = queue.popleft()
        for nei in n.neighbors:
            if nei not in node_map:
                nei_copy = GraphNode(nei.val)
                node_map[nei] = nei_copy
                queue.append(nei)
            node_map[n].neighbors.append(node_map[nei])
    return node_copy
