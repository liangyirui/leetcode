"""
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/

3217. Delete Nodes from Linked List Present in Array

You are given an array of intergers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
"""
from _classes import ListNode

def modified_list(nums: list[int], head: ListNode | None) -> ListNode | None:
    sentinel = ListNode(0, head)
    curr = sentinel
    nums_set = set(nums)
    while curr.next:
        if curr.next.val in nums_set:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return sentinel.next