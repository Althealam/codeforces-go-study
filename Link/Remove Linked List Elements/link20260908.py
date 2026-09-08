# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(next = head)
        cur = head
        pre = dummy_node
        while cur:
            if cur.val==val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy_node.next