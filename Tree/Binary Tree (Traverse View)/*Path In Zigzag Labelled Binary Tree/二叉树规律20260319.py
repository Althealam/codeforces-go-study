# 1. 在zigzag之前，父亲节点和子节点的关系为：假设父亲节点的索引为index，那么左孩子的索引为2*index，右孩子的索引为2*index+1
# 2. 在zigzag之后，对应的关系为
# index, index+1, ..., index+n <=> index+n, index+n-1, ..., index+1, index
# original = left+right-index
# 3. 对于二叉树，如果他的层数是level，那么该层的节点为[2^(level-1), 2^level-1]，因此left为2^(level-1)，right为2^level-1

# 思路：
# 1. 找到label所在的层，只要找到刚好2^level-1>label的level即可
# 2. 获取映射回去后的值，通过original = left+right-index，然后获取其original的父亲节点，将父亲节点加入到res中
# 3. 将最终的res倒序即可res=res[::-1]

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        level = 0
        # 1. 找到label的所在层
        while 2**level-1<label:
            level+=1
        
        # 2. 依次获取父亲节点，直到找到根节点
        while label:
            res.append(label)
            # 一定要获取这一层的左右边界，才能映射
            left = 2**(level-1)
            right = 2**level-1
            label = left+right-label # 映射回原来的值
            label//=2 # 获取其父亲节点
            level-=1 # 到上一层
        return res[::-1]
        