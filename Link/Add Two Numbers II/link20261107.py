# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 链表是从最高位开始的，因此要用栈来存储
# 和Add Two Numbers不同 -> 这道题是从最低位开始的
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        carry = 0
        stack = []
        while stack1 or stack2 or carry:
            if stack1:
                x = stack1[-1].val
                stack1.pop()
            else:
                x = 0
            if stack2:
                y = stack2[-1].val
                stack2.pop()
            else:
                y = 0
            total = x+y+carry
            stack.append(ListNode(total%10))
            carry = total//10
        

        for i in range(len(stack)-1, 0, -1):
            stack[i].next = stack[i-1]
        return stack[-1]
