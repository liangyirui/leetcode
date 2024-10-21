"""
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.
"""

def max_unique_split(s: str) -> int:
    seen = set()
    return backtrack(s, 0, seen)
    

def backtrack(s: str, start: int, seen: set) -> int:
    if start == len(s):
        return 0
    max_count = 0
    for end in range(start + 1, len(s) + 1):
        substring = s[start:end]
        if substring in seen:
            continue
        seen.add(substring)
        max_count = max(max_count, 1 + backtrack(s, end, seen))
        seen.remove(substring)
    return max_count
    

if __name__ == "__main__":
    s = "ababccc"
    print(max_unique_split(s))