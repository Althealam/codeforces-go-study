# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        # 区间[a, b)包含k个待反转元素
        a = b = head
        for i in range(k): 
            # 如果不足k个，则不需要反转，直接返回head即可
            if b is None:
                return head
            b = b.next
        # 反转前面的k个元素
        newHead = self.reverse(a, b)
        # a变成了反转后的新链表的尾节点
        # newHead变成了反转后的新链表的头节点
        a.next = self.reverseKGroup(b, k) # 将第k+1个元素作为head递归调用reverseKGroup函数，并且将上述的两个结果拼接在一起
        return newHead
    
    def reverse(self, a, b): # 反转区间[a, b)，不包含b
        pre = None # 负责反转后的链表头
        cur = a
        while cur!=b:
            nxt = cur.next
            cur.next = pre
            # 当最后cur到达b的时候，pre是反转后的链表头
            pre = cur
            cur = nxt
        return pre # 反转后的头节点