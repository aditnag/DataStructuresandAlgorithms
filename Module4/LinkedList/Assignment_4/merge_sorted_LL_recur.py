# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        h1 = list1
        h2 = list2
        head = temp = None
        if h1.val <= h2.val:
            head = h1
            temp = head.next
            head.next = self.mergeTwoLists(temp, h2)
        else:
            head = h2
            temp = head.next
            head.next = self.mergeTwoLists(h1, temp)
        return head
