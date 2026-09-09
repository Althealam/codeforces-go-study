# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        # slow走一步，fast走两步，如果两个指针相遇的话就说明有环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast: # 找到了相遇点
                slow = head # 让slow回到初始节点
                while slow!=fast: # 初始节点出发和相遇点出发的节点会在环的入口遇到
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        