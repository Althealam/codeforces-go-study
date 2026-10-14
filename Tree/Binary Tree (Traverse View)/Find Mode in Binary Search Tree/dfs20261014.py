# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 分析思路：本题是BST，同时存在重复值，目标是找到出现次数最多的元素，输出是所有的众数
# BST -> 中序遍历 -> 非递减序列 -> 重复元素一定连续出现

# 需要维护的变量：
# 1. pre：上一个访问的节点值
# 2. count：当前值连续出现的次数
# 3. max_count：已经发现的最大出现次数
# 4. res：所有的众数
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        res = []
        pre = None
        count = 0
        max_count = 0
        def dfs(node):
            nonlocal res, pre, count, max_count
            if not node:
                return 
            dfs(node.left)
            # 处理当前节点
            # 1. 更新count
            if pre is not None and node.val==pre:
                count+=1
            else:
                count = 1
            # 2. 更新众数
            if count>max_count:
                max_count = count
                res = [node.val]
            elif count==max_count:
                res.append(node.val)
            # 3. 更新前一个节点的值
            pre = node.val
            dfs(node.right)
        dfs(root)
        return res