"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""

def count_consistent_strings(allowed: str, words: list[str]) -> int:
    is_allowed = [False] * 26
    count = 0
    for ch in allowed:
        is_allowed[ord(ch) - ord('a')] = True
    
    for word in words:
        is_consistent = True
        for ch in word:
            if not is_allowed[ord(ch) - ord('a')]:
                is_consistent = False
                break
        count += 1 if is_consistent else 0
    
    return count