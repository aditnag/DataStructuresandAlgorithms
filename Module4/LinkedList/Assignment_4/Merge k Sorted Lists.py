from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_2_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        head = temp = None
        if l1.val <= l2.val:
            head = l1
            temp = head.next
            head.next = self.merge_2_lists(temp, l2)
        else:
            head = l2
            temp = head.next
            head.next = self.merge_2_lists(l1, temp)
        return head

    def merge(self,lists, l, r):
        mid = (l + r) // 2
        if l == r:
            return lists[l]
        h1 = self.merge(lists, l, mid)
        h2 = self.merge(lists, mid+1, r)
        return self.merge_2_lists(h1, h2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.merge(lists, 0, len(lists) - 1)

