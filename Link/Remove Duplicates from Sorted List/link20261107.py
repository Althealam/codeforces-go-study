# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy1 = ListNode()
        dummy2 = ListNode()
        pre1, pre2 = dummy1, dummy2
        cur = head
        while cur:
            if cur.val<x:
                pre1.next = cur
                pre1 = pre1.next
            else:
                pre2.next = cur
                pre2 = pre2.next
            cur = cur.next
        pre2.next = None
        pre1.next = dummy2.next
        return dummy1.next