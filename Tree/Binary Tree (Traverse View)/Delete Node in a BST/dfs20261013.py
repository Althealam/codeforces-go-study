# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归函数三部曲
#（1）递归函数的参数和返回值：参数为当前子树的根节点和待删除的节点值，返回值为处理后的子树的根节点
#（2）终止条件：遇到空节点则返回（表示没找到删除的节点）
#（3）单层递归的逻辑
# - 遇到空节点：直接返回
# - 找到删除的节点
#   - 左右孩子都为空：直接返回None
#   - 左孩子为空，右孩子不为空：右孩子补位，返回右孩子
#   - 左孩子不为空，右孩子为空：左孩子补位，返回左孩子
#   - 左右孩子都不为空：右孩子补位，同时左孩子变成右孩子的最左节点左孩子

# 时间复杂度：O(h)
# 空间复杂度：O(h)
# - 递归调用栈：每次都只进入一个子树，O(h)
# - while循环：O(1)
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val==key: # 找到了要删除的节点
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # 待删除的节点有左右孩子
                cur = root.right 
                while cur.left: # 找到右孩子节点的最左孩子
                    cur = cur.left 
                cur.left = root.left
                return root.right # 处理后的子树的根节点就是root.right
        if root.val>key: 
            root.left = self.deleteNode(root.left, key)
        if root.val<key:
            root.right = self.deleteNode(root.right, key)
        return root