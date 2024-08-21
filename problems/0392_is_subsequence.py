"""
https://leetcode.com/problems/is-subsequence/description/

392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


def is_subsequence(s: str, t: str) -> bool:
    m, n = len(s), len(t)
    i = j = 0
    while i < m and j < n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == m


if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print("Is s a subsequence of t? Answer:", is_subsequence(s, t))
