"""
https://leetcode.com/problems/design-circular-deque/

641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
"""

class MyCircularDeque:
    
    def __init__(self, k: int) -> None:
        self.queue = [None] * k
        self.capacity = k
        self.size = 0
        self.first = 0
        self.last = k - 1
        
    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False
        self.first = (self.first - 1 + self.capacity) % self.capacity
        self.queue[self.first] = value
        self.size += 1
        return True
        
    def insert_last(self, value: int) -> bool:
        if self.is_full():
            return False
        self.last = (self.last + 1) % self.capacity
        self.queue[self.last] = value
        self.size += 1
        return True
        
    def delete_front(self) -> bool:
        if self.is_empty():
            return False
        self.queue[self.first] = None
        self.first = (self.first + 1) % self.capacity
        self.size -= 1
        return True
        
    def delete_last(self) -> bool:
        if self.is_empty():
            return False
        self.queue[self.last] = None
        self.last = (self.last - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True
        
    def get_front(self) -> int:
        if self.is_empty():
            return -1
        return self.queue[self.first]
        
    def get_last(self) -> int:
        if self_is_empty():
            return -1
        return self.queue[self.last]
        
    def is_empty(self) -> bool:
        return self.size == 0
        
    def is_full(self) -> bool:
        return self.size == self.capacity