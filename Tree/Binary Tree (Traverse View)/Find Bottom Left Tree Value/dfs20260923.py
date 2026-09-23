# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题目类型：自顶向下
# dfs三部曲：
#（1）返回值含义：不用返回具体值，只需要负责遍历+更新全局答案，即遍历当前node，并根据depth更新当前找到的最深层最左节点
#（2）携带参数：当前正在访问的节点，当前节点所在的深度
#（3）终止条件：当前节点为空时，则递归终止（已经走到树外面了，不需要继续递归）
#（4）单层递归的逻辑
# 判断当前深度是不是比之前更深，如果是的话就记录最左节点，并更新最深的深度

# 时间复杂度：O(n)
# 空间复杂度：O(h)，相比于层序遍历，其空间复杂度更低
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        self.max_depth = -1
        self.res = root.val

        def dfs(node, depth):
            # 终止条件
            if not node:
                return 
            # 单层递归的逻辑
            # 第一次到达新的更深层，则更新最大的深度以及答案值
            if depth>self.max_depth:
                self.max_depth = depth
                self.res = node.val
            
            # 先左后右，此时可以保证是最左的
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        return self.res
            