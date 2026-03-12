# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1) # <x
        dummy2 = ListNode(-1) # >=x
        p1, p2 = dummy1, dummy2
        p = head # 遍历原链表
        while p:
            if p.val>=x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            # 不能直接让p前进: p = p.next（否则会导致p带着剩余的结点一起被连接）
            # 断开原链表中每个结点的next指针
            temp = p.next # 记住下一个结点
            p.next = None # 将当前节点的next剪掉（一定要断开当前节点）
            p = temp # 利用刚才记下的下一个结点，跳到原链表的下一个位置
        p1.next = dummy2.next
        return dummy1.next