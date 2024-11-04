"""
https://leetcode.com/problems/rotate-string/description/

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""


def rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    double_s = s + s
    return double_s.find(goal) != -1


if __name__ == "__main__":
    s = "abcde"
    goal = "abced"
    print(rotate_string(s, goal))
