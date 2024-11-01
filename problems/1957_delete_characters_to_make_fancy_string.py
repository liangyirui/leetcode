"""
https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.
"""

def make_fancy_string(s: str) -> str:
    n = len(s)
    if n < 3:
        return s
    sb = []
    for i, ch in enumerate(s):
        if i < 2:
            sb.append(ch)
        elif ch == s[i - 1] and ch == s[i - 2]:
            continue
        else:
            sb.append(ch)
    return ''.join(sb)