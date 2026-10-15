#
# @lc app=leetcode.cn id=1457 lang=python3
# @lcpr version=30403
#
# [1457] 二叉树中的伪回文路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 伪回文：一条路径中，最多只有一个节点值出现奇数次
# 题目类型：自顶向下
# 递归三部曲
#（1）携带参数和返回值含义：当前节点值，当前路径下的哈希表，当前路径下出现频率为奇数的节点集合，无返回值
#（2）终止条件：遇到空节点则直接返回
#（3）单层递归的逻辑
# - 更新当前节点的出现频率
# - 如果当前节点是叶子节点，则判断当前路径是不是伪回文路径，如果是的话更新答案值
# - 如果当前节点不是叶子节点，则递归左右子树
# - 回溯

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode | None) -> int:
        res = 0
        def dfs(node, freq_map):
            nonlocal res
            if not node:
                return 
            if node.val not in freq_map:
                freq_map[node.val]=1
            else:
                freq_map[node.val]+=1
            
            if node.left is None and node.right is None:
                cnt = 0
                for value, freq in freq_map.items():
                    if freq%2!=0:
                        cnt+=1
                if cnt<=1:
                    res+=1
            else:
                dfs(node.left, freq_map)
                dfs(node.right, freq_map)
            
            freq_map[node.val]-=1
        
        dfs(root, {})
        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)
sol = Solution()
res = sol.pseudoPalindromicPaths(root)
print(res)


        
# @lc code=end



#
# @lcpr case=start
# [2,3,1,3,1,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1,1,3,null,null,null,null,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [9]\n
# @lcpr case=end

#

