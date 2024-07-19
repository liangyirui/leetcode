"""
https://leetcode.com/problems/ipo/description/

502. IPO

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.
You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
The answer is guaranteed to fit in a 32-bit signed integer.
"""

import heapq


def find_max_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    n = len(capital)
    cost_profit = list(zip(capital, profits))
    cost_profit.sort()
    pq = []
    ptr = 0
    for i in range(k):
        while ptr < n and cost_profit[ptr][0] <= w:
            heapq.heappush(pq, -cost_profit[ptr][1])
            ptr += 1
        if not pq:
            break
        w += -heapq.heappop(pq)
    return w


if __name__ == "__main__":
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    max_profit = find_max_capital(k, w, profits, capital)
    print(f"The maximized capital is {max_profit}")
