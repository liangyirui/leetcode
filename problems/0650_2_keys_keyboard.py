"""
https://leetcode.com/problems/2-keys-keyboard/description/

650. 2 Keys Keyboard

There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:
Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
"""


def min_steps_dp(n: int) -> int:
    dp = [1000] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n]


def min_steps(n: int) -> int:
    ans = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            ans += factor
            n //= factor
        factor += 1
    return ans


if __name__ == "__main__":
    n = 3
    print(min_steps(n))
    print(min_steps_dp(n))
