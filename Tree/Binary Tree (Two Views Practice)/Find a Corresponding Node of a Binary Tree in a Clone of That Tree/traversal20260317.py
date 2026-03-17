# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. 是否需要访问所有节点：是的，需要访问cloned的所有节点
# 2. 当前节点是否依赖子树：不需要
# 3. 需不需要记录路径/父节点：不需要
# 4. 操作发生在哪：当cloned的当前节点值和target相同，则返回对应的值

class Solution:
    def __init__(self):
        self.res = None # 需要返回的值
        self.target = 0

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.target = target # 注意target是位于original的目标节点
        self.traversal(original, cloned)
        return self.res
    
    def traversal(self, original, cloned):
        if not original or not cloned:
            return 
        if cloned.val==self.target.val: # 操作发生的位置
            self.res = cloned
            return 
        # 二叉树递归模版
        self.traversal(original.left, cloned.left)
        self.traversal(original.right, cloned.right)
        

        