# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        n = 1
        oldtail = head
        while oldtail.next:
            oldtail = oldtail.next
            n += 1
        oldtail.next = head
        newtail = head
        k = k % n
        for i in range(n - k - 1):
            newtail = newtail.next
        newhead = newtail.next
        newtail.next = None
        return newhead
