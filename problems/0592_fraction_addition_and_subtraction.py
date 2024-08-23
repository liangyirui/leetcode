"""
https://leetcode.com/problems/fraction-addition-and-subtraction/description/

592. Fraction Addition and Subtraction
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
"""

import re


def fraction_addition(expression: str) -> str:
    numerator = 0
    denominator = 1
    n = len(expression)
    i = 0
    while i < n:
        curr_num = curr_denom = 0
        is_negative = False

        # check sign
        if expression[i] == "-" or expression[i] == "+":
            if expression[i] == "-":
                is_negative = True
            i += 1

        # parse numerator
        while i < n and expression[i].isdigit():
            val = int(expression[i])
            curr_num = curr_num * 10 + val
            i += 1

        if is_negative:
            curr_num *= -1

        # skip divisor
        i += 1

        # parse denominator
        while i < n and expression[i].isdigit():
            val = int(expression[i])
            curr_denom = curr_denom * 10 + val
            i += 1

        numerator = numerator * curr_denom + curr_num * denominator
        denominator *= curr_denom

    gcd = find_gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return f"{numerator}/{denominator}"


def fraction_addition_re(expression: str) -> str:
    numerator = 0
    denominator = 1
    nums = re.split("/|(?=[-+])", expression)
    nums = list(filter(None, nums))
    for i in range(0, len(nums), 2):
        curr_num = int(nums[i])
        curr_denom = int(nums[i + 1])
        numerator = numerator * curr_denom + curr_num * denominator
        denominator *= curr_denom
    gcd = abs(find_gcd(numerator, denominator))
    numerator //= gcd
    denominator //= gcd
    return f"{numerator}/{denominator}"


def find_gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    expression = "1/3-1/2"
    print(fraction_addition(expression))
    print(fraction_addition_re(expression))
