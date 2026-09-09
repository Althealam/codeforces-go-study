# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        # 定义快慢节点
        slow, fast = dummy_node, dummy_node

        # 移动快节点到正数的第n个节点
        for _ in range(n):
            fast = fast.next
        
        # 移动快节点到序列最后一个节点，此时快节点移动l-n-1个节点
        # 慢节点也移动l-n-1个节点，即正数的第l-n-1个节点，倒数的第n+1个节点
        while fast and fast.next: # 一定要带上fast.next，否则无法保证快节点移动到最后一个节点
            slow = slow.next
            fast = fast.next
        
        # 慢节点在倒数第n个节点的前面一个节点，因此可以直接通过下面的代码执行删除操作
        slow.next = slow.next.next

        return dummy_node.next