#
# @lc app=leetcode.cn id=993 lang=python3
# @lcpr version=30404
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 层序遍历
# 遍历到某一层时，判断一下当前节点是否为x/y，如果是的话，则看看同一层是否有对应的y/x，如果没有的话则直接返回false

from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        queue = deque([(root, None)])
        while queue:
            x_parent, y_parent = None, None
            for _ in range(len(queue)):
                cur, parent = queue.popleft()
                if cur.val==x:
                    x_parent = parent
                if cur.val==y:
                    y_parent = parent
                if cur.left:
                    queue.append((cur.left, cur))
                if cur.right:
                    queue.append((cur.right, cur))
            # 当前层找到两个
            if x_parent is not None and y_parent is not None:
                if x_parent==y_parent:
                    return False
                return True
            # 当前层只找到一个
            if x_parent is not None or y_parent is not None:
                return False
        return False
        
        


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
sol = Solution()
res = sol.isCousins(root, 5, 4)
print(res)

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n4\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,null,4,null,5]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,null,4]\n2\n3\n
# @lcpr case=end

#

