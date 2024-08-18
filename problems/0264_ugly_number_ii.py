"""
https://leetcode.com/problems/ugly-number-ii/description/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
"""

import heapq


def nth_ugly_number(n: int) -> int:
    dp = [0] * n
    dp[0] = 1
    index2 = index3 = index5 = 0
    factor2, factor3, factor5 = 2, 3, 5
    for i in range(1, n):
        dp[i] = min(factor2, factor3, factor5)
        if factor2 == dp[i]:
            index2 += 1
            factor2 = 2 * dp[index2]
        if factor3 == dp[i]:
            index3 += 1
            factor3 = 3 * dp[index3]
        if factor5 == dp[i]:
            index5 += 1
            factor5 = 5 * dp[index5]
    return dp[n - 1]


def nth_ugly_number_pq(n: int) -> int:
    pq = []
    seen = {1}
    primes = [2, 3, 5]
    heapq.heappush(pq, 1)
    curr = 1
    for _ in range(n):
        curr = heapq.heappop(pq)
        for prime in primes:
            next_num = curr * prime
            if next_num in seen:
                continue
            heapq.heappush(pq, next_num)
            seen.add(next_num)
    return curr


if __name__ == "__main__":
    n = 10
    print(nth_ugly_number_pq(n))
