"""
https://leetcode.com/problems/count-number-of-teams/description/

1395. Count Number of Teams
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
You have to form a team of 3 soldiers amongst them under the following rules:
Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
"""

from _classes import BIT


def num_teams(rating: list[int]) -> int:
    n = len(rating)
    count = 0
    for mid in range(n):
        left_smaller = right_larger = 0
        for left in range(mid):
            if rating[mid] > rating[left]:
                left_smaller += 1
        for right in range(mid + 1, n):
            if rating[mid] < rating[right]:
                right_larger += 1
        left_larger = mid - left_smaller
        right_smaller = n - 1 - mid - right_larger
        count += left_smaller * right_larger + left_larger * right_smaller
    return count


def num_teams_bit(rating: list[int]) -> int:
    n = len(rating)
    max_val = max(rating)
    lbtree = BIT(max_val)
    rbtree = BIT(max_val)
    lbtree.update(rating[0], 1)
    for i in range(1, n):
        rbtree.update(rating[i], 1)

    count = 0
    for i in range(1, n - 1):
        num = rating[i]
        rbtree.update(num, -1)
        count += rbtree.query(num - 1) * (i - lbtree.query(num))
        count += lbtree.query(num - 1) * (n - i - 1 - rbtree.query(num))
        lbtree.update(rating[i], 1)
    return count


if __name__ == "__main__":
    rating = [2, 5, 3, 4, 1]
    print(num_teams(rating))
    print(num_teams_bit(rating))
