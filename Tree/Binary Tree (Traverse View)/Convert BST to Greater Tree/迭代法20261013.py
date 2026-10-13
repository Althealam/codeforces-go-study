# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 利用BST的有序性质，通过右中左反向中序遍历，从大到小访问节点，并使用pre记录已经遍历过的节点值之和，并将每个节点更新为累加值
# 类似中序遍历的迭代法，但是顺序从左中右变化了
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [] # 模拟递归过程中系统自动维护的调用栈
        cur = root # 当前节点
        pre = 0 # 记录前面一个节点的值
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right # 右节点
            else:
                cur = stack.pop() # 已经遍历到最右了，开始进行单个节点的处理逻辑
                cur.val+=pre
                pre = cur.val
                cur = cur.left
        return root