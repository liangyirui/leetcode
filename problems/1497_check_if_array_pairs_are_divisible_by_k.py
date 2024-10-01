"""
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.
"""

def can_arrange(arr: list[int], k: int) -> bool:
    remainder_count = {}
    for num in arr:
        remainder_count[(num % k + k) % k] = remainder_count.get((num % k + k) % k, 0) + 1
    
    for num in arr:
        rem = (num % k + k) % k
        if rem == 0:
            if remainder_count[rem] % 2 == 1:
                return False
        elif remainder_count[rem] != remainder_count.get((k - rem), 0):
            return False
    return True