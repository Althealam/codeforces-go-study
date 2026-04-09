# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input: root(TreeNode), voyage(list)
# output: values of all flipped nodes (list[int])

# 1. 题目类型：自顶向下
# 2. DFS三部曲
#（1）返回值含义：以当前节点为根的子树，是否能够通过反转匹配上voyage
#（2）携带信息：当前遍历到voyage的第几个元素（全局变量），当前节点
#（3）终止条件：
# - 已经遍历完voyage了，则说明已经找好了所有的flipped元素
# - 遇到的节点为空节点，则直接return True（空树默认匹配任何剩下的序列）
# - 如果node.val!=voyage[self.pos]：直接返回False
#（4）单层递归的逻辑
# - 移动指针：匹配当前根节点，self.pos+=1
# - 判断是否需要翻转
#   - 如果有左孩子，并且左孩子的值不等于voyage[self.pos]：说明左孩子对不上，尝试翻转。递归的时候先去右子树，再去左子树
#   - 否则：递归的时候先去左子树，再去右子树
# - 接收结果：获取left_res and right_res
class Solution:
    def __init__(self):
        self.pos = 0
        self.res = []
        self.voyage = []

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.voyage = voyage
        if self.dfs(root):
            return self.res
        return [-1]
    
    def dfs(self, node):
        if not node:
            return True
        if node.val!=self.voyage[self.pos]:
            return False
        else:
            self.pos+=1
            if node.left and node.left.val!=self.voyage[self.pos]:
                self.res.append(node.val)
                return self.dfs(node.right) and self.dfs(node.left)
            else:
                return self.dfs(node.left) and self.dfs(node.right)