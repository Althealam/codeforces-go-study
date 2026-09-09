# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 时间复杂度：O(m+n)
# 空间复杂度：O(1)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = self.get_length(headA)
        lengthB = self.get_length(headB)
        if lengthA<lengthB:
            headA, headB = headB, headA
            lengthA, lengthB = lengthB, lengthA
        diff = lengthA-lengthB

        curA, curB = headA, headB
        for _ in range(diff):
            curA = curA.next

        while curA!=curB:
            curA = curA.next
            curB = curB.next

        return curA
    
    def get_length(self, head):
        if head is None:
            return 0
        cur = head
        length = 0
        while cur:
            length+=1
            cur = cur.next
        return length
            