"""
https://leetcode.com/problems/maximum-swap/description/

670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.
"""

def maximum_swap(num: int) -> int:
    digits = [int(x) for x in str(num)]
    n = len(digits)
    max_idx = len(n) - 1
    left = right = 0
    for i in range(n - 1, -1, -1):
        if digits[i] > digits[max_idx]:
            max_idx = i
        elif digits[i] < digits[max_idx]:
            left = i
            right = max_idx
    digits[left], digits[right] = digits[right], digits[left]
    return int(''.join([str(x) for x in digits]))