"""
https://leetcode.com/problems/all-oone-data-structure/

Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.
"""

class Node:
    def __init__(self, freq = 0, prev = None, next = None):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.keys = set()
        

class AllOne:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = {}		# Mapping from key to its node
        
    def inc(self, key: str):
        if key in self.mp:
            node = self.mp[key]
            freq = node.freq
            node.keys.remove(key). # Remove key from current node
            next_node = node.next
            if next_node is self.tail or next_node.freq != freq + 1:
                # Create new node if next node does not exist of freq is not freq + 1
                new_node = Node(freq + 1, node, next_node)
                new_node.keys.add(key)
                node.next = new_node
                next_node.prev = new_node
                self.mp[key] = new_node
            else:
                # Increment the existing next node
                next_node.keys.add(key)
                self.mp[key] = next_node
    		# Remove the current node if it has no keys left
            if not node.keys:
                self.remove_node(node)
        else:
            first_node = self.head.next
            if first_node is self.tail or first_node.freq > 1:
                new_node = Node(1, self.head, first_node)
                new_node.keys.add(key)
                self.head.next = new_node
                first_node.prev = new_node
                self.mp[key] = new_node
            else:
                first_node.keys.add(key)
                self.mp[key] = first_node
                
    def dec(self, key: str):
        if key not in self.mp:
            return
        node = self.mp[key]
        node.keys.remove(key)
        freq = node.freq
        if freq == 1:
            del self.mp[key]
        else:
            prev_node = node.prev
            if prev_node is self.head or prev_node.freq != freq - 1:
                new_node = Node(freq - 1, prev_node, node)
                new_node.keys.add(key)
                prev_node.next = new_node
                node.prev = new_node
                self.mp[key] = new_node
            else:
                prev_node.keys.add(key)
                self.mp[key] = prev_node
            if not node.keys:
                self.remove_node(node)
                
    
    def get_max_key(self):
        if self.tail.prev is self.head:
            return ""
        return next(iter(self.tail.prev.keys))
        
        
    def get_min_key(self):
    	if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))
        
        
    def remove_node(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
            