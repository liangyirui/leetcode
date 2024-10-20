"""
https://leetcode.com/problems/parsing-a-boolean-expression/description/

1106. Parsing a Boolean Expression

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.
"""

def parse_bool_expr(expression: str) -> bool:
    stack = []
    for ch in expression:
        if ch in ["(", ","]:
            continue
        if ch in ["t", "f", "&", "|", "!"]:
            stack.append(ch)
        else:
            has_true = False
            has_false = False
            while stack[-1] in ["t", "f"]:
                val = stack.pop()
                if val == "t":
                    has_true = True
                if val == "f":
                    has_false = True
            op = stack.pop()
            if op == "&":
                result = "f" if has_false else "t"
            if op == "|":
                result = "t" if has_true else "f"
            if op == "!":
                result = "t" if not has_true else "f"
            stack.append(result)
    return stack[-1] == "t"