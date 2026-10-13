# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        if not root:
            return None
        
        # 处理头节点，让root移动到[low, high]的范围内
        while root and (root.val<low or root.val>high):
            if root.val<low:
                root = root.right # 小于low则往右走
            else:
                root = root.left # 大于high则往左走
        
        cur = root

        # 此时的root已经在[low, high]的范围内，处理左孩子元素小于low的情况
        while cur:
            # 如果左孩子节点小于low，则左孩子节点的左孩子都小于low，则删除左孩子节点
            while cur.left and cur.left.val<low:
                cur.left = cur.left.right
            cur = cur.left # 递归处理左子树
        
        cur = root
        
        # 继续处理右孩子元素大于high的情况
        while cur:
            # 如果右孩子节点大于high，则右孩子节点的右孩子都大于high，则删除右孩子节点
            while cur.right and cur.right.val>high:
                cur.right = cur.right.left
            cur = cur.right # 递归处理右子树
        return root