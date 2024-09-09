"""
https://leetcode.com/problems/split-linked-list-in-parts/

725. Split Linked List in Parts

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.
""""

from _classes import ListNode

def split_list_to_parts(head: ListNode | None, k: int) -> list[list[ListNode | None]]:
    nodes = [None] * k
    curr = head
    sz = 0
    while curr:
    	curr = curr.next
        sz += 1
    num = sz // k
    rem = sz % k
    curr = head
    prev = None
    i = 0
    while i < k and curr:
        nodes[i] = curr
        for j in range(num + (rem > 0)):
            prev = curr
            curr = curr.next
        prev.next = None
        rem -= 1
        i += 1
    return nodes