"""
Description:
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.
`k` is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.


Constrains:
* The number of nodes in the list is n
* 1 <= k <= n <= 5000
* 0 <= Node.val <= 1000

Ideas:
1. Use a list as a stack
2. Use double pointers to denote head and tail every k nodes
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        current_node = head
        node_list = []
        before_node = None
        while current_node is not None:
            if len(node_list) == k:
                new_head, before_node, after = self.reverse_nodes(before_node, node_list)
                if new_head is not None:
                    head = new_head
                node_list = []
                current_node = after
            else:
                node_list.append(current_node)
                current_node = current_node.next
        if len(node_list) > 0 and len(node_list) < k:
            before_node.next = node_list[0]
        elif len(node_list) == k:
            new_head, before_node, after = self.reverse_nodes(before_node, node_list)
            if new_head is not None:
                head = new_head
        return head
    
    def reverse_nodes(self, before_node, node_list):
        first = node_list.pop()
        after = first.next
        if before_node is None:
            new_head = first
        else:
            new_head = None
            before_node.next = first
        while len(node_list) > 0:
            last = node_list.pop()
            first.next = last
            first = last
            first.next = None
        return new_head, first, after
    
    def reverseKGroup_alternative(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        counter = 1
        before_start = None
        start = head
        end = head
        while end is not None:
            if counter == k:
                new_head, before_start, next_node = self.reverse(start, end, before_start, k)
                if new_head is not None:
                    head = new_head
                start = next_node
                end = next_node
                counter = 1
            else:
                counter += 1
                end = end.next
        return head
    
    def reverse(self, start, end, before_start, k):
        i = 0
        current_node = start
        next_node = end.next
        before = None
        while i < k:
            current_next = current_node.next
            current_node.next = before
            before = current_node
            current_node = current_next
            i += 1
        start.next = next_node

        if before_start is None:
            new_start = end
        else:
            new_start = None
            before_start.next = end
        return new_start, start, next_node
        