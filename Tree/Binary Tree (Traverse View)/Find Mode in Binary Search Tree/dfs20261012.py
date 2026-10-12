# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 考虑到BST的有序性质，可以将空间复杂度从O(n)优化到O(h)
# BST的中序遍历是非递减序列，因此相同的元素一定连续出现，因此只需要记录前一个节点的值，就能统计当前元素的出现次数，不需要哈希表

# 1. 题目类型：自顶向下（不需要等待左右子树计算出结果，遍历过程直接更新count, max_count, result），当前节点的处理依赖中序遍历的前一个节点，而不是左右子树的返回值
# 2. dfs三部曲
#（1）返回值及含义：无，不需要返回当前子树的众数，只需要在dfs遍历过程中更新外部变量即可
#（2）携带参数及含义：当前正在访问的节点
# 同时维护四个状态变量
# - pre：上一个访问的节点
# - count：当前元素连续出现的次数
# - max_count：目前找到的最大频率
# - result：保存所有众数
#（3）终止条件：节点为空时，直接终止递归
#（4）单层递归逻辑
# - 递归左子树
# - 处理当前节点：判断当前节点的值是否和前面一个节点相同
# 如果相同的话，则元素连续出现，更新count
# 如果不同的话，则遇到了新的元素，count=1
# - 更新最大频率和结果数组
# 发现更大的频率，则更新最大频率值max_count，清空result
# 发现相同的更大频率
# - 递归右子树

# local：局部变量，表示当前函数内部的变量，作用领域为当前函数
# nonlocal：非局部变量，表示外层函数中的局部变量，作用领域为当前函数和嵌套函数

# 时间复杂度：O(n)，不管使用哪个方法，都需要遍历二叉树中的每个节点
# 空间复杂度：O(h)，DFS递归调用栈
# 1. 平衡二叉树：树的高度为logn
# 2. 退化为链表的二叉树：树的高度为n

class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        pre = None
        count = 0
        max_count = 0
        result = []
        def dfs(node):
            nonlocal pre, count, max_count
            # 终止条件
            if node is None:
                return 
            # 1. 递归左子树
            dfs(node.left)
            # 2. 处理当前节点
            if pre is None or pre.val!=node.val:
                count = 1
            else:
                count+=1
            # 更新众数
            if count>max_count:
                max_count = count
                result.clear() # 清空result数组
                result.append(node.val)
            elif count==max_count:
                result.append(node.val)
            
            # 更新前面一个节点
            pre = node 

            # 3. 递归右子树
            dfs(node.right)
        dfs(root)
        return result