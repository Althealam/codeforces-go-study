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


# 返回值递归
# 1. 判断root.val==head.val，如果是的话，则继续遍历root.left和root.right，判断一下和head的下一个节点是否相同
# 2. 如果root.val!=head.val，那么就继续判断root.left和root.right是否和head.val相同

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.is_same(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def is_same(self, head, root):
        if head is None:
            return True
        if root is None and head is not None:
            return False
        if root.val!=head.val:
            return False
        return self.is_same(head.next, root.left) or self.is_same(head.next, root.right)

        