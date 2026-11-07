# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(next = head)
        l1 = dummy
        for _ in range(n):
            l1 = l1.next
        l2 = dummy
        while l1.next:
            l2 = l2.next
            l1 = l1.next

        l2.next = l2.next.next
        return dummy.next