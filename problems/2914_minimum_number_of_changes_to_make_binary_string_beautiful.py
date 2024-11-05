"""
https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/

You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more substrings such that:

Each substring has an even length.
Each substring contains only 1's or only 0's.
You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.
"""


def min_changes(s: str) -> int:
    n = len(s)
    changes = 0
    for i in range(0, n, 2):
        if s[i] != s[i + 1]:
            changes += 1
    return changes


if __name__ == "__main__":
    s = "1001"
    print(min_changes(s))
