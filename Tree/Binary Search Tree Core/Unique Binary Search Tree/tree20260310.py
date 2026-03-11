class Solution:
    def numTrees(self, n: int) -> int:
        return self.count(1, n) # 计算闭区间[1, n]组成的BST个数

    # 计算闭区间[lo, hi]组成的BST个数
    def count(self, lo, hi):
        if lo>hi:
            return 1
        res = 0
        for i in range(lo, hi+1):
            # i的值作为根节点root
            left = self.count(lo, i-1)
            right = self.count(i+1, hi)
            # 左右子树的组合数乘积是BST的总数
            res += left*right
        return res
