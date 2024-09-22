"""
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
"""

def find_kth_number(n: int, k: int) -> int:
    curr = 1
    k -= 1
    while k > 0:
        steps = count_steps(n, curr, curr + 1)
        if steps <= k:
            curr += 1
            k -= steps
        else:
            curr *= 10
            k -= 1
    return curr
    

def count_steps(n: int, prefix1: int, prefix2: int) -> int:
    steps = 0
    while prefix1 <= n:
        steps += min(n + 1, prefix2) - prefix1
        prefix1 *= 10
        prefix2 *= 10
    return steps