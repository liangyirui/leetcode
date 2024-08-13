"""
https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
"""


def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
    ans = []
    candidates.sort()
    backtrack(candidates, 0, target, [], ans)
    return ans


def backtrack(
    nums: list[int], start: int, remain: int, path: list[int], paths: list[list[int]]
) -> None:
    if remain < 0:
        return
    if remain == 0:
        paths.append(path[:])
        return
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        path.append(nums[i])
        backtrack(nums, i + 1, remain - nums[i], path, paths)
        path.pop()


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(combination_sum_2(candidates, target))
