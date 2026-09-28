# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if len(inorder)==0 and len(postorder)==0:
            return None
        root = TreeNode(postorder[-1])
        root_index_inorder = inorder.index(root.val)
        root.left = self.buildTree(inorder[:root_index_inorder], postorder[:root_index_inorder])
        root.right = self.buildTree(inorder[root_index_inorder+1:], postorder[root_index_inorder:-1])
        return root 