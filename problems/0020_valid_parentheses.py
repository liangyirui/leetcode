"""
https://leetcode.com/problems/valid-parentheses/description/

20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(s: str) -> bool:
    stack = []
    lookup = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in lookup:
            top = stack.pop() if stack else "#"
            if top != lookup[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    s = "(]"
    print(is_valid(s))
