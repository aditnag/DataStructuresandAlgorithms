# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while count < k and curr:
            curr = curr.next
            count += 1

        if count < k:
            return head

        curr = head
        prev = None
        count = 0
        while count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        head.next = self.reverseKGroup(curr, k)
        return prev
