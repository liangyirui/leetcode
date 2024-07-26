"""
https://leetcode.com/problems/sort-an-array/description/

912. Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""


def quick_sort(nums: list[int]) -> list[int]:
    lo, hi = 0, len(nums) - 1
    _quick_sort(nums, lo, hi)
    return nums


def _quick_sort(nums: list[int], lo: int, hi: int) -> None:
    if lo > hi:
        return
    mid = _partition(nums, lo, hi)
    _quick_sort(nums, lo, mid - 1)
    _quick_sort(nums, mid + 1, hi)


def _partition(nums: list[int], lo: int, hi: int) -> int:
    pivot = lo
    while True:
        if nums[lo] < nums[pivot]:
            lo += 1
        elif nums[hi] > nums[pivot]:
            hi -= 1
        elif lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
        else:
            nums[pivot], nums[hi] = nums[hi], nums[pivot]
            break
    return hi


###################################


def merge_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    aux = [0] * n
    _merge_sort(nums, aux, 0, n - 1)
    return nums


def _merge_sort(nums: list[int], aux: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    _merge_sort(nums, aux, lo, mid)
    _merge_sort(nums, aux, mid + 1, hi)
    _merge(nums, aux, lo, mid, hi)


def _merge(nums: list[int], aux: list[int], lo: int, mid: int, hi: int) -> None:
    for i in range(lo, hi + 1):
        aux[i] = nums[i]
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            nums[k] = aux[j]
            j += 1
        elif j > hi:
            nums[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            nums[k] = aux[j]
            j += 1
        else:
            nums[k] = aux[i]
            i += 1


####################################
def heap_sort(nums: list[int]) -> None:
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)


def heapify(nums: list[int], n: int, i: int):
    root = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and nums[left] > nums[root]:
        root = left
    if right < n and nums[right] > nums[root]:
        root = right
    if root != i:
        nums[i], nums[root] = nums[root], nums[i]
        heapify(nums, n, root)


if __name__ == "__main__":
    nums = [5, 1, 1, 2, 0, 0]
    print(nums)
    heap_sort(nums)
    print(nums)
