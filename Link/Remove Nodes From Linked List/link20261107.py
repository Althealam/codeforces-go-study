# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = [] # 单调栈，递减的
        cur = head
        while cur:
            # 当前节点比栈顶大，说明栈顶右边存在更大的值
            while st and st[-1].val<cur.val:
                st.pop()
            st.append(cur)
            cur = cur.next
        for i in range(len(st)-1):
            st[i].next = st[i+1]
        if not st:
            return None
        st[-1].next = None
        return st[0]