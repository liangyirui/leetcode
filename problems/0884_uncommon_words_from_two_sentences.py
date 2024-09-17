"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
"""

from collections import Counter

def uncommon_from_sentences(s1: str, s2: str) -> list[str]:
    count = Counter(s1.split())
    count += Counter(s2.split())
    return [word for word in count if count[word] == 1]