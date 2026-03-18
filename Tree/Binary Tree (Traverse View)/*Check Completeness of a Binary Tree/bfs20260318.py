# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 完全二叉树：除了最后一层，其余每一层必须是被完全填满的，最后一层的节点要尽可能的靠左排列
# 分析：判断层序遍历的时候，中间是否有断点，可以判断放进去的index是否连续来判断
# index可以用来获取所有节点的索引，而count则是用来获取所有非空节点的数量
# 如果一颗树是完全二叉树，那么他的编号一定是连续的

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append([root, 1])
        count, last_index = 0, 0
        while q:
            size = len(q)
            for _ in range(size):
                cur, idx = q.popleft()
                if cur: # 如果不是空节点，那么就要更新last_index和count
                    last_index = idx
                    count+=1
                    q.append([cur.left, 2*idx])
                    q.append([cur.right, 2*idx+1])
        return count==last_index
