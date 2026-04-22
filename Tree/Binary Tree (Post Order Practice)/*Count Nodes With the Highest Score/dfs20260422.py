# 1. 将parents转换为字典，key为parents，value为children
# 2. 题目类型：自底向上（分解问题）
# 3. DFS三部曲：获取以node为根节点的子树的大小
#（1）携带参数：当前节点node，转换后的图
#（2）返回值含义：以node为根节点的子树的大小
#（3）终止条件：遇到空节点则返回0
#（4）单层递归的逻辑
# - 获取左右子树的大小leftsize, rightsize
# - 获取上面的子树的大小：numnodes-leftsize-rightsize-1
# - 获取当前节点的分数：leftsize*rightsize*uppersize
# - 更新当前节点的分数值到hash表中
# - 获取当前子树的大小：cur=leftsize+rightsize+1
class Solution:
    def __init__(self):
        self.hash = {}

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(1, len(parents)):
            graph[parents[i]].append(i)
        
        numnodes = len(parents)
        self.dfs(0, graph, numnodes)
        maxscore = max(self.hash.keys())
        return self.hash[maxscore]
        

    def dfs(self, nodeidx, graph, numnodes):
        if nodeidx is None:
            return 0
        leftidx = graph[nodeidx][0] if len(graph[nodeidx])>0 else None
        rightidx = graph[nodeidx][1] if len(graph[nodeidx])>1 else None
        leftsize = self.dfs(leftidx, graph, numnodes)
        rightsize = self.dfs(rightidx, graph, numnodes)
        uppersize = numnodes-leftsize-rightsize-1
        cursize = leftsize+rightsize+1
        curscore = (leftsize if leftsize>0 else 1)*(rightsize if rightsize>0 else 1)*(uppersize if uppersize>0 else 1)
        self.hash[curscore] = self.hash.get(curscore, 0)+1
        return cursize