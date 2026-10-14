# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 字典序的比较可以直接利用Python的字符串比较运算符完成
# 字典序：英文字典中单词的排列顺序（比如s1=abc, s2=abd, s1<s2是true）
# 如何将数字转换为英文：chr(node.val)+ord('a')

# 1. 题目类型：自顶向下，中序遍历
# 2. 递归三部曲
# （1）携带参数和返回值：携带参数为当前遍历的节点，和当前的路径，无返回值
# （2）终止条件：如果节点为空，则直接返回；如果为叶子节点，则更新最小的字符串
# （3）单层节点的更新：当前路径加入当前节点的值，递归左右子树，并且回溯

# 注意点：
# 1. 如何根据node的值获取对应的字母
# 2. 如何比较两个字符串的字典序（可以直接用python的<或者>）
# 3. 回溯操作
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = None
        def dfs(node, path):
            nonlocal res
            if not node:
                return 
            path.append(chr(node.val+ord("a")))
            if node.left is None and node.right is None:
                cur_path = "".join(path[::-1])
                if res is None or cur_path<res:
                    res = cur_path
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            
            # 回溯
            path.pop()
        dfs(root, [])
        return res
        