#
# @lc app=leetcode.cn id=1110 lang=python3
# @lcpr version=30404
#
# [1110] 删点成林
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题目类型：自底向上

# 递归三部曲
#（1）携带参数和返回值的含义
# - 携带参数：当前需要处理的子树根节点cur，需要删除的节点值数组
# - 返回值含义：删除当前子树中所有需要删除的节点后，这棵子树剩余的根节点（返回的是treenode，而不是list）
#（2）终止条件：当前节点为空，则直接返回空
#（3）单层递归的逻辑
# - 删除左子树
# - 删除右子树
# - 判断当前根节点是否需要删除
#   - 如果需要删除当前根节点：将处理后的左右子树加入到ans中
#   - 如果不需要删除当前根节点：保留当前节点，并连接处理后的左右子树
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        delete_set = set(to_delete)

        def dfs(cur):
            if not cur:
                return None

            # 1. 递归处理左右子树
            left = dfs(cur.left)
            right = dfs(cur.right)

            # 2. 当前节点不需要删除
            if cur.val not in delete_set:
                cur.left = left
                cur.right = right
                return cur

            # 3. 当前节点需要删除
            else:
                if left:
                    ans.append(left)

                if right:
                    ans.append(right)

                return None

        # 4. 处理原始根节点
        new_root = dfs(root)

        if new_root:
            ans.append(new_root)

        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n[3,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,null,3]\n[3]\n
# @lcpr case=end

#

