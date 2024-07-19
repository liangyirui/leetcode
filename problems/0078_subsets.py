"""
https://leetcode.com/problems/subsets/description/

78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
"""


def subsets(nums: list[int]) -> list[list[int]]:
    path = []
    paths = []
    backtrack(nums, 0, path, paths)
    return paths


def backtrack(
    nums: list[int], start: int, path: list[int], paths: list[list[int]]
) -> None:
    paths.append(path[:])
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(nums, i + 1, path, paths)
        path.pop()


def main() -> None:
    nums = [1, 2, 3, 4]
    paths = subsets(nums)
    print(paths)


if __name__ == "__main__":
    main()
