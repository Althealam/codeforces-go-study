# 1. 构建图，其key是parents，value是children
# 思路：为了获取节点node的分数，我们需要找到其左右子树的大小（left和right），以及上面的子树的大小（count-left-right-1）
# 2. DFS三部曲：用于获取用node为根节点的子树的大小
#（1）携带参数：当前节点node
#（2）返回值含义：以node为根节点的子树的大小
#（3）终止条件：遇到空节点则直接返回0
#（4）单层递归的逻辑
# - 调用DFS获取左右子树的大小
# - 获取上面的子树的大小
# - 获取当前节点的分数值，并且更新hash表（key：节点分数，value：节点个数）

class Solution:
    def __init__(self):
        self.hash = {}
        self.maxscore = float('-inf')

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        numnodes = len(parents)
        graph = defaultdict(list)
        for i in range(1, len(parents)):
            graph[parents[i]].append(i)
        self.dfs(0, graph, numnodes)
        return self.hash[self.maxscore]
        
    def dfs(self, nodeidx, graph, numnodes):
        if nodeidx is None: # 不可以写成if not nodeidx，因为nodeidx=0的时候也会被认为是False
            return 0
        # 获取分数值
        leftidx = graph[nodeidx][0] if len(graph[nodeidx])>0 else None
        rightidx = graph[nodeidx][1] if len(graph[nodeidx])>1 else None
        leftsize = self.dfs(leftidx, graph, numnodes)
        rightsize = self.dfs(rightidx, graph, numnodes)
        uppersize = numnodes-leftsize-rightsize-1

        # 注意：leftsize和rightsize不可能是None，只有可能是0
        score = (leftsize if leftsize!=0 else 1)*(rightsize if rightsize!=0 else 1)*(uppersize if uppersize!=0 else 1)
        self.hash[score] = self.hash.get(score, 0)+1
        self.maxscore = max(self.maxscore, score)

        return leftsize+rightsize+1
