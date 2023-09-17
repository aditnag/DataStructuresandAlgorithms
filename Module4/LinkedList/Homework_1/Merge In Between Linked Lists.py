# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count_a = 1
        count_b = 0

        prev_a = list1
        while count_a < a:
            prev_a = prev_a.next
            count_a += 1

        after_b = list1
        p2 = list1
        while count_b < b:
            p2 = p2.next
            after_b = p2.next
            count_b += 1

        if prev_a:
            prev_a.next = list2

        p2 = list1
        while p2 and p2.next:
            p2 = p2.next

        p2.next = after_b
        return list1
