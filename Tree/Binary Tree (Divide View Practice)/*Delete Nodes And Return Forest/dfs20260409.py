# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 题目类型：自底向上
# 子节点直接返回空，让父亲节点指向空节点，来执行删除操作
# 2. DFS三部曲
#（1）返回值含义：处理完后的子树根节点
#（2）携带信息：to_delete, is_root（表示当前节点是否是根节点，也就是父亲节点是否被删了），当前节点
#（3）单层递归的逻辑
# - 单层逻辑
#   - 判断一下自己是否要被删除：获取一个bool值
#   - 如果自己没有被删除，并且父亲被删除了，则说明找到了一个答案值，更新答案值
#   - 如果is_deleted=True，说明自己要被删除，则返回一个空值，用来向上汇报
#   - 如果is_deleted=False，说明自己不会被删除，则处理左右儿子，并且左右儿子都是根节点，则is_root=True

class Solution:
    def __init__(self):
        self.res = []
        self.todeleteset = None

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.todeleteset = set(to_delete)
        self.dfs(True, root)
        return self.res

    
    def dfs(self, is_root, node):
        if not node:
            return None
        
        # 确定自己是否要被删
        is_deleted = node.val in self.todeleteset

        # 如果自己没有被删，并且父亲被删了，那么自己就是新的根
        if is_root and not is_deleted:
            self.res.append(node)

        # 自底向上重新连接
        node.left = self.dfs(is_deleted, node.left)
        node.right = self.dfs(is_deleted, node.right)

        # 向上汇报
        return None if is_deleted else node


        