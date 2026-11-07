# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        cur1, cur2 = l1, l2
        dummy_node = ListNode()
        pre = dummy_node
        carry = 0 # 进位值
        while cur1 or cur2 or carry:
            x = cur1.val if cur1 else 0
            y = cur2.val if cur2 else 0
            total = x+y+carry 
            pre.next = ListNode(total%10)
            carry = total//10
            pre = pre.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        return dummy_node.next
            
