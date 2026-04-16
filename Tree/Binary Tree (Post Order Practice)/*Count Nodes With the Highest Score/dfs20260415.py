# 1. 题目类型：自底向下
# 2. DFS三部曲：获取以某个节点node为根的子树的大小
#（1）携带参数：node（当前处理的节点序号）
#（2）返回值：以当前节点为根的子树总节点数
#（3）终止条件：如果遇到空节点，则返回0
#（4）单层递归的逻辑
# - 调用单层递归，获取左右子树的大小
# - 计算得分：左子树大小为l_size，右子树大小为r_size，上方部分的大小为n-l_size-r_size-1，更新得分为l_size*r_size*(n-l_size-r_size-1)
# - 更新最高分，并且更新哈希表
# - 向上汇报，返回当前子树的总大小：l_size+r_size+1

class Solution:
    def __init__(self):
        self.maxsize = 0
        self.count = defaultdict(list)

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)] # 邻接表示树
        for i, p in enumerate(parents):
            if p!=-1:
                children[p].append(i) # 父亲节点->孩子节点（不包括根节点）
        
        self.dfs(0, children, n)
        return len(self.count[self.maxsize])
    
    def dfs(self, node_idx, children, totalnode):
        """获取以node_idx为根节点的子树的大小"""
        if node_idx is None:
            return 0
        left_child = children[node_idx][0] if len(children[node_idx])>=1 else None
        right_child = children[node_idx][1] if len(children[node_idx])>=2 else None
        
        # 获得左子树的大小
        l_size = self.dfs(left_child, children, totalnode)
        # 获得右子树的大小
        r_size = self.dfs(right_child, children, totalnode)

        # 获取上面的子树的大小
        upsize = totalnode-l_size-r_size-1

        score = (l_size if l_size>0 else 1)*(r_size if r_size>0 else 1)*(upsize if upsize>0 else 1)

        self.maxsize = max(self.maxsize, score)
        self.count[score].append(node_idx)
        return l_size+r_size+1

