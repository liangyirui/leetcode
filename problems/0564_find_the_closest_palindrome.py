"""
https://leetcode.com/problems/find-the-closest-palindrome/description/

564. Find the Closest Palindrome
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.
The closest is defined as the absolute difference minimized between two integers.
"""


def nearest_palindromic(num: str) -> str:
    n = len(num)
    i = n // 2 - 1 if n % 2 == 0 else n // 2
    first_half = int(num[: i + 1])
    candidates = []
    candidates.append(build_palindrome(first_half, n % 2 == 0))
    candidates.append(build_palindrome(first_half + 1, n % 2 == 0))
    candidates.append(build_palindrome(first_half - 1, n % 2 == 0))
    candidates.append(10 ** (n - 1) - 1)
    candidates.append(10**n + 1)

    diff = float("inf")
    res = 0
    n1 = int(num)
    for candidate in candidates:
        if candidate == n1:
            continue
        if abs(candidate - n1) < diff:
            diff = abs(candidate - n1)
            res = candidate
        elif abs(candidate - n1) == diff:
            res = min(res, candidate)
    return str(res)


def build_palindrome(left: int, even: bool) -> int:
    res = left
    if not even:
        left = left // 10
    while left > 0:
        res = res * 10 + left % 10
        left //= 10
    return res


if __name__ == "__main__":
    num = "123"
    print(nearest_palindromic(num))
