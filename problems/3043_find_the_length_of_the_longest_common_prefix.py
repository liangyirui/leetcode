"""
https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/

You are given two arrays with positive integers arr1 and arr2.

A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.

A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.

You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.

Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.
"""

class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 10
        
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def insert(self, num: int) -> None:
        node = self.root
        num_str = str(num)
        for digit in num_str:
            idx = int(digit)
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
            
    def find_longest_prefix(self, num: int) -> int:
        node = self.root
        num_str = str(num)
        length = 0
        for digit in num_str:
            idx = int(digit)
            if node.children[idx]:
                length += 1
                node = node.children[idx]
            else:
                break
        return length
        
def longest_common_prefix(arr1: list[int], arr2: list[int]) -> int:
    trie = Trie()
    for num in arr1:
        trie.insert(num)
    longest_prefix = 0
    for num in arr2:
        longest_prefix = max(longest_prefix, trie.find_longest_prefix(num))
    return longest_prefix