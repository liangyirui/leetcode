"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/

1653. Minimum Deletions to Make String Balanced

You are given a string s consisting only of characters 'a' and 'b'​​​​.
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.
"""


def minimum_deletions(s: str) -> int:
    n = len(s)
    count_b = 0
    min_deletions = n
    for ch in s:
        if ch == "a":
            min_deletions = min(min_deletions + 1, count_b)
        else:
            count_b += 1
    return min_deletions


def minimum_deletions_stack(s: str) -> int:
    stack = []
    min_deletions = 0
    for ch in s:
        if stack and stack[-1] == "b" and ch == "a":
            stack.pop()
            min_deletions += 1
        else:
            stack.append(ch)
    return min_deletions


if __name__ == "__main__":
    s = "aababbab"
    print(minimum_deletions(s))
    print(minimum_deletions_stack(s))
