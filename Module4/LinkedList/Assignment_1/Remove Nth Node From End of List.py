# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        c = 0

        while c < n:
            p2 = p2.next
            c += 1

        if p2 is None:
            head = head.next
            return head

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next
        return head
