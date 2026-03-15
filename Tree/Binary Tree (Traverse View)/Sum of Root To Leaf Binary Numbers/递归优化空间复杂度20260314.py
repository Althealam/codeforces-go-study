# Definition for a binary tree node.
# 优化版：时间 O(n)，空间 O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum_ = 0

    def sumRootToLeaf(self, root) -> int:
        self.traversal(root, 0)  # 传当前路径表示的二进制数 cur，而不是 path 列表
        return self.sum_

    def traversal(self, root, cur):
        """cur = 从根到当前节点父节点为止的路径所表示的二进制数（十进制）"""
        if root is None:
            return
        # [1, 0, 1] ==> 1是根节点，第2、3位依次往右
        # cur = 2*0+1 = 1
        # cur = 1*2+0 = 2
        # cur = 2*2+1 = 5
        cur = cur * 2 + root.val  # 当前路径对应的数，O(1)
        if root.left is None and root.right is None:
            self.sum_ += cur  # 叶子：直接累加，无需 path 拷贝和 return_num
            # print(f"leaf val={root.val}, cur={cur}")
        self.traversal(root.left, cur)
        self.traversal(root.right, cur)

root = TreeNode(val=1)
root.left = TreeNode(val=0)
root.right = TreeNode(val=1)
root.left.left = TreeNode(val=0)
root.left.right = TreeNode(val=1)
root.right.left = TreeNode(val=0)
root.right.right = TreeNode(val=1)
sol = Solution()
res = sol.sumRootToLeaf(root)
print(res)  # 22
