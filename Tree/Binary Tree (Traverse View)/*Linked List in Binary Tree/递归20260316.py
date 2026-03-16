# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 需要访问所有节点
# 2. 答案依赖子树
# 3. 不是路径问题
# 4. 不是祖先问题

# 返回值递归
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.issame(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def issame(self, head, root):
        """判断以当前root为节点的子树是否可以找到一个和head相同的路径"""
        if not head: # 链表匹配完就已经成功了
            return True
        if not root or not head:
            return False
        if root.val!=head.val:
            return False
        else:
            return self.issame(head.next, root.left) or self.issame(head.next, root.right)
        