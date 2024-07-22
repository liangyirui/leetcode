"""
https://leetcode.com/problems/sort-the-people/description/

2418. Sort the People

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the ith person.
Return names sorted in descending order by the people's heights.
"""


def sort_people(names: list[str], heights: list[int]) -> list[str]:
    """Use python built-in sort function"""
    n = len(names)
    sorted_indices = sorted(range(n), key=lambda i: heights[i], reverse=True)
    sorted_names = [names[i] for i in sorted_indices]
    return sorted_names


def quick_sort(names: list[str], heights: list[int]) -> list[str]:
    """Implement quick sort"""
    _quick_sort(heights, names, 0, len(heights) - 1)
    return names


def _quick_sort(heights: list[int], names: list[str], lo: int, hi: int) -> None:
    if lo > hi:
        return
    mid = partition(heights, names, lo, hi)
    _quick_sort(heights, names, lo, mid - 1)
    _quick_sort(heights, names, mid + 1, hi)


def partition(heights: list[int], names: list[str], lo: int, hi: int) -> int:
    pivot = lo
    while True:
        if heights[lo] > heights[pivot]:
            lo += 1
        elif heights[hi] < heights[pivot]:
            hi -= 1
        elif lo < hi:
            swap(heights, names, lo, hi)
            lo += 1
            hi -= 1
        else:
            swap(heights, names, pivot, hi)
            break
    return hi


def swap(heights: list[int], names: list[str], i: int, j: int) -> None:
    heights[i], heights[j] = heights[j], heights[i]
    names[i], names[j] = names[j], names[i]


if __name__ == "__main__":
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    print(quick_sort(names, heights))
