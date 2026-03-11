# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 将每棵子树进行序列化，然后用哈希表重复出现次数
class Solution:
    def __init__(self):
        self.memo = {} # 所有子树以及出现的次数
        self.res = [] # 重复的子树根节点

    def serialize(self, root):
        if root == None:
            return '#'
        
        # 左右子树序列化
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        # 后序位置
        myself = left+","+right+","+str(root.val)

        # 获取该子树之前的出现次数
        if myself in self.memo:
            prev_freq = self.memo[myself]
        else:
            prev_freq = 0
        
        if prev_freq==1: # 这个子树不是第一次出现，之前已经出现过一次了
            self.res.append(root)
        self.memo[myself] = prev_freq+1
        return myself

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.serialize(root)
        return self.res
        