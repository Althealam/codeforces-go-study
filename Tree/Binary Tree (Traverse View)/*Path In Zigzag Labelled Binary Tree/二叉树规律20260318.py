# 是否要遍历节点：否，因为本题是无穷二叉树，遍历节点的话时间复杂度无限大

# 对于普通二叉树，父节点为label//2，但是本题是之字形，因此无法直接得到父节点
# 如何求二进制：1<<level = 2^level

# 1. 先忽略zigzag，只观察正常编号
# - 每一层的范围为：[2^(level-1), 2^level-1]（最右的节点是2^level-1，也就是本层的最大节点）
# - 父节点的关系：parent = label//2
# 2. 引入zigzag：奇数层从左到右，偶数层从右到左
# - 先将翻转的层反转回去，再寻找父节点
# - left<->right, left+1<->right-1, ..., right<->left
# 如果当前label是zigzag的值，那么原本的正常编号是normal=left+right-label
# - 找父节点的值：parent = normal//2
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        level = 0
        
        # 找到label的所在层
        while (1<<level)<=label:
            level+=1
        
        while label:
            res.append(label)

            left = 1<<(level-1)
            right = (1<<level)-1

            # 映射回正常的树
            label = left+right-label
            
            # 找父亲节点
            label//=2

            level -=1
        return res[::-1]
        