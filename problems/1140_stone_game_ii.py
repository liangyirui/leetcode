"""
https://leetcode.com/problems/stone-game-ii/description/

Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
"""


def stone_game(piles: list[int]) -> int:
    n = len(piles)
    suffix_sum = [0] * n
    suffix_sum[n - 1] = piles[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + piles[i]
    memo = [[0] * n for _ in range(n)]
    return max_stone(suffix_sum, 1, 0, memo)


def max_stone(
    suffix_sum: list[int], curr_max: int, curr_index: int, memo: list[list[int]]
) -> int:
    if curr_index + 2 * curr_max >= len(suffix_sum):
        return suffix_sum[curr_index]
    if memo[curr_index][curr_max] > 0:
        return memo[curr_index][curr_max]
    stones = float("inf")
    for i in range(1, 2 * curr_max + 1):
        stones = min(
            stones, max_stone(suffix_sum, max(curr_max, i), curr_index + i, memo)
        )
    memo[curr_index][curr_max] = suffix_sum[curr_index] - stones
    return memo[curr_index][curr_max]


if __name__ == "__main__":
    piles = [2, 7, 9, 4, 4]
    print(stone_game(piles))
