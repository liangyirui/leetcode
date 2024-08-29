"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

947. Most Stones Removed with Same Row or Column

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
"""


def remove_stones(stones: list[list[int]]) -> int:
    n = len(stones)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                adj[i].append(j)
                adj[j].append(i)

    num_of_cc = 0
    marked = [False] * n

    def dfs(stone):
        marked[stone] = True
        for neighbor in adj[stone]:
            if marked[neighbor]:
                continue
            dfs(neighbor)

    for i in range(n):
        if marked[i]:
            continue
        dfs(i)
        num_of_cc += 1

    return n - num_of_cc


if __name__ == "__main__":
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(remove_stones(stones))
