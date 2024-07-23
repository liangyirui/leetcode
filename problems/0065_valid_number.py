"""
https://leetcode.com/problems/valid-number/description/

65. Valid Number

Given a string s, return whether s is a valid number.
For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".
Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.
The digits are defined as one or more digits.
"""


def is_number(s: str) -> bool:
    seen_digit = seen_exponent = seen_dot = False
    for i, ch in enumerate(s):
        if ch.isdigit():
            seen_digit = True
        elif ch in "+-":
            if i > 0 and s[i - 1] not in "eE":
                return False
        elif ch in "eE":
            if seen_exponent or not seen_digit:
                return False
            seen_exponent = True
            seen_digit = False
        elif ch == ".":
            if seen_dot or seen_exponent:
                return False
            seen_dot = True
        else:
            return False
    return seen_digit


def is_number_dfa(s: str) -> bool:
    dfa = [
        {"digit": 1, "sign": 2, "dot": 3},
        {"digit": 1, "dot": 4, "exponent": 5},
        {"digit": 1, "dot": 3},
        {"digit": 4},
        {"digit": 4, "exponent": 5},
        {"sign": 6, "digit": 7},
        {"digit": 7},
        {"digit": 7},
    ]

    curr_state = 0
    for ch in s:
        if ch.isdigit():
            group = "digit"
        elif ch in "+-":
            group = "sign"
        elif ch in "eE":
            group = "exponent"
        elif ch == ".":
            group = "dot"
        else:
            return False
        if group not in dfa[curr_state]:
            return False
        curr_state = dfa[curr_state][group]

    return curr_state in [1, 4, 7]


if __name__ == "__main__":
    s = "1.0e+1"
    print(is_number(s))
