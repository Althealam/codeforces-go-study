# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：
# 2. DFS三部曲
#（1）携带参数：当前遍历到preorder的第几个元素idx，这个子树的upperbound，preorder
#（2）返回值含义：建立好的子树根节点
#（3）终止条件：
# - 已经遍历完preorder了则返回None
# - 如果当前遍历的元素值超过了upperbound，则返回
#（4）单层递归的逻辑
# - 获取根节点并且移动idx
# - 递归建立左右子树
#   - 左子树的upperbound就是根节点
#   - 右子树的upperbound继承根节点的upperbound
class Solution:
    def __init__(self):
        self.idx = 0
        self.preorder = None

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        return self.dfs(float('inf'))

    def dfs(self, upperbound):
        if self.idx == len(self.preorder):
            return None
        if self.preorder[self.idx]>upperbound:
            return None
        root = TreeNode(self.preorder[self.idx])
        self.idx+=1
        root.left = self.dfs(root.val)
        root.right = self.dfs(upperbound)
        return root