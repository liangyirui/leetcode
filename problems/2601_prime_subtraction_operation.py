"""
https://leetcode.com/problems/prime-subtraction-operation/description/

You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.
"""

def prime_sub_operation(nums: list[int]) -> bool:
    primes = generate_primes(1000)
    prev = 1
    i = 0
    while i < len(nums):
        diff = nums[i] - prev
        if diff < 0:
            return False
        if primes[diff] or diff == 0:
            i += 1
            prev += 1
        else:
            prev += 1
    return True

def generate_primes(limit: int) -> list[bool]:
    primes = [True] * (limit + 1)
    primes[0] = False
    primes[1] = False
    for p in range(2, isqrt(limit) + 1):
        if not primes[p]:
            continue
        for i in range(p * p, limit + 1, p):
            primes[i] = False
    return primes
