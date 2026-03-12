# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a, b = head, head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        # 反转前面k个元素
        newHead = self.reverseN(a, k)
        # 递归反转后将后续链表拼接在一起
        a.next = self.reverseKGroup(b, k)
        return newHead

    
    def reverseN(self, head, n):
        # 反转前面n个节点
        pre = None
        cur = head
        while n>0:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            n-=1
        head.next = cur
        return pre