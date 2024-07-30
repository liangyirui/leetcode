from typing import Self


class ListNode:
    """ListNode class for linked list"""

    def __init__(self, val: int = 0, next: Self | None = None) -> None:
        self.val = val
        self.next = next


class TreeNode:
    """TreeNode class for binary tree"""

    def __init__(
        self, val: int = 0, left: Self | None = None, right: Self | None = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Trie:
    class TrieNode:
        """TrieNode class for ASCII trie"""

        def __init__(self, val: bool = False) -> None:
            self.val = val
            self.children = [None] * 256

    def __init__(self) -> None:
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if node.children[ord(ch)] is None:
                node.children[ord(ch)] = self.TrieNode()
            node = node.children[ord(ch)]
        node.val = True


class GraphNode:
    """Definition of graph node"""

    def __init__(self, val: int = 0, neighbors: list[Self] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class UF:
    """Union Find with path compression"""

    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.components = n

    def find(self, p: int) -> int:
        if self.parent[p] == p:
            return p
        # path compression
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        p, q = self.find(p), self.find(q)
        if p == q:
            return False
        if self.size[q] > self.size[p]:
            self.parent[p] = q
            self.size[q] += self.size[p]
        else:
            self.parent[q] = p
            self.size[p] += self.size[q]
        self.components -= 1
        return True


class BIT:
    def __init__(self, n: int) -> None:
        self.tree = [0] * (n + 1)
        self.n = n

    def update(self, idx: int, val: int) -> None:
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & (-idx)

    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & (-idx)
        return res
