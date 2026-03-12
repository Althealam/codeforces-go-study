# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = self.addTwo(l1, l2)
        return l3
    
    def addTwo(self, l1, l2):
        # 由于链表是从最高位到最低位，所以要用栈，从最低位开始
        stack1 = [] # 1->2->3->4 ==> stack1 = [1, 2, 3, 4]
        stack2 = [] # 1->2->3->4 ==> stack2 = [1, 2, 3, 4]
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None # 结果链表的头指针，初始化为None
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total = val1+val2+carry  
            # 更新进位
            carry = total//10 
            # 创建新节点
            node = ListNode(total%10)
            # 更新一下链表（头插法）
            node.next = head # 将当前链表挂在新节点的后面
            head = node # 更新head，让他重新指向最前面的这个新节点
            # 头插法主要是永远让新的节点当头节点
        return head

