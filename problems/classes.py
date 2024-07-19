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
