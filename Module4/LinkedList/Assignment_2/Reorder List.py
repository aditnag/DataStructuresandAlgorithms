# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow = head
        fast = head
        l1 = None
        while fast and fast.next:
            l1 = slow
            slow = slow.next
            fast = fast.next.next

        l1.next = None
        curr = slow
        prev = None
        # reversing the separated list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        p1, p2 = head, prev
        while p1 and p2:
            temp_p1, temp_p2 = p1.next, p2.next
            p1.next = p2
            if temp_p1:
                p2.next = temp_p1
            p1, p2 = temp_p1, temp_p2

        # return head
