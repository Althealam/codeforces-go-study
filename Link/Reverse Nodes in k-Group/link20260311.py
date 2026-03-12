# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.get_length(head)
        dummy_node = ListNode(next = head)
        first_node = dummy_node
        while n>=k:
            n-=k
            pre = None # 待反转链表的头节点的前面一个节点
            cur = first_node.next # 开始遍历待反转的链表
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            # 将反转后的链表合并在一起
            original_head = first_node.next

            # 连接三个部分
            first_node.next = pre
            original_head.next = cur

            # 移动first_node
            first_node = original_head
        return dummy_node.next
        

    def get_length(self, head):
        n = 0
        cur = head
        while cur:
            n+=1
            cur = cur.next
        return n