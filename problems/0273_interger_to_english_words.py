"""
https://leetcode.com/problems/integer-to-english-words/description/

273. Integer to English Words
Convert a non-negative integer num to its English words representation.
"""


def number_to_words(num: int) -> str:
    below_twenty: list[str] = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    tens: list[str] = [
        "",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]

    def helper(num: int) -> str:
        if num < 20:
            return below_twenty[num]
        if num < 100:
            return tens[num // 10] + (" " + helper(num % 10) if num % 10 != 0 else "")
        if num < 1000:
            return (
                helper(num // 100)
                + " Hundred"
                + (" " + helper(num % 100) if num % 100 != 0 else "")
            )
        if num < 1000000:
            return (
                helper(num // 1000)
                + " Thousand"
                + (" " + helper(num % 1000) if num % 1000 != 0 else "")
            )
        if num < 1000000000:
            return (
                helper(num // 1000000)
                + " Million"
                + (" " + helper(num % 1000000) if num % 1000000 != 0 else "")
            )
        return (
            helper(num // 1000000000)
            + " Billion"
            + (" " + helper(num % 1000000000) if num % 1000000000 != 0 else "")
        )

    return helper(num)


if __name__ == "__main__":
    num = 1234567
    print(number_to_words(num))
