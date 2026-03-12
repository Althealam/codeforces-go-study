class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        a, b = head, head
        for _ in range(k):
            if b is None: # 不满足k个的则直接返回
                return head
            b = b.next
        new_head = self.reverse(a, b)
        # print(new_head.val)
        # print(a.val)
        a.next = self.reverseKGroup(b, k)
        return new_head
    
    def reverse(self, left, right):
        pre = None
        cur = left
        while cur!=right:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
    def print_link(self, head):
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)
        return arr
    
    def arr_to_link(self, arr):
        dummy_node = ListNode()
        cur = dummy_node
        for i in range(len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return dummy_node.next


sol = Solution()
arr = [1,2,3,4,5]
head = sol.arr_to_link(arr)
sol.print_link(sol.reverseKGroup(head, 2))
