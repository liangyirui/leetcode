"""
https://leetcode.com/problems/moving-average-from-data-stream/description/

346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Implement the MovingAverage class:
MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
"""


class MovingAverage:
    def __init__(self, size: int) -> None:
        self.arr = [0] * size
        self.size = size
        self.total = 0
        self.count = 0
        self.head = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.total = self.total - self.arr[tail] + val
        self.head = (self.head + 1) % self.size
        self.arr[self.head] = val
        return self.total / min(self.size, self.count)
