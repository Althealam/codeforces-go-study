# 1. 题目类型：自底向上（post order）
# 2. DFS三部曲：获取以node为根节点的子树的大小
#（1）携带参数：当前节点
#（2）返回值含义：以node为根节点的子树的大小
#（3）终止条件：遇到空节点则直接返回0
#（4）单层递归的逻辑
# - 调用DFS获取左右子树的大小leftsize, rightsize
# - 获取上面的树的大小：n-leftsize-rightsize-1
# - 获取当前节点的分数：leftsize*rightsize*(n-leftsize-rightsize-1)，并且更新到哈希表中
# - 返回当前子树的大小：leftsize+rightsize+1

class Solution:
    def __init__(self):
        self.count = {}
        self.maxscore = 0

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        numnodes = len(parents)
        graph = defaultdict(list)
        for i in range(1, len(parents)):
            graph[parents[i]].append(i) # parent->children
        
        self.dfs(0, graph, numnodes)
        return self.count[self.maxscore]
    
    def dfs(self, nodeidx, graph, numnodes):
        if nodeidx is None:
            return 0
        # 获取左右子树的大小
        leftidx = graph[nodeidx][0] if len(graph[nodeidx])>=1 else None
        rightidx = graph[nodeidx][1] if len(graph[nodeidx])>=2 else None
        
        leftsize = self.dfs(leftidx, graph, numnodes)
        rightsize = self.dfs(rightidx, graph, numnodes)

        upsize = numnodes-leftsize-rightsize-1

        score = (leftsize if leftsize!=0 else 1)*(rightsize if rightsize!=0 else 1)*(upsize if upsize!=0 else 1)

        self.count[score] = self.count.get(score, 0)+1
        self.maxscore = max(self.maxscore, score) 
        return leftsize+rightsize+1