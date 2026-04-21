# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# root.val=min(root.left.val, root.right.val)
# root和root.child的情况是，要么root.val=root.child.val，要么root.val<root.child.val
# 根节点一定是全树的最小值

# 1. 题目类型：自顶向下
# 2. DFS三部曲：获取以node为根节点的子树的第二小的值
#（1）携带参数：当前节点node
#（2）返回值含义：以node为根节点的子树的第二小的值
#（3）终止条件：如果node为空节点，则返回-1；如果node没有任何的子节点，同样返回-1
#（4）单层递归的逻辑
# 如果node.left.val==node.val，说明第二小的子节点可能在左子树中，递归左子树
# 如果node.left.val>node.val，说明左子节点就是第二小的值

# 如果node.right.val==node.val，说明第二小的子节点可能在右子树中，递归右子树
# 如果node.right.val>node.val，说明右子节点就是第二小的值

# 这时候已经获取了left和right，分别表示以node.left和node.right为根节点的子树的第二小的值
# 合并left和right，如果left=-1则返回right，如果right=-1则返回left，否则返回min(left, right)

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    def dfs(self, node):
        if not node or (node.left is None and node.right is None):
            return -1
        
        if node.left.val==node.val:
            left = self.dfs(node.left)
        elif node.left.val>node.val:
            left = node.left.val
        
        if node.right.val==node.val:
            right = self.dfs(node.right)
        elif node.right.val>node.val:
            right = node.right.val
        
        if left==-1:
            return right
        if right==-1:
            return left
        return min(left, right)