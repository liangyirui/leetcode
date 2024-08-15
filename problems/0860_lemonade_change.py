"""
https://leetcode.com/problems/lemonade-change/description/

860. Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
"""


def lemonade_change(bills: list[int]) -> bool:
    fives = tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives < 1:
                return False
            fives -= 1
            tens += 1
        else:
            if tens > 0 and fives > 0:
                fives -= 1
                tens -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True


if __name__ == "__main__":
    bills = [5, 5, 10, 10, 20]
    print(lemonade_change(bills))
