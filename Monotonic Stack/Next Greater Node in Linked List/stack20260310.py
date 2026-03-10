# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n+=1
        
        ans = [0]*n
        stack = []
        cur = head
        index = 0
        while cur:
            while len(stack)!=0 and cur.val>stack[-1][0]:
                val, idx = stack.pop()
                ans[idx] = cur.val
            stack.append((cur.val, index))
            index+=1
            cur = cur.next
        
        return ans