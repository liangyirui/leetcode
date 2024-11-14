"""
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/

You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

A store can only be given at most one product type but can be given any amount of it.
After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.

Return the minimum possible x.
"""


def minimized_maximum(n: int, quantities: list[int]) -> int:
    lo = 0
    hi = max(quantities)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_distribute(n, quantities, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def can_distribute(n: int, quantities: list[int], target: int) -> bool:
    j = 0
    remain = quantities[j]
    for i in range(n):
        if remain <= target:
            j += 1
            if j == len(quantities):
                return True
            else:
                remain = quantities[j]
        else:
            remain -= target
    return False


if __name__ == "__main__":
    n = 7
    quantities = [15, 10, 10]
    print(minimized_maximum(n, quantities))
