# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 暴力法：DFS遍历整棵树+哈希表统计频率
# dfs三部曲
# 1. 题目类型：自顶向下
# 2. 返回值及含义：无返回值（freq_map是一个可变字典，所有递归调用共享同一个字典对象，因此不需要通过return返回它）
# 3. 携带参数及含义
# cur：当前正在访问的节点
# freq_map：记录元素出现次数的哈希表
# 4. 终止条件：当前节点为空时，终止递归
# 5. 单层递归的逻辑
# - 处理当前节点，将当前节点值的出现次数加1
# - 递归左子树，即统计左子树中每个元素的出现次数
# - 递归右子树，即统计右子树中每个元素的出现次数

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def searchBST(self, cur, freq_map):
        if cur is None:
            return 
        freq_map[cur.val]+=1 # 统计元素频率
        self.searchBST(cur.left, freq_map)
        self.searchBST(cur.right, freq_map)

    def findMode(self, root: TreeNode | None) -> list[int]:
        freq_map = defaultdict(int) # key: 元素，value：出现频率
        result = []
        if root is None:
            return result
        self.searchBST(root, freq_map)
        max_freq = max(freq_map.values())
        for key, freq in freq_map.items():
            if freq==max_freq:
                result.append(key)
        return result
        