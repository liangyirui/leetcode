"""
https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/

2337. Move Pieces to Obtain a String

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.
"""


def can_change(start: str, target: str) -> bool:
    n = len(start)
    i = j = 0
    while i < n or j < n:
        while i < n and start[i] == "_":
            i += 1
        while j < n and target[j] == "_":
            j += 1
        if i == n or j == n:
            return i == n and j == n
        if (
            start[i] != target[j]
            or (start[i] == "L" and i < j)
            or (start[i] == "R" and i > j)
        ):
            return False
        i += 1
        j += 1
    return True


if __name__ == "__main__":
    start = "R_L_"
    target = "__LR"
    print(can_change(start, target))
