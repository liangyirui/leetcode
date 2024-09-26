"""
https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

You are given an array words of size n consisting of non-empty strings.

We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].

For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

Note that a string is considered as a prefix of itself.
"""

class TrieNode:
    def __init__(self) -> None:
        self.val = 0
        self.children = [None] * 26
        
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node.children[idx].val += 1
            node = node.children[idx]
            
    def get_score(self, word: str) -> int:
        node = self.root
        score = 0
        for ch in word:
            idx = ord(ch) - ord('a')
            score += node.children[idx]
            node = node.children[idx]
    	return score
        

def sum_prefix_scores(self, words: list[str]) -> list[int]:
    trie = Trie()
    for word in words:
        trie.insert(word)
    scores = []
    for word in words:
        score = trie.get_score(word)
        scores.append(score)
    return scores