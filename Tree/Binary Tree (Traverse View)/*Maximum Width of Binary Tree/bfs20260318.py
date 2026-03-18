# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 本题目的关键是对二叉树的节点按照行进行编号，然后就可以通过每一行的最左侧节点和最右侧节点的编号得到这一行的宽度，进而算出最大宽度
# 假设父亲节点的编号是x，那么左子节点的编号就是2*x，右子节点的编号就是2*x+1

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxwidth = 0
        q = collections.deque()
        q.append((root, 1))
        while q:
            size = len(q)
            start, end = 0, 0 # 这一行的第一个和最后一个节点
            for i in range(size): # 从左边到右边遍历每一行
                cur, idx = q.popleft()
                if i==0:
                    start = idx
                if i == size-1:
                    end = idx
                if cur.left:
                    q.append((cur.left, 2*idx))
                if cur.right:
                    q.append((cur.right, 2*idx+1))
            maxwidth = max(maxwidth, end-start+1)
        return maxwidth
        