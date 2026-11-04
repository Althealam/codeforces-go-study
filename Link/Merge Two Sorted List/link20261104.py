# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. 定义slow和fast，fast每次走两步，slow每次走一步，如果slow和fast相遇的话，说明有环，同时可以找到相遇点
# 2. slow走的节点数为x+y，fast走过的节点数为x+y+n(y+z)，n为fast在环内走的圈数，其中y是相遇的地方，x是头节点到环形入口的地方，z为相遇点到环入口的地方
# 2*(x+y)=x+y+n(y+z) -> x+y=n(y+z) -> x = n(y+z)-y = (n-1)(y+z)+z 
# 头节点到环形入口的地方 = 相遇点到环入口的地方
# 从头节点出发一个指针，从相遇点出发一个指针，两个指针都走一步，最终两个指针会在环的入口相遇
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None