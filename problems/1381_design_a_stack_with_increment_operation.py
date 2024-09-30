"""
https://leetcode.com/problems/design-a-stack-with-increment-operation/description/

Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

* CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
* void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
* int pop() Pops and returns the top of the stack or -1 if the stack is empty.
* void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
"""

class CustomStack:
    
    def __init__(self, maxSize: int) -> None:
        self.stack = [0] * maxSize
        self.inc = [0] * maxSize
        self.top = -1
        
    
    def push(self, x: int) -> None:
        if self.top == len(self.stack) - 1:
            return
        self.top += 1
        self.stack[self.top] = x
        
    
    def pop(self) -> int:
        if self.top == -1:
            return -1
        val = self.stack[self.top] + self.inc[self.top]
        if self.top > 0:
            self.inc[self.top - 1] += self.inc[self.top]
        self.inc[self.top] = 0
        self.top -= 1
        return val
        
        
    def increment(self, k: int, val: int) -> None:
        if self.top == -1:
            return
        idx = min(self.top, k - 1)
        self.inc[idx] += val
        